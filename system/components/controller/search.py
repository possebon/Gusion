# Python Standard Libraries
#
# External Libraries
from scholarly import scholarly
# Components
#   Controller
from system.components.controller.proxy import make_collector, setup_new_proxies
#   Model
from system.components.model.database import populate_author, create_db
# Path
from system.tor_path import tor_path
# Select author
def select_author(name):
    pass
# Get author
def get_author(name):
    # Setup working proxy
    def setup_proxy():
        http_collector = make_collector()
        while True:
            http = setup_new_proxies(http_collector)
            print("Trying proxy:", http["http"], http["https"])
            proxy_works = scholarly.use_proxy(http=http["http"], https=http["https"])
            if proxy_works:
                break
        print("Working proxy:", http["http"], http["https"])
        return True
    # Setup tor browser
    def setup_tor():
        working_proxy = setup_proxy()
        if working_proxy:
            try: 
                scholarly.launch_tor(tor_path)
            except Exception as e:
                print(e)
    setup_tor()
    # Search author by name
    def search_author(name):
        while True:
            search_query = scholarly.search_author('Steven A Cholewiak')
            author = next(search_query).fill() 
            if author:
                break
        return author
    # Get and populate author
    author = search_author(name) 
    create_db()
    populate_author(author)
    


