# Python Standard Libraries
#
# External Libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# Components
from system.components.controller.search import author_options
# Authors Page
authors_page = html.Div([
                    html.Div([
                        html.Div([
                            dcc.Dropdown(
                                id='author-1-dropdown',
                                options=author_options()
                            ),
                            html.Div(id="author-1-content-div"),
                            dbc.Button("Select author", id="author-1-button", color="dark")
                        ], id="author-1-div"),
                        html.Div([
                            dcc.Dropdown(
                                id='author-2-dropdown',
                                options=author_options()
                            ),
                            html.Div(id="author-2-content-div"),
                            dbc.Button("Select author", id="author-2-button", color="dark")
                        ], id="author-2-div"),
                    ], className="row")
], id="authors-page-div")