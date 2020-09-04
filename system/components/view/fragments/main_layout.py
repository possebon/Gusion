# Python Standard Libraries
#
# External Libraries
import dash_core_components as dcc
import dash_html_components as html
# Components
#   Fragments
from system.components.view.fragments.main_menu import main_menu

# Main Layout
main_layout = html.Div([
    html.Div([
    main_menu
    ],id="menu-div", style={"padding-bottom": "6vh"}),
    html.Div(id="page-content-div"),
], id="root-div", style={"height": "100vh"})