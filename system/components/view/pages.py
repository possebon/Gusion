# Python Standard Libraries
#
# External Libraries
#
# Components
#   Pages
from system.components.view.pages_.home_page import home_page
from system.components.view.pages_.authors_page import authors_page
from system.components.view.pages_.groups_page import groups_page
from system.components.view.pages_.search_page import search_page
from system.components.view.pages_.graph_page import graph_page
# Pages dictionary
pages = {"home" : home_page,
         "authors" : authors_page,
         "groups": groups_page,
         "graph" : graph_page,
         "search" : search_page}