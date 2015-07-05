__author__ = 'neuraxis'


def valsleeptime(p_sleep_time):
    if len(p_sleep_time) != 4:return False
    i = 0
    while i <= 3:
        if p_sleep_time[i].isnumeric():i += 1
        else:return False
    if 0 <= int(p_sleep_time[0]) <= 2:
        if 0 <= int(p_sleep_time[1]) <= 9:
            if 0 <= int(p_sleep_time[2]) <= 6:
                if 0 <= int(p_sleep_time[3]) <= 9:return True
    else:return False