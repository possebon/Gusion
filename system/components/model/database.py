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
            interests TEXT,
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
        CREATE TABLE paper (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            abstract TEXT NOT NULL,
            authors TEXT NOT NULL,
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
        
        
  