"""
Task 4: Improve Your Dash Application

Adds a region-filtering radio button and CSS styling to the
Pink Morsel sales visualiser.
"""

import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Load the formatted data produced in Task 2
data = pd.read_csv("data/formatted_sales_data.csv")
data["Date"] = pd.to_datetime(data["Date"])
data = data.sort_values("Date")

app = Dash(__name__)

# Colours used throughout the app
COLORS = {
    "background": "#fdf6f0",
    "header": "#d6336c",
    "accent": "#ff8fab",
    "text": "#3a3a3a",
}


def build_figure(region: str):
    """Build the line chart for the selected region."""
    if region == "all":
        filtered = data.groupby("Date", as_index=False)["Sales"].sum()
    else:
        filtered = data[data["Region"] == region]

    fig = px.line(
        filtered,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time ({region.title()})",
        labels={"Date": "Date", "Sales": "Sales ($)"},
    )
    fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")
    fig.update_layout(
        plot_bgcolor=COLORS["background"],
        paper_bgcolor=COLORS["background"],
        font_color=COLORS["text"],
    )
    fig.update_traces(line_color=COLORS["header"])
    return fig


app.layout = html.Div(
    style={
        "backgroundColor": COLORS["background"],
        "fontFamily": "Helvetica, Arial, sans-serif",
        "padding": "40px",
        "minHeight": "100vh",
    },
    children=[
        html.H1(
            children="🍬 Pink Morsel Sales Visualiser",
            style={
                "textAlign": "center",
                "color": COLORS["header"],
                "marginBottom": "10px",
            },
        ),
        html.P(
            "Explore how the 15 Jan 2021 price increase affected Pink Morsel sales, "
            "filtered by region.",
            style={
                "textAlign": "center",
                "color": COLORS["text"],
                "marginBottom": "30px",
            },
        ),
        html.Div(
            style={"textAlign": "center", "marginBottom": "20px"},
            children=[
                dcc.RadioItems(
                    id="region-filter",
                    options=[
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                        {"label": "All", "value": "all"},
                    ],
                    value="all",
                    inline=True,
                    labelStyle={
                        "marginRight": "20px",
                        "fontSize": "18px",
                        "color": COLORS["text"],
                    },
                    inputStyle={"marginRight": "6px"},
                )
            ],
        ),
        html.Div(
            style={
                "backgroundColor": "white",
                "borderRadius": "12px",
                "padding": "20px",
                "boxShadow": "0 4px 12px rgba(0,0,0,0.1)",
                "maxWidth": "1000px",
                "margin": "0 auto",
            },
            children=[dcc.Graph(id="sales-line-chart", figure=build_figure("all"))],
        ),
    ],
)


@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-filter", "value"),
)
def update_chart(selected_region):
    return build_figure(selected_region)


if __name__ == "__main__":
    app.run(debug=True)