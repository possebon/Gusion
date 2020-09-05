# Python Standard Libraries
#
# External Libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# Components
from system.components.controller.graph import graph
# Home Page
graph_page = html.Div([
                graph()
])