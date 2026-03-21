from src.main import (
    clean_symbol,
    calculate_pnl,
    classify_trade,
    risk_check,
    process_single_trade,
    calculate_total_pnl,
)


def test_clean_symbol():
    assert clean_symbol(" aapl ") == "AAPL"


def test_calculate_pnl():
    assert calculate_pnl(100, 110, 5) == 50


def test_classify_trade():
    assert classify_trade(10) == "PROFIT"
    assert classify_trade(-10) == "LOSS"
    assert classify_trade(0) == "BREAKEVEN"


def test_risk_check():
    assert risk_check(-10) == "HIGH RISK"
    assert risk_check(2) == "NORMAL"


def test_process_single_trade_valid():
    trade = process_single_trade(["Aapl", 150, 160, 10])
    assert trade is not None
    assert trade["symbol"] == "AAPL"
    assert trade["result"] == "PROFIT"


def test_calculate_total_pnl():
    trade_log = [
        {"pnl": 100},
        {"pnl": -50},
        {"pnl": 40},
    ]
    assert calculate_total_pnl(trade_log) == 90
