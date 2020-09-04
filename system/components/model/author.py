# Python Standard Libraries
import sqlite3
# External Libraries
#
# Components
#
# Get author data
def get_author_data_db(name):
    try:
        conn = sqlite3.connect("./system/db/database.db")
    except Exception as e:
        print(e)
    result = []
    try:
        cursor = conn.cursor()
        cursor.execute(f"""
        SELECT * FROM authors
        WHERE name = "{name}"               
        """)
        result = cursor.fetchone()
        print(result)
    except Exception as e:
        print(e)
    return result

def get_papers_by_author_db(idx):
    try:
        conn = sqlite3.connect("./system/db/database.db")
    except Exception as e:
        print(e)
    result = []
    # Get paper id
    try:
        cursor = conn.cursor()
        cursor.execute(f"""
        SELECT * FROM author_paper
        WHERE author_id = "{idx}"               
        """)
        results = cursor.fetchall()
    except Exception as e:
        print(e)
    # Get papers
    papers = []
    for result in results:
        idz = result[2] 
        try:
            cursor = conn.cursor()
            cursor.execute(f"""
            SELECT * FROM papers
            WHERE id = "{idz}"
            """)
            paper = cursor.fetchone()
            papers.append(paper)
        except Exception as e:
            print(e)      
    return papers