# Python Standard Libraries
import sqlite3
# External Libraries
#
# Components
#   Model
from system.components.model.database import get_authors_db
# Get graph db
def get_graph_db():
    authors = get_authors_db()
    nodes = []
    links = []
    IDX = 0
    try:
        conn = sqlite3.connect("./system/db/database.db")
        cursor = conn.cursor()
    except Exception as e:
        print(e)
    authors_check = []
    for author in authors:
        try:
            cursor.execute(f"""
            SELECT id FROM authors
            WHERE name = "{author}"
            """)
            result = cursor.fetchone()
            author_id = result[0]
        except Exception as e:
            print(e)
        try:
            cursor.execute(f"""
            SELECT coauthor_id from author_coauthor
            WHERE author_id = "{author_id}"
            """)
            results = cursor.fetchall()
            coauthors = []
            for coauthor in results:
                coauthors.append(coauthor[0])
        except Exception as e:
            print(e)
        author_id = IDX
        repeated = False
        for author_ in authors_check:
            if author_["name"] == author:
                author_id = author_["idx"]
                repeated = True
                for node in nodes:
                    if node["name"] == author_["name"]:
                        node["group"] = 1
                break
        if not repeated:
            nodes.append({"name": author, "group": 1})
            IDX += 1
            authors_check.append({"name": author, "idx": IDX})
        for coauthor in coauthors:
            try:
                cursor.execute(f"""
                SELECT name from authors
                WHERE id = "{coauthor}"               
                """)
                result = cursor.fetchone()
                coauthor_name = result[0]
            except Exception as e:
                print(e) 
            repeated = False
            for author in authors_check:
                if author["name"] == coauthor_name:
                    coauthor_id = author["idx"]
                    repeated = True
                    break
            if not repeated:
                coauthor_id = IDX
                authors_check.append({"name": coauthor_name, "idx": IDX})
                IDX += 1
                nodes.append({"name": coauthor_name, "group": 2})
            links.append({"source": author_id, "target": coauthor_id})
    return nodes, links
        