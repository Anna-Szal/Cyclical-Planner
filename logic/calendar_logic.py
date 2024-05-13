import calendar
import numpy as np



def get_days_grid(year):
    days = []
    for i in range(12):
        month = i+1
        start_day, num_days = calendar.monthrange(year, month)
        month_days = np.arange(num_days)+1
        month_days = month_days.reshape((-1,1))
        month_arr = np.full(month_days.shape, month)
        month_days = np.concatenate((month_arr, month_days), 1)
        days.append(month_days)

    days = np.concatenate(days)

    start_day, num_days = calendar.monthrange(year, 1)
    if start_day > 0:
        month_days = np.zeros((start_day, 2), dtype=int)
        days = np.concatenate((month_days , days))

    if len(days)%7:
        trailing_zeros_num = (len(days)//7 + 1) * 7 - len(days)
        trailing_zeros_num = np.zeros((trailing_zeros_num, 2), dtype=int)
        days = np.concatenate((days, trailing_zeros_num))

    return days.reshape(-1, 7, 2).transpose((1, 0, 2))