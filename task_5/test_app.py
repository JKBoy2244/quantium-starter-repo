from task_4.appStyled import app


def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel Sales Visualiser"


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    picker = dash_duo.find_element("#region-filter")
    assert picker is not None

    picker_text = picker.text
    assert "North" in picker_text
    assert "East" in picker_text
    assert "South" in picker_text
    assert "West" in picker_text
    assert "All" in picker_text
