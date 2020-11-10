# Python Standard Libraries
#
# External Libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# Components
from system.components.controller.search import author_options
# Groups Page
groups_page = html.Div([
                    html.Div([
                        html.Div([
                            dcc.Dropdown(
                                id='group-1-dropdown',
                                options=author_options(),
                                multi=True
                            ),
                            html.Div(id="group-1-content-div"),
                            dbc.Button("Select Group", id="group-1-button", color="dark")
                        ], id="group-1-div"),
                        html.Div([
                            dcc.Dropdown(
                                id='group-2-dropdown',
                                options=author_options(),
                                multi=True
                            ),
                            html.Div(id="group-2-content-div"),
                            dbc.Button("Select Group", id="group-2-button", color="dark")
                        ], id="group-2-div"),
                    ], className="row")
], id="groups-page-div")