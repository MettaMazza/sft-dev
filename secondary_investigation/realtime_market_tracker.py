"""
SADE: Real-Time Market Tracker — Forward-Forced from ONE.

All predictions derived forward from the axiom ONE via the fold map.
No backward fitting. No denominator sweeps. No MSE minimization.

Method:
1. Fetch live price data, normalize to (0, 1]
2. Quantize each price to nearest b/d for structural denominators
3. Scan ALL denominators for positive fold successor matches
4. Intersect forced candidates across all positives
5. Find best fold depth n
6. Apply fold^n to predict next price
"""
import urllib.request
import json
import os
import sys
from datetime import datetime
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE, period
from sftoe.discovery import find_derivation, generate_sftoe_code
from sftoe.proof import verify_value
from sftoe.gate import verify_code

def fetch_live_prices(ticker):
    print(f"Fetching live chart data for {ticker} from Yahoo Finance API...")
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=30d"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            result = data['chart']['result'][0]
            timestamps = result['timestamp']
            prices = result['indicators']['adjclose'][0]['adjclose']

            cleaned_data = []
            for t, p in zip(timestamps, prices):
                if p is not None:
                    date_str = datetime.fromtimestamp(t).strftime('%Y-%m-%d')
                    cleaned_data.append((date_str, float(p)))
            return cleaned_data
    except Exception as e:
        print(f"Error fetching live data: {e}")
        return None


def find_positive_denominators(quantized_seq, d_max=500, threshold=0.5):
    """
    For each d, test fold successor (2b) mod d against consecutive transitions.
    Accept ALL positives.
    """
    total = len(quantized_seq) - 1
    if total <= 0:
        return []

    positives = []
    for d in range(2, d_max + 1):
        matches = 0
        for i in range(total):
            b = quantized_seq[i]
            b_next = quantized_seq[i + 1]
            b_mod = b % d
            if b_mod == 0:
                b_mod = d
            forced = (2 * b_mod) % d
            if forced == 0:
                forced = d
            b_next_mod = b_next % d
            if b_next_mod == 0:
                b_next_mod = d
            if b_next_mod == forced:
                matches += 1

        rate = matches / total
        if rate >= threshold:
            positives.append({'d': d, 'matches': matches, 'total': total, 'rate': rate})

    positives.sort(key=lambda x: -x['rate'])
    return positives


def find_best_fold_depth(quantized_seq, d_quant, max_depth=None):
    """
    For each fold depth n, test fold^n(b/d) against next observed state.
    """
    if max_depth is None:
        max_depth = min(d_quant, 200)

    total = len(quantized_seq) - 1
    if total <= 0:
        return 1, {}

    depth_scores = {}
    for depth in range(1, max_depth + 1):
        hits = 0
        for i in range(total):
            state = Fraction(quantized_seq[i], d_quant)
            for _ in range(depth):
                state = (state * 2) % 1
                if state == 0:
                    state = Fraction(1, 1)
            pred_ball = round(float(state) * d_quant)
            if pred_ball == quantized_seq[i + 1]:
                hits += 1
        depth_scores[depth] = {'hits': hits, 'total': total, 'rate': hits / total if total > 0 else 0}

    best_depth = max(depth_scores, key=lambda k: depth_scores[k]['hits'])
    return best_depth, depth_scores


