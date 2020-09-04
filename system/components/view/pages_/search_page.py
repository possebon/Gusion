# Python Standard Libraries
#
# External Libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# Components
#   Fragments
from system.components.view.fragments.search_form import search_form
from system.components.view.fragments.search_menu import search_menu
# Search Page
search_page = html.Div([
                html.Div(id="callback-search-div"),
                search_form,
                search_menu
])