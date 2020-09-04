# Python Standard Libraries
#
# External Libraries
from scholarly import scholarly
# Components
#   Model
from system.components.model.database import populate_author, create_db, get_authors_db
# Path
from system.tor_path import tor_path
# Select author
def select_author(name):
    pass
# Get author
def get_author(name):
    if name != None:
        # Setup tor browser
        def setup_tor():
            try: 
                scholarly.launch_tor(tor_path)
            except Exception as e:
                print(e)
        setup_tor()
        # Search author by name
        def search_author(name):
            while True:
                search_query = scholarly.search_author(name)
                author = next(search_query).fill() 
                if author:
                    break
            return author
        # Get and populate author
        author = search_author(name) 
        create_db()
        populate_author(author)
    
def author_options():
    authors = get_authors_db()
    author_options = []
    for author in authors:
        option = {"label" : author, "value" : author}
        author_options.append(option)
    return author_options
