import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the processed data from Task 2
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])

# Group by date and sum sales
daily_sales = (
    df.groupby("date", as_index=False)["sales"]
    .sum()
    .sort_values("date")
)

# Create the line chart
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

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
