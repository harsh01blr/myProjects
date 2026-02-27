import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load dataset
df = pd.read_csv("sample_data.csv")

# Sorting for each chart
df_units = df.sort_values("Units_Sold", ascending=False)
df_revenue = df.sort_values("Revenue", ascending=False)
df_inventory = df.sort_values("Inventory", ascending=False)

# Low-stock color logic
low_stock_threshold = 20
colors_inventory = [
    "red" if inv < low_stock_threshold else "#1f77b4"
    for inv in df_inventory["Inventory"]
]

# Create vertical dashboard layout
fig = make_subplots(
    rows=3, cols=1,
    subplot_titles=[
        "Top-Selling Medicines (Units Sold)",
        "Revenue by Medicine",
        "Inventory Levels with Low-Stock Highlight"
    ]
)

# Chart 1: Units Sold
fig.add_trace(
    go.Bar(
        x=df_units["Medicine"],
        y=df_units["Units_Sold"],
        marker_color="#1f77b4"
    ),
    row=1, col=1
)

# Chart 2: Revenue
fig.add_trace(
    go.Bar(
        x=df_revenue["Medicine"],
        y=df_revenue["Revenue"],
        marker_color="#1f77b4"
    ),
    row=2, col=1
)

# Chart 3: Inventory with red highlights
fig.add_trace(
    go.Bar(
        x=df_inventory["Medicine"],
        y=df_inventory["Inventory"],
        marker_color=colors_inventory
    ),
    row=3, col=1
)

# Apply 45° tilt to all x-axes
fig.update_xaxes(tickangle=-45)

# Main dashboard title
fig.update_layout(
    title_text="Pharmacy Sales & Inventory Dashboard (Prototype)",
    height=1200,
    showlegend=False
)

# Export to GitHub Pages
fig.write_html("docs/index.html", include_plotlyjs='cdn')