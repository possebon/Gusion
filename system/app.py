# Python Standard Libraries
#
# External Libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
# Components
#   Controller
from system.components.controller.search import get_author
#   Fragments
from system.components.view.fragments.main_layout import main_layout
#   Pages
from system.components.view.pages import pages
# Stylesheet
external_stylesheets = [dbc.themes.LUX]
# App
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
# Main Layout
layout = main_layout
app.layout = html.Div([dcc.Location(id="url"), layout], id="layout-div")
# Callbacks
#   Redirect pages
@app.callback(
    Output("page-content-div", "children"), 
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname in ["/", "/home"]:
        return pages["home"]
    elif pathname in ["/authors"]:
        return pages["authors"]
    elif pathname in ["/search"]:
        return pages["search"]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
#   Search author
@app.callback(
    Output("callback-search-div", "children"), 
    [Input("search-button", "n_clicks")],
    [State("search-author", "value")]
)
def search_author(click, name):
    print("get author")
    get_author(name)
    return None


