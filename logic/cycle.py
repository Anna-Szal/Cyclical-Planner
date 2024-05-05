from dataclasses import dataclass
from logic.date import Date



@dataclass
class Cycle:
    task: str
    period: int
    next_date: Date
