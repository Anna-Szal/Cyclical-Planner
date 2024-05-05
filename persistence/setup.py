import sqlite3 as sl



def create_tables(path):
    con = sl.connect(path)
    with con:
        con.execute("""
            CREATE TABLE done_task (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                task TEXT
            );
        """)
        con.execute("""
                CREATE TABLE done_date (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    year INTEGER,
                    month INTEGER,
                    day INTEGER
                );
            """)
        con.execute("""
                CREATE TABLE done_task_date (
                    task_id INTEGER,
                    date_id INTEGER,
                    FOREIGN KEY(task_id) REFERENCES task(id),
                    FOREIGN KEY(date_id) REFERENCES date(id)
                );
            """)

        con.execute("""
            CREATE TABLE cycle (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                task TEXT,
                period INTEGER,
                start_year INTEGER,
                start_month INTEGER,
                start_day INTEGER
            );
        """)    
