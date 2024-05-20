import time
from typing import List

from logic.db_interfaces import DbTodoInterface, DbDoneInterface
from logic.date import Date
from logic.cycle import Cycle



class DbLogic:
    def __init__(self, todo_db: DbTodoInterface, done_db: DbDoneInterface):
        self.todo_db = todo_db
        self.done_db = done_db

        today = time.localtime()
        self.today = Date(today[0], today[1], today[2])
        

    # TO DO part
    def create_cycle(self, cycle: Cycle) -> None:
        self.todo_db.create_cycle(cycle)

    def get_cycle(self, task: str) -> Cycle:
        return self.todo_db.get_cycle(task)
    
    def get_all_cycles(self) -> List[Cycle]:
        return self.todo_db.get_all_cycles()

    def update_cycle(self, task: str, new_cycle: Cycle) -> None:
        self.todo_db.update_cycle(task, new_cycle)

    def remove_cycle(self, task: str) -> None:
        self.todo_db.remove_cycle(task)
    

    def shift_dates_on_startup(self):
        cycles = self.todo_db.get_all_cycles()
        for cycle in cycles:
            delta = cycle.next_date.delta_with(self.today)
            if delta < 0:
                cycle.next_date = self.today
                self.todo_db.update_cycle(cycle.task, cycle)


    def get_todo_tasks(self, date: Date) -> List[str]:
        tasks = []
        cycles = self.todo_db.get_all_cycles()

        for cycle in cycles:
            delta = date.delta_with(cycle.next_date)
            if delta >=0 and delta % cycle.period == 0:
                tasks.append(cycle.task)

        return tasks



    # DONE part
    def get_done_tasks(self, date: Date):
        return self.done_db.get_tasks(date)

    def get_done_dates(self, task: str) -> List[Date]:
        return self.done_db.get_dates(task)
    
    def get_tasks_start_with(self, string: str) -> List[str]:
        return self.done_db.get_tasks_start_with(string)

    def update_task(self, old_task_name: str, new_task_name: str):
        return self.done_db.update_task(old_task_name, new_task_name)
    
    def remove_task(self, task:str):
        pass


    # TO DO --> DONE part
    def move_to_done(self, task, done_date: Date):
        self.done_db.insert_task(task, done_date)

        cycle = self.todo_db.get_cycle(task)
        done_shifted = done_date.get_shifted_date(cycle.period)
        delta = done_shifted.delta_with(cycle.next_date)
        if delta > 0:
            cycle.next_date = done_shifted
            self.todo_db.update_cycle(task, cycle)