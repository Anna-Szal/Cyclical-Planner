import sqlite3 as sl

from logic.db_interfaces import DbDoneInterface
from logic.date import Date


class DbDone(DbDoneInterface):
    def __init__(self, db_path):
        self.db_path = db_path


    def get_tasks(self, date):
        con = sl.connect(self.db_path)
        tasks = []
        with con:
            cursor = con.cursor()
            cursor.execute('SELECT id FROM done_date WHERE year=(?) AND month=(?) AND day=(?)', date)
            date_id = cursor.fetchone()

            if date_id:         
                cursor.execute('SELECT task_id FROM done_task_date WHERE date_id=(?)', date_id)
                task_ids = cursor.fetchall()

                for id in task_ids:
                    cursor.execute('SELECT task FROM done_task WHERE id=(?)', id)
                    task = cursor.fetchone()
                    tasks.append(task[0])

        return tasks


    def get_tasks_start_with(self, string):
        con = sl.connect(self.db_path)
        with con:
            cursor = con.cursor()
            cursor.execute('SELECT * FROM done_task WHERE task LIKE (?)', (string+'%',))
            tasks = cursor.fetchall()
            tasks = [t[1] for t in tasks]
        return tasks


    def get_dates(self, task):
        con = sl.connect(self.db_path)
        dates = []
        with con:
            cursor = con.cursor()
            cursor.execute('SELECT id FROM done_task WHERE task=(?)', (task,))
            task_id = cursor.fetchone()

            if task_id:         
                cursor.execute(
                    'SELECT date_id FROM done_task_date WHERE task_id=(?)', 
                    task_id
                    )
                date_ids = cursor.fetchall()

                for id in date_ids:
                    cursor.execute(
                        'SELECT year, month, day FROM done_date WHERE id=(?)', 
                        id
                        )
                    date = cursor.fetchone()
                    dates.append(Date(*date))

        return dates       


    def insert_task(self, task, date):
        con = sl.connect(self.db_path)
        cursor = con.cursor()
        with con:
            cursor.execute('SELECT * FROM done_task WHERE task=(?)', (task,))
            task_db = cursor.fetchone()
            if task_db:
                task_id = task_db[0]
            else:
                cursor.execute('INSERT INTO done_task (task) VALUES(?)', (task,))
                task_id = cursor.lastrowid

            cursor.execute(
                'SELECT * FROM done_date WHERE year=(?) AND month=(?) AND day=(?)', 
                date
                )
            date_db = cursor.fetchone()
            if date_db:
                date_id = date_db[0]
            else:
                cursor.execute(
                    'INSERT INTO done_date (year, month, day) VALUES(?, ?, ?)', 
                    date
                    )
                date_id = cursor.lastrowid
            
            cursor.execute(
                'SELECT * FROM done_task_date WHERE task_id=(?) AND date_id=(?)', 
                (task_id, date_id)
                )
            pair = cursor.fetchone()
            if not pair:
                cursor.execute(
                    'INSERT INTO done_task_date VALUES(?, ?)', 
                    (task_id, date_id)
                    )

            con.commit()


    def update_task(self, old_task_name, new_task_name):
        con = sl.connect(self.db_path)
        with con:
            cursor = con.cursor()
            cursor.execute(
                'UPDATE done_task SET task=(?) WHERE task=(?)', 
                (new_task_name, old_task_name)
                )
            con.commit()


    def remove_task(self, task, date):
        con = sl.connect(self.db_path)
        with con:
            cursor = con.cursor()
            cursor.execute('SELECT id FROM done_task WHERE task=(?)', (task,))
            task_id = cursor.fetchone()
            cursor.execute('SELECT id FROM done_date WHERE year=(?) AND month=(?) AND day=(?)', date)
            date_id = cursor.fetchone()

            cursor.execute('DELETE FROM done_task_date WHERE task_id=(?) AND date_id=(?)', (task_id[0], date_id[0]))
            con.commit()
            
    
    def remove_task_history(self, task):
        con = sl.connect(self.db_path)
        with con:
            cursor = con.cursor()
            cursor.execute('SELECT id FROM done_task WHERE task=(?)', (task,))
            task_id = cursor.fetchone()
            cursor.execute('DELETE FROM done_task_date WHERE task_id=(?)', task_id)
            cursor.execute('DELETE FROM done_task WHERE task=(?)', (task,))


    # DEBUGGING
    def print_all_tasks(self):
        con = sl.connect(self.db_path)
        with con:
            cursor = con.cursor()
            data = cursor.execute('SELECT * FROM done_task_date')
            id_list = [(x[0], x[1]) for x in data]

            for row in id_list:
                cursor.execute('SELECT * FROM done_task where id=(?)', (row[0],))
                task = cursor.fetchone()

                cursor.execute('SELECT * FROM done_date where id=(?)', (row[1],))
                date = cursor.fetchone()
                print(f'{task} --- {date}')
