from scipy.stats import norm

def calculate_parametric_var(returns, confidence_level=0.95, portfolio_value=1000000):
    """
    Calculates the Dollar Value at Risk (VaR).
    Essential for March 2026 volatility regimes.
    """
    if returns.empty:
        return 0.0
    
    mu = returns.mean()
    sigma = returns.std()
    
    # norm.ppf gets the Z-score for the 5th percentile
    z_score = norm.ppf(1 - confidence_level)
    
    # VaR = Portfolio Value * (Mean + Z * StdDev)
    var_pct = mu + z_score * sigma
    return abs(var_pct * portfolio_value)

def calculate_sharpe_ratio(returns, risk_free_rate=0.045):
    """
    Standardized risk-adjusted return. 
    (Mar 2026 Risk-Free Rate estimated at 4.5%)
    """
    if returns.std() == 0:
        return 0.0
    return (returns.mean() - risk_free_rate/252) / returns.std()
