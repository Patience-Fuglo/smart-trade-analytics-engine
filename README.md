# Smart Trade Analytics Engine

A modular Python trade analytics engine that simulates core quantitative trading workflows—data validation, trade processing, PnL computation, and summary metrics.

## Features

- **Trade Processing Pipeline** – Symbol normalization, input validation, safe handling of invalid data
- **PnL Analytics** – Profit/Loss calculation, return percentage, trade classification (PROFIT/LOSS/BREAKEVEN)
- **Risk Flagging** – Rule-based detection for high-risk trades (>5% negative return)
- **Summary Metrics** – Total PnL, win/loss counts, best and worst trade identification
- **Test Coverage** – Unit tests with pytest

## Project Structure

```
smart-trade-analytics-engine/
├── src/
│   ├── __init__.py
│   └── main.py          # Core analytics engine
├── tests/
│   └── test_main.py     # Unit tests
├── requirements.txt
├── pytest.ini
└── README.md
```

## Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/smart-trade-analytics-engine.git
cd smart-trade-analytics-engine

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Git Commands

```bash
# Initialize repository (first time only)
git init

# Stage all changes
git add .

# Commit changes
git commit -m "Your commit message"

# Add remote origin (first time only)
git remote add origin https://github.com/yourusername/smart-trade-analytics-engine.git

# Push to GitHub
git push -u origin main
```

## Usage

### Run the Analytics Engine

```bash
python src/main.py
```

**Sample Output:**
```
Cleaned Trade Log:
{'symbol': 'AAPL', 'buy_price': 150.0, 'sell_price': 160.0, 'quantity': 10, 'pnl': 100.0, 'return_pct': 6.67, 'result': 'PROFIT', 'risk': 'NORMAL'}
{'symbol': 'GOOG', 'buy_price': 2800.0, 'sell_price': 2780.0, 'quantity': 5, 'pnl': -100.0, 'return_pct': -0.71, 'result': 'LOSS', 'risk': 'NORMAL'}
{'symbol': 'TSLA', 'buy_price': 250.0, 'sell_price': 270.0, 'quantity': 2, 'pnl': 40.0, 'return_pct': 8.0, 'result': 'PROFIT', 'risk': 'NORMAL'}

Total PnL: 40.0
Winning Trades: 2
Losing Trades: 1
Best Trade: AAPL | PnL: 100.0
Worst Trade: GOOG | PnL: -100.0
```

### Run Tests

```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage report (requires pytest-cov)
pytest --cov=src --cov-report=term-missing
```

**Test Output:**
```
tests/test_main.py::test_clean_symbol PASSED
tests/test_main.py::test_calculate_pnl PASSED
tests/test_main.py::test_classify_trade PASSED
tests/test_main.py::test_risk_check PASSED
tests/test_main.py::test_process_single_trade_valid PASSED
tests/test_main.py::test_calculate_total_pnl PASSED

============================== 6 passed ===============================
```

## Technical Implementation

| Component | Description |
|-----------|-------------|
| `clean_symbol()` | Normalizes ticker symbols (uppercase, trimmed) |
| `validate_prices()` | Ensures buy/sell prices are positive numbers |
| `validate_quantity()` | Ensures quantity is a positive integer |
| `calculate_pnl()` | Computes profit/loss: `(sell - buy) × quantity` |
| `calculate_return_percentage()` | Computes return: `((sell - buy) / buy) × 100` |
| `classify_trade()` | Classifies trades as PROFIT, LOSS, or BREAKEVEN |
| `risk_check()` | Flags trades with returns below -5% as HIGH RISK |
| `process_all_trades()` | Batch processes trades with error handling |

## Future Enhancements

- CSV/API data ingestion
- Position tracking and multi-asset support
- Sharpe ratio and drawdown analysis
- Equity curve visualization
- Event-driven backtesting

## License

MIT

## 👤 Author

**Patience Fuglo**  
Quantitative Finance & Machine Learning Enthusiast