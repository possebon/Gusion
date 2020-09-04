# Python Standard Libraries
#
# External Libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# Components
#
# Authors Page
authors_page = html.Div([
                    html.Div([
                        html.Div([
                            html.P("Author 1")
                        ], id="author-1-div"),
                        html.Div([
                            html.P("Author 2")
                        ], id="author-2-div"),
                    ], className="row")
], id="authors-page-div")