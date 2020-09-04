# Python Standard Libraries
#
# External Libraries
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# Components
#
# Search menu items
search_menu_items = dbc.Row(
    [
        dbc.Col(
            dbc.NavLink(dbc.Button("Go back", id="return-home-button", n_clicks=0),
            href="/home",
            id="home-link"
            ),
            id="return-home-col", 
            width="auto"
        ),
        dbc.Col(
            dbc.Button("Search", id="search-button", n_clicks=0),
            id="search-col", 
            width="auto"
        ),
    ],
    no_gutters=True,
    className="flex-nowrap mt-3 mt-md-3",
    align="center",
)
# Search menu
search_menu = dbc.Navbar(
    [
        search_menu_items,
        dbc.NavbarToggler(id="navbar-toggler")
    ],
    color="dark",
    dark=True,
    #change to css
    style={"position": "absolute", "bottom": 0, "left":0, "width": "100%"},
    id="review-menu")