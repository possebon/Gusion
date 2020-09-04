# Python Standard Libraries
#
# External Libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# Components
#
# Search Form
search_string_input = dbc.FormGroup(
    [
        dbc.Label("Search author", html_for="search-author-row", width=2),
        dbc.Col(
            dbc.Input(
                type="text", id="search-author", placeholder="Enter author"
            ),
            width=10,
        ),
    ],
    row=True,
)

search_form = dbc.Form([search_string_input], id="search-form")