"""
Task 3: Create a Dash Application

Visualises the formatted Pink Morsel sales data as a line chart
so we can answer: "Were sales higher before or after the Pink
Morsel price increase on 15 Jan 2021?"
"""

import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load the formatted data produced in Task 2
data = pd.read_csv("data/formatted_sales_data.csv")
data["Date"] = pd.to_datetime(data["Date"])
data = data.sort_values("Date")

# Build the line chart: total sales over time
fig = px.line(
    data,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Date": "Date", "Sales": "Sales ($)"},
)

# Mark the price increase date for context
fig.add_vline(x="2021-01-15", line_dash="dash", line_color="red")

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Pink Morsel Sales Visualiser"),
        dcc.Graph(id="sales-line-chart", figure=fig),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)