import plotly.graph_objects as go

def plot_terminal_view(df, title="MARKET MONITOR - 05 MAR 2026", save_path="reports/market_monitor.png"):
    """Creates a high-contrast Bloomberg-style chart and saves as PNG."""
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['Asset'], y=df['Change_%'],
        mode='lines+markers',
        line=dict(color='#00E5FF', width=3),
        marker=dict(size=12, color='#FFFFFF')
    ))

    fig.update_layout(
        template="plotly_dark",
        title=f"<b>{title}</b>",
        paper_bgcolor='#000000',
        plot_bgcolor='#1A0033',
        font=dict(color="#00FF00", family="Courier New"),
        yaxis_title="Percent Change (%)",
        width=1000, height=600 # Professional aspect ratio
    )
    
    # Save as Static Image
    fig.write_image(save_path, scale=2) # Scale=2 for High DPI/Retina quality
    print(f">>> Image saved to: {save_path}")
    return fig
