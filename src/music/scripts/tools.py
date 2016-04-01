# coding=utf8
u'scripts/cron_task.py的工具。'

from functools import partial

# python apps
import datetime
import gevent
import time
import traceback


gs_list = []

# add_one_hour = lambda x: ':'.join((str(int(x.split(':')[0]) + 1), x.split(':')[1]))


def main():
    u'supervisor执行的程序'
    gevent.joinall(gs_list)


def is_in_same_day(argtime, fixed_point=0):
    if int(time.time()) - int(argtime) >= 3600 * 24:
        return False
    argtime = datetime.fromtimestamp(int(argtime))
    now = datetime.now()
    if now.day == argtime.day:
        return not (fixed_point > argtime.hour and fixed_point <= now.hour)
    else:
        if argtime.hour < fixed_point:
            return False
        return fixed_point > now.hour


def excute_fixed_time_task(func, hour, minute, weekday=None, year=0, month=0, day=0,
                           skip_day_timestamp_ids=None):
    if year != 0:
        assert day != 0 and month != 0
    if month != 0:
        assert day != 0
    _name = func.func.__name__ if isinstance(func, partial) else func.__name__

    while True:
        now = datetime.datetime.now()
        if now.hour == int(hour) and now.minute == int(minute) and now.isoweekday() == int(weekday or now.isoweekday()):
            if not ((day == now.day or day == 0) and (month == now.month or month == 0) and (
                    year == now.year or year == 0)):
                gevent.sleep(1)
                continue

            if skip_day_timestamp_ids is not None:
                skip = False
                for skip_day_timestamp in skip_day_timestamp_ids:
                    if is_in_same_day(skip_day_timestamp):
                        print 'skip', skip_day_timestamp
                        skip = True
                        break
                if skip:
                    gevent.sleep(1)
                    continue

            txt = ' '.join([str(now), 'fixed_time_task: ', _name])
            try:
                func()
                print 'exec func:', _name
                gevent.sleep(60)
            except:
                print traceback.format_exc()
                gevent.sleep(60)
        else:
            gevent.sleep(1)


def execute_interval_task(func, seconds):
    while True:
        gevent.sleep(seconds)
        try:
            func()
        except:
            print traceback.format_exc()


def fixed_time_task(func, hour, minute, weekday=None, year=0, month=0, day=0, skip_day_timestamp_ids=None):
    print('scripts/tools.py --> fixed_time_task(): ...')
    new_func = partial(excute_fixed_time_task, func, hour, minute, weekday, year, month, day,
                       skip_day_timestamp_ids)
    gs = gevent.spawn(new_func)
    gs_list.append(gs)
    # _name = func.func.__name__ if isinstance(func, partial) else func.__name__


def fixed_interval_task(func, seconds):
    new_func = partial(execute_interval_task, func, seconds)
    gs = gevent.spawn(new_func)
    gs_list.append(gs)
    # _name = func.func.__name__ if isinstance(func, partial) else func.__name__


'''
# ============  test  =================
def only_day(arg):
    print 'only day', arg

def only_day_and_month(arg):
    print 'only day and month', arg

def day_and_month_and_year(arg):
    print 'day and month and year', arg

def hour_interval():
    print 'run hour interval task when ', int(time.time())

now = datetime.datetime.now()
fixed_time_task(partial(only_day, 'good'), day=now.day, hour=now.hour, minute=now.minute + 1)
fixed_time_task(partial(only_day, 'bad'), day=now.day + 1, hour=now.hour, minute=now.minute + 1)
fixed_time_task(partial(only_day_and_month, 'good'), day=now.day, month=now.month, hour=now.hour, minute=now.minute + 1)
fixed_time_task(partial(only_day_and_month, 'bad'), day=now.day, month=now.month + 1, hour=now.hour,
                minute=now.minute + 1)
fixed_time_task(partial(day_and_month_and_year, 'good'), day=now.day, month=now.month, year=now.year, hour=now.hour,
                minute=now.minute + 1)
fixed_time_task(partial(day_and_month_and_year, 'bad'), day=now.day, month=now.month, year=now.year + 1, hour=now.hour,
                minute=now.minute + 1)

fixed_interval_task(hour_interval, seconds=3600)
'''


