import pytest
from src.analytics import calculate_hormuz_premium

def test_hormuz_premium_calculation():
    # Scenario: Mar 5, 2026 Spot vs GS Forecast
    spot = 85.41
    gs_fair_value = 71.00 # GS base case without conflict
    
    premium = calculate_hormuz_premium(spot, gs_fair_value)
    
    # Assert the premium is exactly 14.41
    assert round(premium, 2) == 14.41

def test_negative_premium():
    # Math should hold even if market is in contango/oversupply
    assert calculate_hormuz_premium(60.00, 70.00) == -10.00