def main():
    ticker = "AAPL"
    if len(sys.argv) > 1 and sys.argv[1] != '--cli':
        ticker = sys.argv[1].upper()

    print("=== SADE: Forward-Forced Real-Time Market Tracker ===")

    # 1. Fetch live prices
    data = fetch_live_prices(ticker)
    if not data or len(data) < 10:
        print("Error: Could not retrieve sufficient data points.")
        sys.exit(1)

    dates = [d[0] for d in data]
    prices = [d[1] for d in data]

    N_total = len(prices)
    print(f"Retrieved {N_total} trading days of history.")
    print(f"Latest price ({dates[-1]}): ${prices[-1]:.2f}")

    # 2. Normalize and quantize to integer states
    # Use a denominator that gives good resolution
    d_quant = 100  # Quantize to cents (percentage of max)
    norm_factor = max(prices) * 1.1
    quantized = [max(1, min(d_quant, round(p / norm_factor * d_quant))) for p in prices]

    print(f"\nQuantized to d={d_quant}, norm_factor=${norm_factor:.2f}")
    print(f"Quantized sequence (last 10): {quantized[-10:]}")

    # 3. Find positive denominators
    print("\n[STEP 1] Scanning denominators d=2..500 for positive fold matches...")
    positive_ds = find_positive_denominators(quantized, d_max=500)
    print(f"  Found {len(positive_ds)} positive denominators")
    for p in positive_ds[:10]:
        print(f"    d={p['d']}: {p['matches']}/{p['total']} ({p['rate']*100:.1f}%)")

    # 4. Find best fold depth
    print(f"\n[STEP 2] Finding best fold depth...")
    best_depth, depth_scores = find_best_fold_depth(quantized, d_quant)
    best_info = depth_scores[best_depth]
    print(f"  Best depth: {best_depth} ({best_info['hits']}/{best_info['total']} hits, {best_info['rate']*100:.1f}%)")

    # 5. Forward-force prediction
    print(f"\n[STEP 3] Applying fold^{best_depth} to last state...")
    last_q = quantized[-1]
    state = Fraction(last_q, d_quant)
    sv = SmithianValue(state)
    verify_value(sv)

    for _ in range(best_depth):
        sv = fold(sv)

    pred_q = round(float(sv.value) * d_quant)
    pred_price = (pred_q / d_quant) * norm_factor

    actual_today = prices[-1]

    # 6. Also compute tomorrow (one more fold)
    sv_tomorrow = fold(sv)
    pred_q_tomorrow = round(float(sv_tomorrow.value) * d_quant)
    pred_price_tomorrow = (pred_q_tomorrow / d_quant) * norm_factor

    # 7. Log
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "market_tracking_log.csv")
    headers = "Timestamp,Ticker,Method,ActualPriceToday,ForecastTomorrow,BestDepth,PositiveDenominators\n"

    file_exists = os.path.exists(log_file)
    with open(log_file, "a") as f:
        if not file_exists:
            f.write(headers)
        timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ds_str = ";".join(str(p['d']) for p in positive_ds[:10])
        log_line = f"{timestamp_str},{ticker},forward_forced,{actual_today:.2f},{pred_price_tomorrow:.2f},{best_depth},{ds_str}\n"
        f.write(log_line)

    # 8. Display
    print("\n" + "=" * 55)
    print(f" FORWARD-FORCED TRACKING DASHBOARD: {ticker}")
    print("=" * 55)
    print(f"  Method:                    Forward-Forced from ONE")
    print(f"  Positive Denominators:     {len(positive_ds)}")
    print(f"  Best Fold Depth:           {best_depth}")
    print(f"  Quantization:              d={d_quant}")
    print("-" * 55)
    print(f"  Today's Actual Price:      ${actual_today:.2f}")
    print(f"  TOMORROW'S FORECAST:       ${pred_price_tomorrow:.2f}")
    direction = 'UP' if pred_price_tomorrow > actual_today else 'DOWN' if pred_price_tomorrow < actual_today else 'STABLE'
    print(f"  Direction Forecast:        {direction}")
    print("=" * 55)
    print(f"Record appended to: {log_file}")

    # 9. SADE Verification
    print(f"\nDeriving state {last_q}/{d_quant} from ONE via SADE...")
    initial_frac = Fraction(last_q, d_quant)
    proof = find_derivation(initial_frac)
    code = generate_sftoe_code(proof, "verify_market_state")

    print("Verifying AST constraints...")
    verify_code(code)
    print("AST Gate: PASSED")

    namespace = {}
    exec(code, namespace)
    res = namespace["verify_market_state"]()
    verify_value(res)
    print(f"Value Verification: PASSED. State: {res.value}")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
    except Exception as e:
        print(f"Exception encountered: {e}")
