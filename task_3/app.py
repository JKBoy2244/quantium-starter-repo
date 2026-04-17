import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the processed data from Task 2
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Sum sales by date so the line chart clearly answers the business question
daily_sales = (
    df.groupby("date", as_index=False)["sales"]
    .sum()
    .sort_values("date")
)

# Build the line chart
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales",
    template="plotly_white"
)

# Add a marker for the price increase date
fig.add_vline(
    x=pd.Timestamp("2021-01-15"),
    line_dash="dash",
    line_color="red",
    annotation_text="Price increase: 2021-01-15",
    annotation_position="top left"
)

# Create the Dash app
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Pink Morsel Sales Visualiser"),
        dcc.Graph(figure=fig),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
