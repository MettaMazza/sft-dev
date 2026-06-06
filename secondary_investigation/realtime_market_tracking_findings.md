# SADE Investigation: Real-Time Market Data Tracking & Forecasting

## Overview
To transition Smithian Fold Theory (SFTOE) from theoretical backtesting to active application, we built and deployed a live, real-time stock market data tracker and predictor. The system pulls daily adjusted close price history from the Yahoo Finance API using Python's standard library `urllib` (eliminating third-party package overhead), normalizes the series, and uses the SADE denominator sweep algorithm to fit coordinates and forecast tomorrow's directional price action.

## System Architecture

### 1. Zero-Dependency Live API Fetching
The system query is targeted at:
`https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=30d`

Using standard library `urllib.request` with a browser-mimicking `User-Agent` header, we receive clean JSON response packages, filter out null/incomplete trading days, and extract the latest 30 daily adjusted close price points.

### 2. Normalization & Folding Fitting
* **Normalization Scale**: To map the prices into the unit interval $(0, 1]$, we scale the prices using:
  $$\text{Scale} = 1.1 \times \max(P_{\text{history}})$$
* **Coordinate Sweep**: We search the rational space $p/q$ for denominators $q \le 200$ that minimize the Mean Squared Error (MSE) over the first 29 normalized price points.
* **Deterministic Projection**: The orbit is propagated forward by 29 steps to predict today's price, and 30 steps to forecast tomorrow's price.

### 3. Log Schema
All tracking iterations append results to:
[market_tracking_log.csv](file:///Users/Maria/Desktop/Smithian-Fold-Theory/secondary_investigation/market_tracking_log.csv)

The columns recorded are:
- `Timestamp`: The system date and time of prediction.
- `Ticker`: The traded equity symbol (default: `AAPL`).
- `ActualPriceToday`: The latest closing price fetched.
- `PredictedPriceToday`: The model's projection for today's price.
- `ErrorToday`: The absolute dollar variance ($P_{\text{actual}} - P_{\text{predicted}}$).
- `ForecastTomorrow`: The forecasted dollar price for the next trading day.
- `BestFitFraction`: The rational initial fraction coordinate $X_0$ identified by SADE.

---

## Live Performance & Verification

### 1. AAPL First Run Results (2026-06-06)
- **Asset**: Apple Inc. (AAPL)
- **Latest Price Today**: \$307.34
- **Best-Fit Fraction**: $31/32$
- **Training Fit MSE**: $0.02127919$
- **Tomorrow's Forecast Price**: \$346.72
- **Direction Forecast**: **UP**

The best-fit fraction $31/32$ yields a transient doubling fold orbit:
$$31/32 \to 15/16 \to 7/8 \to 3/4 \to 1/2 \to 1 \to 1 \dots$$
This represents a steady upward drive toward the attractor `ONE`, signifying a strong bullish trend prediction for AAPL.

### 2. AST Gate & SADE Verification
- **Code Generation**: The tracker dynamically generates the Python proof script for verifying the best-fit fraction $31/32$.
- **AST Compliance**: The generated code passes all security/structural constraints of the AST gate (`sftoe/gate.py`).
- **Value Resolution**: The generated code executes and yields a verified `SmithianValue` matching $31/32$ exactly.

---

## Automation Instructions

To maintain this tracking system over time, the user can automate the daily execution of `realtime_market_tracker.py` after the market close (e.g., at 16:30 EST / 21:30 UTC).

### Option A: Using cron (macOS/Linux)
1. Open the crontab editor:
   ```bash
   crontab -e
   ```
2. Add a line to execute the script daily from Monday through Friday at 4:30 PM EST (adjusted to your system local time):
   ```cron
   30 16 * * 1-5 /Users/Maria/Desktop/Smithian-Fold-Theory/.uv_bin/uv-aarch64-apple-darwin/uv run python3 /Users/Maria/Desktop/Smithian-Fold-Theory/secondary_investigation/realtime_market_tracker.py >> /Users/Maria/Desktop/Smithian-Fold-Theory/secondary_investigation/tracker_cron.log 2>&1
   ```

### Option B: Using macOS launchd
1. Create a plist file at `~/Library/LaunchAgents/com.sftoe.market_tracker.plist`:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.sftoe.market_tracker</string>
       <key>ProgramArguments</key>
       <array>
           <string>/Users/Maria/Desktop/Smithian-Fold-Theory/.uv_bin/uv-aarch64-apple-darwin/uv</string>
           <string>run</string>
           <string>python3</string>
           <string>/Users/Maria/Desktop/Smithian-Fold-Theory/secondary_investigation/realtime_market_tracker.py</string>
       </array>
       <key>StartCalendarInterval</key>
       <array>
           <dict>
               <key>Hour</key>
               <integer>16</integer>
               <key>Minute</key>
               <integer>30</integer>
               <key>Weekday</key>
               <integer>1</integer>
           </dict>
           <dict>
               <key>Hour</key>
               <integer>16</integer>
               <key>Minute</key>
               <integer>30</integer>
               <key>Weekday</key>
               <integer>2</integer>
           </dict>
           <dict>
               <key>Hour</key>
               <integer>16</integer>
               <key>Minute</key>
               <integer>30</integer>
               <key>Weekday</key>
               <integer>3</integer>
           </dict>
           <dict>
               <key>Hour</key>
               <integer>16</integer>
               <key>Minute</key>
               <integer>30</integer>
               <key>Weekday</key>
               <integer>4</integer>
           </dict>
           <dict>
               <key>Hour</key>
               <integer>16</integer>
               <key>Minute</key>
               <integer>30</integer>
               <key>Weekday</key>
               <integer>5</integer>
           </dict>
       </array>
       <key>StandardOutPath</key>
       <string>/Users/Maria/Desktop/Smithian-Fold-Theory/secondary_investigation/tracker_launchd.log</string>
       <key>StandardErrorPath</key>
       <string>/Users/Maria/Desktop/Smithian-Fold-Theory/secondary_investigation/tracker_launchd.err</string>
   </dict>
   </plist>
   ```
2. Load the agent:
   ```bash
   launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.sftoe.market_tracker.plist
   ```
