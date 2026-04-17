from dash import dcc, html
from task_4.appStyled import app


def walk_components(component):
    if component is None:
        return

    yield component

    children = getattr(component, "children", None)

    if isinstance(children, (list, tuple)):
        for child in children:
            yield from walk_components(child)
    elif children is not None:
        yield from walk_components(children)


def test_header_present():
    headers = [
        component
        for component in walk_components(app.layout)
        if isinstance(component, html.H1)
    ]

    assert headers
    assert headers[0].children == "Pink Morsel Sales Visualiser"


def test_visualisation_present():
    graphs = [
        component
        for component in walk_components(app.layout)
        if isinstance(component, dcc.Graph)
    ]

    assert graphs
    assert graphs[0].id == "sales-chart"


def test_region_picker_present():
    radio_items = [
        component
        for component in walk_components(app.layout)
        if isinstance(component, dcc.RadioItems)
    ]

    assert radio_items
    assert radio_items[0].id == "region-filter"

    option_values = {option["value"] for option in radio_items[0].options}
    assert option_values == {"north", "east", "south", "west", "all"}
