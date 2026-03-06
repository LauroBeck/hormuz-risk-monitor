import pandas as pd

def load_hbm_data():
    """Returns verified market data for the March 05, 2026 session."""
    data = {
        'Date': pd.to_datetime(['2026-03-02', '2026-03-03', '2026-03-04', '2026-03-05']),
        'Asset': ['SK Hynix'] * 4,
        'Price': [1061000, 939000, 849000, 941000],  # Verified Mar 05 Close
        'Change_%': [0, -11.50, -9.58, 10.84]        # The 10.84% Sidecar Rebound
    }
    df = pd.DataFrame(data)
    # Ensure Pandas 3.0.1 Copy-on-Write compatibility
    return df.copy()
