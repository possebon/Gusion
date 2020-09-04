# Python Standard Libraries
import sqlite3
# External Libraries
#
# Components
#
# Create Database
def create_db():
    try: 
        conn = sqlite3.connect("database.db")
    except Exception as e:
        print(e)
    
    try:    
        cursor = conn.cursor()
        
        cursor.execute("""
        CREATE TABLE authors (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            affiliation TEXT NOT NULL,
            citedby INTEGER,
            cites_per_year TEXT,
            email TEXT,
            url_picture TEXT,
            interests TEXT
        )          
        """)
        
        cursor.execute("""
        CREATE TABLE author_paper (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            author_id INTEGER NOT NULL,
            paper_id INTEGER NOT NULL
        )
        """)
        
        cursor.execute("""
        CREATE TABLE author_coauthor (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            author_id INTEGER NOT NULL,
            coauthor_id INTEGER NOT NULL
        )
        """)
        
        cursor.execute("""
        CREATE TABLE papers (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            abstract TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            cites INTEGER NOT NULL,
            journal TEXT,
            publisher TEXT,
            url TEXT,
            cites_per_year TEXT
        )
        """)
    except Exception as e:
        print(e)
# Populate author
def populate_author(author):
    # Check values available
    try:
        name = author.name  
    except Exception as e:
        print(e)
        name = "Name not available"
    try:
        affiliation = author.affiliation
    except Exception as e:
        print(e)
        affiliation = "Affiliation not available"
    try:
        citedby = author.citedby
    except Exception as e:
        print(e)
        citedby = "Cites not available"
    try:
        cites_per_year = author.cites_per_year
    except Exception as e:
        print(e)
        cites_per_year = "Cites_per_year not available"
    try:
        email = author.email
    except Exception as e:
        print(e)
        email = "Email not available"
    try:
        coauthors = author.coauthors
    except Exception as e:
        print(e)
        coauthors = "Coauthors not available"
    try:
        url_picture = author.url_picture
    except Exception as e:
        print(e)
        url_picture = "URL picture not available"
    try:
        interests = author.interests
    except Exception as e:
        print(e)
        interests = "Interests not available"
    # Connect to database
    conn = None
    try: 
        conn = sqlite3.connect("database.db")
    except Exception as e:
        print(e)
    # Add author
    if conn:
        try:    
            cursor = conn.cursor()
            cursor.execute(f"""
            INSERT INTO authors (name, affiliation, citedby, cites_per_year, email, url_picture, interests)
            VALUES ("{name}", "{affiliation}", "{citedby}", "{cites_per_year}", "{email}", "{url_picture}", "{interests}")
            """)
            conn.commit()
        except Exception as e:
            print(e)
        # Get ID of author
        try:    
            cursor = conn.cursor()
            cursor.execute(f"""
            SELECT id FROM authors
            WHERE name = "{name}"
            """)
            results = cursor.fetchone()
            author_id = results[0]
        except Exception as e:
            print(e)
    # Add papers
    for publication in author.publications:
        try:
            paper = publication.fill()
        except Exception as e:
            print(e)
            paper = publication
        # Check values available
        try:
            title = paper.bib["title"]  
        except Exception as e:
            print(e)
            title = "Title not available"
        title = title.replace('"', "'")
        try:
            abstract = paper.bib["abstract"]
        except Exception as e:
            print(e)
            abstract = "Abstract not available"
        abstract = abstract.replace('"', "'")
        try:
            paper_author = paper.bib["author"]
        except Exception as e:
            print(e)
            paper_author = "Author not available"
        try:
            year = paper.bib["year"]
        except Exception as e:
            print(e)
            year = "Year not available"
        try:
            cites = paper.bib["cites"]
        except Exception as e:
            print(e)
            cites = "Cites not available"
        try:
            journal = paper.bib["journal"]
        except Exception as e:
            print(e)
            journal = "Journal not available"
        try:
            publisher = paper.bib["publisher"]
        except Exception as e:
            print(e)
            publisher = "Publisher not available"
        try:
            url = paper.bib["url"]
        except Exception as e:
            print(e)
            url = "URL not available"
        try:
            paper_cites_per_year = paper.cites_per_year
        except Exception as e:
            print(e)
            paper_cites_per_year = "Cites per year not available"
        # Add paper
        if conn:
            try:    
                cursor = conn.cursor()
                cursor.execute(f"""
                INSERT INTO papers (title, abstract, author, year, cites, journal, publisher, url, cites_per_year)
                VALUES ("{title}", "{abstract}", "{paper_author}", "{year}", "{cites}", "{journal}", "{publisher}", "{url}", "{paper_cites_per_year}")
                """)
                conn.commit()
            except Exception as e:
                print(e)
            # Get ID of paper
            try:    
                cursor = conn.cursor()
                cursor.execute(f"""
                SELECT id FROM papers
                WHERE title = "{title}"
                """)
                results = cursor.fetchone()
                paper_id = results[0]
                print(paper_id)
            except Exception as e:
                print(e)
            # Add link author-paper
            try: 
                cursor = conn.cursor()
                cursor.execute(f"""
                INSERT INTO author_paper (author_id, paper_id)
                VALUES ("{author_id}", "{paper_id}")
                """)
                conn.commit()
            except Exception as e:
                print(e)   
    # Add coauthors
    if coauthors != "Coauthors not available":
        print(coauthors)
        for coauthor in coauthors:
            # Check values available
            try:
                coauthor_name = coauthor.name  
            except Exception as e:
                print(e)
                coauthor_name = "Name not available"
            try:
                coauthor_affiliation = coauthor.affiliation
            except Exception as e:
                print(e)
                coauthor_affiliation = "Affiliation not available"
            # Add coauthor
            if conn:
                try:    
                    cursor = conn.cursor()
                    cursor.execute(f"""
                    INSERT INTO authors (name, affiliation)
                    VALUES ("{coauthor_name}", "{coauthor_affiliation}")
                    """)
                    conn.commit()
                except Exception as e:
                    print(e)
                # Get ID of coauthor
                try:    
                    cursor = conn.cursor()
                    cursor.execute(f"""
                    SELECT id FROM authors
                    WHERE name = "{coauthor_name}"
                    """)
                    results = cursor.fetchone()
                    coauthor_id = results[0]
                except Exception as e:
                    print(e)
                # Add link author-coauthor
                try:    
                    cursor = conn.cursor()
                    cursor.execute(f"""
                    INSERT INTO author_coauthor (author_id, coauthor_id)
                    VALUES ("{author_id}", "{coauthor_id}")
                    """)
                    conn.commit()
                except Exception as e:
                    print(e)  
# Get authors
def get_authors_db():
    try:
        conn = sqlite3.connect("./system/db/database.db")
    except Exception as e:
        print(e)
    authors = []
    try:
        cursor = conn.cursor()
        cursor.execute("""
        SELECT name, citedby from authors 
        WHERE citedby > -1               
        """)
        results = cursor.fetchall()
        # Turn results into list
        for result in results:
            authors.append(result[0])
    except Exception as e:
        print(e)
    return authors
        