import sqlite3
import functools


def initial_connect():
    conn = sqlite3.connect('rides')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS rides (id INTEGER PRIMARY KEY, date DATE, Karol TEXT, Pioter TEXT)")
    conn.commit()
    conn.close()


def connect_wrapper(func):
    def func_with_wrapper(*args, **kwargs):
        conn = sqlite3.connect('rides')
        cur = conn.cursor()
        print(args, kwargs)
        result = func(cur, *args, **kwargs)
        print(str(result))
        conn.commit()
        conn.close()
        return result
    return func_with_wrapper


@connect_wrapper
def check_calendar_day(cur, day):
    cur.execute(f'SELECT * FROM rides WHERE date={day}')
    results = cur.fetchall()
    return results


initial_connect()
check_calendar_day(day='2022-07-02')

