import sqlite3
import functools
import datetime

CARS_DICTIONARY = {
    1: 'Clio',
    2: 'Mercedes',
    3: 'Seat',
    4: 'Tojka',
    5: 'Yamaha'
}

CARS_KAROL = [
    'Tojka',
    'Seat',
]

CARS_PIOTER = [
    'Mercedes',
    'Clio',
    'Yamaha'
]

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
        result = func(cur, *args, **kwargs)
        conn.commit()
        conn.close()
        return result
    return func_with_wrapper


@connect_wrapper
def check_calendar_day(cur, day):
    cur.execute(f"SELECT * FROM rides WHERE date={day}")
    results = cur.fetchone()
    print(results)
    if results:
        car_karol = results[2]
        car_pioter = results[3]
    else:
        car_karol = 'No data'
        car_pioter = 'No data'
    return {'car_karol': car_karol, 'car_pioter': car_pioter}
    # cur.execute("INSERT INTO rides( date, Karol, Pioter) VALUES (?,?,?)", (day, 'Tojka', 'Clio'))
    # z = cur.execute('SELECT * FROM rides')
    # s = z.fetchall()
    # print(s)

# @connect_wrapper
# def karol_insert_ride_info(cur, car):
#     cur.execute('INSERT INTO rides')


@connect_wrapper
def calculate_drives(cur):
    cur.execute('SELECT * FROM rides WHERE Karol NOT NULL AND Pioter NOT NULL')
    all_rides = cur.fetchall()
    cur.execute("SELECT * FROM rides WHERE date BETWEEN '2022-07-01' and '2022-07-30'")
    actual_month_rides = cur.fetchall()
    print(all_rides)
    print(actual_month_rides)
    rides_pioter = 0
    rides_karol = 0
    for ride in all_rides:
        if ride[2] == ride[3]:
            if ride[2] in CARS_KAROL:
                rides_karol += 1
            else:
                rides_pioter += 1
    return {'rides_karol': rides_karol, 'rides_pioter': rides_pioter}

initial_connect()
check_calendar_day(day='2022-07-02')


