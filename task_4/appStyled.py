import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

def make_figure(selected_region):
    if selected_region == "all":
        filtered_df = df.copy()
        chart_title = "Pink Morsel Sales Over Time - All Regions"
    else:
        filtered_df = df[df["region"] == selected_region].copy()
        chart_title = f"Pink Morsel Sales Over Time - {selected_region.title()}"

    daily_sales = (
        filtered_df.groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title=chart_title
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        template="plotly_white",
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        font=dict(color="#1f2937"),
        margin=dict(l=40, r=40, t=70, b=40)
    )

    fig.update_traces(line=dict(width=3))

    return fig

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f7fb",
        "minHeight": "100vh",
        "padding": "30px",
        "fontFamily": "Arial, sans-serif"
    },
    children=[
        html.Div(
            style={
                "maxWidth": "1200px",
                "margin": "0 auto",
                "backgroundColor": "white",
                "padding": "30px",
                "borderRadius": "18px",
                "boxShadow": "0 8px 20px rgba(0, 0, 0, 0.08)"
            },
            children=[
                html.H1(
                    "Pink Morsel Sales Visualiser",
                    style={
                        "textAlign": "center",
                        "color": "#e91e63",
                        "marginBottom": "10px"
                    }
                ),

                html.P(
                    "Use the region filter below to explore Pink Morsel sales over time.",
                    style={
                        "textAlign": "center",
                        "color": "#4b5563",
                        "marginBottom": "25px",
                        "fontSize": "18px"
                    }
                ),

                html.Div(
                    style={
                        "marginBottom": "25px",
                        "padding": "15px",
                        "backgroundColor": "#fce4ec",
                        "borderRadius": "12px"
                    },
                    children=[
                        html.Label(
                            "Filter by region:",
                            style={
                                "fontWeight": "bold",
                                "fontSize": "18px",
                                "color": "#1f2937",
                                "display": "block",
                                "marginBottom": "10px"
                            }
                        ),

                        dcc.RadioItems(
                            id="region-filter",
                            options=[
                                {"label": "North", "value": "north"},
                                {"label": "East", "value": "east"},
                                {"label": "South", "value": "south"},
                                {"label": "West", "value": "west"},
                                {"label": "All", "value": "all"}
                            ],
                            value="all",
                            inline=True,
                            labelStyle={
                                "marginRight": "18px",
                                "fontSize": "16px",
                                "color": "#374151"
                            },
                            inputStyle={
                                "marginRight": "6px"
                            }
                        )
                    ]
                ),

                dcc.Graph(
                    id="sales-chart",
                    figure=make_figure("all")
                )
            ]
        )
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):
    return make_figure(selected_region)

if __name__ == "__main__":
    app.run(debug=True)
