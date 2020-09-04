# Python Standard Libraries
#
# External Libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# Components
from system.components.controller.search import author_options
print(author_options())
print("here")
# Authors Page
authors_page = html.Div([
                    html.Div([
                        html.Div([
                            html.P("Author 1"),
                            dcc.Dropdown(
                                id='author-1-dropdown',
                                options=author_options()
                            ),
                            dbc.Button("Select", id="author-1-button", color="dark")
                        ], id="author-1-div"),
                        html.Div([
                            html.P("Author 2"),
                            dcc.Dropdown(
                                id='author-2-dropdown',
                                options=author_options()
                            ),
                            dbc.Button("Select", id="author-2-button", color="dark")
                        ], id="author-2-div"),
                    ], className="row")
], id="authors-page-div")