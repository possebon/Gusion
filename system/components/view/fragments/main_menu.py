# Python Standard Libraries
#
# External Libraries
import dash_bootstrap_components as dbc
import dash_html_components as html
# Components
#
# Menu items
menu_items = dbc.Row(
    [
        dbc.Col(
            dbc.NavLink(dbc.Button("Home", id="home-button", n_clicks=0),
            href="/home",
            id="home-link"
            ),
            id="home-col", 
            width="auto"
        ),
        dbc.Col(
            dbc.NavLink(dbc.Button("Authors", id="authors-button", n_clicks=0),
            href="/authors",
            id="authors-link"
            ),
            id="authors-col", 
            width="auto"
        )
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3",
    align="center",
)
# Main menu
main_menu = dbc.Navbar(
    [   
        html.A(
            dbc.Row(
                [   
                    dbc.Col(html.Img(src="assets/logo.png", height="67vh")),
                    dbc.Col(dbc.NavbarBrand("Gusion", className="ml-2")),
                ],
                align="center",
                no_gutters=True,
                ),
            href="/",
            id="logo"
        ),
        menu_items,
        dbc.NavbarToggler(id="navbar-toggler")
    ],
    color="dark",
    dark=True,
    style={"position": "absolute", "top": 0, "left":0, "width": "100%"},
    id="menu")