from typing import List

from logic.date import Date
from logic.cycle import Cycle



class DbTodoInterface:

    def create_cycle(self, cycle: Cycle) -> None:
        pass

    def get_cycle(self, task: str) -> Cycle:
        pass

    def get_all_cycles(self) -> List[Cycle]:
        pass

    def update_cycle(self, task: str, new_cycle: Cycle) -> None:
        pass

    def remove_cycle(self, task: str) -> None:
        pass


class DbDoneInterface:
    def get_tasks(self, date: Date) -> List[str]:
        pass

    def get_dates(self, task: str) -> List[Date]:
        pass

    def insert_task(self, task: str, date: Date) -> None:
        pass

    def update_task(self, old_task_name: str, new_task_name: str) -> None:
        pass

    def remove_task(self, task: str, date: Date) -> None:
        pass