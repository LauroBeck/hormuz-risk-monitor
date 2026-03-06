import pandas as pd
from src.data_loader import load_hbm_data
from src.processing import process_market_data
from src.analytics import calculate_parametric_var

def main():
    print("--- [AUTOMATED RUN: MAR 2026 REGIME] ---")
    try:
        # 1. Ingest
        df = load_hbm_data()
        
        # 2. Process (with the Sidecar-fix we just verified)
        processed = process_market_data(df)
        
        # 3. Analyze
        risk = calculate_parametric_var(processed['Log_Returns'], portfolio_value=1000000)
        
        # 4. Log to Reports
        with open("reports/daily_log.txt", "a") as f:
            f.write(f"Date: {pd.Timestamp.now()}, Price: {processed['Price'].iloc[-1]}, VaR: ${risk:,.2f}\n")
            
        print(f"Success: Market Close Report Generated. Portfolio VaR: ${risk:,.2f}")
    except Exception as e:
        print(f"Pipeline Failure: {e}")

if __name__ == "__main__":
    main()
