import pandas as pd
from src.processing import process_market_data

def test_sidecar_logic():
    # Mock a 15% price spike (Today's Rebound scenario)
    data = {'Price': [100, 115], 'Asset': ['SK Hynix', 'SK Hynix']}
    df = pd.DataFrame(data)
    processed = process_market_data(df)
    assert processed['Sidecar_Triggered'].iloc[-1] == True
    print("SUCCESS: Sidecar trigger verified for >10% moves.")

if __name__ == "__main__":
    test_sidecar_logic()
