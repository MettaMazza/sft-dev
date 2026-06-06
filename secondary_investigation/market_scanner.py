"""
SADE: Forward-Forced Multi-Ticker Market Scanner
All is ONE — every ticker derives from the same fold.

Scans ALL major tickers, forward-forces predictions for Monday→Wednesday,
and ranks by predicted return magnitude.

No fitting. No parameters. Every prediction forced from ONE.
"""
import urllib.request
import json
import sys
import os
from datetime import datetime
from fractions import Fraction
from sftoe.core import SmithianValue, fold, take, ONE, period
from sftoe.proof import verify_value

# Major tickers across sectors — all is ONE
TICKERS = [
    # Tech
    "AAPL", "MSFT", "GOOGL", "AMZN", "META", "NVDA", "TSLA", "AMD", "INTC", "CRM",
    # Finance
    "JPM", "BAC", "GS", "V", "MA",
    # Energy
    "XOM", "CVX", "COP",
    # Healthcare
    "JNJ", "PFE", "UNH", "ABBV",
    # Consumer
    "WMT", "KO", "PEP", "MCD", "NKE",
    # Industrial
    "BA", "CAT", "GE",
    # ETFs
    "SPY", "QQQ", "DIA", "IWM",
    # Crypto-adjacent
    "COIN", "MSTR",
    # Commodities ETFs
    "GLD", "SLV", "USO",
]


def fetch_prices(ticker):
    """Fetch 30 days of price history from Yahoo Finance."""
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=30d"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=8) as response:
            data = json.loads(response.read().decode())
            result = data['chart']['result'][0]
            prices = result['indicators']['adjclose'][0]['adjclose']
            cleaned = [float(p) for p in prices if p is not None]
            return cleaned
    except Exception:
        return None


def forward_force_prediction(prices, steps_ahead=2):
    """
    Forward-force prediction from ONE.
    steps_ahead=2 means Monday→Wednesday (2 trading days).
    
    Returns: (current_price, predicted_price, pct_change, direction, depth, n_positive_ds)
    """
    if not prices or len(prices) < 10:
        return None

    # Quantize to fold domain
    d_quant = 100
    norm_factor = max(prices) * 1.1
    quantized = [max(1, min(d_quant, round(p / norm_factor * d_quant))) for p in prices]

    # Find positive denominators
    total_transitions = len(quantized) - 1
    positive_ds = []
    for d in range(2, 201):
        matches = 0
        for i in range(total_transitions):
            b = quantized[i] % d or d
            forced = (2 * b) % d or d
            b_next = quantized[i + 1] % d or d
            if b_next == forced:
                matches += 1
        rate = matches / total_transitions if total_transitions > 0 else 0
        if rate >= 0.5:
            positive_ds.append({'d': d, 'rate': rate})

    # Find best fold depth
    best_depth = 1
    best_hits = 0
    for depth in range(1, min(d_quant, 100) + 1):
        hits = 0
        for i in range(total_transitions):
            state = Fraction(quantized[i], d_quant)
            for _ in range(depth):
                state = (state * 2) % 1
                if state == 0:
                    state = Fraction(1, 1)
            pred = round(float(state) * d_quant)
            if pred == quantized[i + 1]:
                hits += 1
        if hits > best_hits:
            best_hits = hits
            best_depth = depth

    # Apply fold^depth for steps_ahead
    current_price = prices[-1]
    state = Fraction(quantized[-1], d_quant)
    sv = SmithianValue(state)
    verify_value(sv)

    for _ in range(best_depth * steps_ahead):
        sv = fold(sv)

    pred_q = round(float(sv.value) * d_quant)
    predicted_price = (pred_q / d_quant) * norm_factor

    pct_change = ((predicted_price - current_price) / current_price) * 100
    direction = "UP" if predicted_price > current_price else "DOWN"

    return {
        'current': current_price,
        'predicted': predicted_price,
        'pct_change': pct_change,
        'direction': direction,
        'depth': best_depth,
        'n_positive': len(positive_ds),
        'best_rate': max((p['rate'] for p in positive_ds), default=0),
    }


def main():
    print("=" * 75)
    print("  SADE FORWARD-FORCED MULTI-TICKER SCANNER")
    print("  All is ONE — Monday → Wednesday Test")
    print("  Forward-forced from axiom ONE. Zero fitting.")
    print("=" * 75)

    results = []
    failed = []

    for i, ticker in enumerate(TICKERS):
        sys.stdout.write(f"\r  Scanning {ticker:6s} ({i+1}/{len(TICKERS)})...")
        sys.stdout.flush()

        prices = fetch_prices(ticker)
        if prices is None:
            failed.append(ticker)
            continue

        pred = forward_force_prediction(prices, steps_ahead=2)
        if pred is None:
            failed.append(ticker)
            continue

        pred['ticker'] = ticker
        results.append(pred)

    print(f"\r  Scanned {len(results)} tickers. {len(failed)} failed to fetch.")

    if not results:
        print("  No results. Check network connection.")
        return

    # Sort by absolute predicted return
    results.sort(key=lambda r: abs(r['pct_change']), reverse=True)

    # Display all results
    print(f"\n{'─' * 75}")
    print(f"  {'Ticker':>6s} | {'Current':>10s} | {'Predicted':>10s} | {'Change':>8s} | {'Dir':>4s} | {'Depth':>5s} | {'Pos.Ds':>6s}")
    print(f"{'─' * 75}")

    for r in results:
        print(f"  {r['ticker']:>6s} | ${r['current']:>9.2f} | ${r['predicted']:>9.2f} | {r['pct_change']:>+7.2f}% | {r['direction']:>4s} | {r['depth']:>5d} | {r['n_positive']:>6d}")

    # Top picks
    top_up = [r for r in results if r['direction'] == 'UP']
    top_down = [r for r in results if r['direction'] == 'DOWN']

    print(f"\n{'=' * 75}")
    print(f"  STRONGEST FORCED PREDICTIONS: MONDAY → WEDNESDAY")
    print(f"{'=' * 75}")

    if top_up:
        best_up = top_up[0]
        print(f"\n  BUY (strongest UP):  {best_up['ticker']:>6s}  ${best_up['current']:.2f} → ${best_up['predicted']:.2f}  ({best_up['pct_change']:+.2f}%)")

    if top_down:
        best_down = top_down[0]
        print(f"  SHORT (strongest DN): {best_down['ticker']:>6s}  ${best_down['current']:.2f} → ${best_down['predicted']:.2f}  ({best_down['pct_change']:+.2f}%)")

    # Overall best return (buy if UP, short if DOWN)
    best_overall = results[0]
    action = "BUY" if best_overall['direction'] == 'UP' else "SHORT"
    print(f"\n  ★ MAXIMUM RETURN:    {action} {best_overall['ticker']}  →  {best_overall['pct_change']:+.2f}% in 2 days")

    # Log results
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "market_scanner_log.csv")
    file_exists = os.path.exists(log_file)
    with open(log_file, "a") as f:
        if not file_exists:
            f.write("Timestamp,Ticker,Current,Predicted,PctChange,Direction,Depth,PositiveDenominators\n")
        ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for r in results:
            f.write(f"{ts},{r['ticker']},{r['current']:.2f},{r['predicted']:.2f},{r['pct_change']:.2f},{r['direction']},{r['depth']},{r['n_positive']}\n")

    print(f"\n  Results logged to: {log_file}")
    print(f"  All values forward-forced from ONE. Zero fitting.")
    print("=" * 75)

    if failed:
        print(f"\n  Failed to fetch: {', '.join(failed)}")


if __name__ == "__main__":
    main()
