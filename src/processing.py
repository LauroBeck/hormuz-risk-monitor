import pandas as pd
import numpy as np

def process_market_data(df):
    """
    Processes market data with Pandas 3.0 CoW compatibility.
    Handles Sidecar detection for the Mar 05, 2026 volatility regime.
    """
    df = df.copy()
    
    # Defensive Check: Ensure Change_% exists or calculate it
    if 'Change_%' not in df.columns:
        df['Change_%'] = df['Price'].pct_change() * 100
        df['Change_%'] = df['Change_%'].fillna(0)
    
    # Calculate Log Returns for Risk Analytics
    df['Log_Returns'] = np.log(df['Price'] / df['Price'].shift(1)).fillna(0)
    
    # Sidecar Trigger: KRX Rule (Move > 10% for 1 minute)
    # We flag any day with a >10% move as a Sidecar event
    df['Sidecar_Triggered'] = df['Change_%'].abs() >= 10.0
    
    return df
