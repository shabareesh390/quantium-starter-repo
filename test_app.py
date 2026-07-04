"""
Task 5: Test Your Dash Application

Verifies that the header, the line chart, and the region radio
picker are all present in the rendered app.
"""

from app import app


def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "🍬 Pink Morsel Sales Visualiser"


def test_visualisation_is_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None


def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    radio_items = dash_duo.find_element("#region-filter")
    assert radio_items is not None