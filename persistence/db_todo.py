import sqlite3 as sl
from typing import List, Optional

from logic.date import Date
from logic.cycle import Cycle
from logic.db_interfaces import DbTodoInterface



class DbTodo(DbTodoInterface):
    def __init__(self, db_path: str):
        self.db_path = db_path


    def get_all_cycles(self) -> List[Cycle]:
        cycles = []

        con = sl.connect(self.db_path)
        with con:
            cursor = con.cursor()
            data = cursor.execute('SELECT * FROM cycle')
            for row in data:
                cycles.append(Cycle(row[1], row[2], Date(row[3], row[4], row[5])))
        
        return cycles


    # CRUD
    def create_cycle(self, cycle: Cycle) -> None:
        con = sl.connect(self.db_path)
        cursor = con.cursor()
        with con:
            cursor.execute(
                '''
                INSERT INTO cycle (
                    task, 
                    period, 
                    start_year, 
                    start_month, 
                    start_day
                    ) 
                VALUES(?,?,?,?,?)
                ''', 
                (
                    cycle.task, 
                    cycle.period, 
                    cycle.next_date.year, 
                    cycle.next_date.month, 
                    cycle.next_date.day
                )
            )
            con.commit()
            

    def get_cycle(self, task: str) -> Optional[Cycle]:
        con = sl.connect(self.db_path)
        cursor = con.cursor()
        with con:
            cursor.execute('SELECT * FROM cycle WHERE task=(?)', (task, ))
            row = cursor.fetchone()
            if row:
                cycle = Cycle(row[1], row[2], Date(row[3], row[4], row[5]))
                return cycle
            else:
                return None


    def update_cycle(self, old_task_name: str, new_cycle: Cycle) -> None:
        con = sl.connect(self.db_path)
        with con:
            cursor = con.cursor()
            cursor.execute(
                '''
                UPDATE cycle
                SET
                    task = (?), 
                    period = (?),
                    start_year = (?),
                    start_month = (?),
                    start_day = (?)
                WHERE task = (?)
                ''',
                (
                    new_cycle.task,
                    new_cycle.period,
                    new_cycle.next_date.year, 
                    new_cycle.next_date.month, 
                    new_cycle.next_date.day,
                    old_task_name
                )
            )
            con.commit()


    def remove_cycle(self, task: str) -> None:
        con = sl.connect(self.db_path)
        with con:
            cursor = con.cursor()
            cursor.execute('DELETE FROM cycle WHERE task = (?)', (task,))
            con.commit()


    # DEBUGGING
    def print_all_tasks(self):
        con = sl.connect(self.db_path)
        with con:
            cursor = con.cursor()
            data = cursor.execute('SELECT * FROM cycle')
            for row in data:
                print(row)
