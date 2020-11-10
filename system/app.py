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
from system.components.controller.author import get_plot_author
from system.components.controller.group import get_plot_group
#   Fragments
from system.components.view.fragments.main_layout import main_layout
#   Pages
from system.components.view.pages import pages
# Stylesheet
external_stylesheets = [dbc.themes.LUX]
# App
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
server = app.server
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
    elif pathname in ["/groups"]:
        return pages["groups"]
    elif pathname in ["/graph"]:
        return pages["graph"]
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
    get_author(name)
    return None
#   Select author 1
@app.callback(
    Output("author-1-content-div", "children"),
    [Input("author-1-button", "n_clicks")],
    [State("author-1-dropdown", "value")]
)
def plot_author_1(click, name):
    if click:
        plot = get_plot_author(name)
        return plot 
    else:
        return None
#   Select author 2
@app.callback(
    Output("author-2-content-div", "children"),
    [Input("author-2-button", "n_clicks")],
    [State("author-2-dropdown", "value")]
)
def plot_author_2(click, name):
    if click:
        plot = get_plot_author(name)
        return plot 
    else:
        return None
#   Select group 1
@app.callback(
    Output("group-1-content-div", "children"),
    [Input("group-1-button", "n_clicks")],
    [State("group-1-dropdown", "value")]
)
def plot_group_1(click, names):
    if click:
        plot = get_plot_group(names)
        return plot 
    else:
        return None
#   Select group 2
@app.callback(
    Output("group-2-content-div", "children"),
    [Input("group-2-button", "n_clicks")],
    [State("group-2-dropdown", "value")]
)
def plot_group_2(click, names):
    if click:
        plot = get_plot_group(names)
        return plot 
    else:
        return None

