import time

from logic.cycle import Cycle
from logic.date import Date



def preprocess_task(task):
    if task == '':
        return None, 'task field cannot be empty'
    
    return task, ''


def preprocess_period(period):
    if period == '':
        return None, 'period field cannot be empty'
    
    try:
        period = int(period)
    except ValueError as e:
        return None, 'period should be a number (days), no additional symbols allowed'
    
    return period, ''


def preprocess_next_date(next_date):
    if next_date == '':
        return None, 'next date field cannot be empty'
    
    try:
        next_date = next_date.split('.')
        next_date = Date(int(next_date[2]), int(next_date[1]), int(next_date[0]))
    except:
        return None, 'dates should have format DD.MM.YYYY'


    today = time.localtime()
    if next_date.delta_with(today[:3]) < 0:
        return None, 'make sure next date of the cycle is not in the past'
        
    return next_date, ''


def preprocess_cycle(task, period, next_date):
    elements = [task, period, next_date]
    functions = [preprocess_task, preprocess_period, preprocess_next_date]
    
    for i in range(len(elements)):
        elements[i], msg = functions[i](elements[i])
        if not elements[i]:
            return None, msg

    new_cycle = Cycle(*elements)
    return new_cycle, ''