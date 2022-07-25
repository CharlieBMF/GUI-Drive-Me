import sqlite3
import functools

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
    cur.execute("SELECT * FROM rides WHERE date=?", (day,))
    results = cur.fetchone()
    if results:
        car_karol = results[2]
        car_pioter = results[3]
    else:
        car_karol = 'No data'
        car_pioter = 'No data'
    return {'car_karol': car_karol, 'car_pioter': car_pioter}


@connect_wrapper
def insert_ride_info(cur, day, car, driver):
    if car:
        cur.execute("SELECT * FROM rides WHERE date=?", (day,))
        data_exist = cur.fetchall()
        if driver == 'Karol':
            if data_exist:
                cur.execute("UPDATE rides SET Karol=? WHERE date=?", (CARS_DICTIONARY[car], day))
            else:
                cur.execute("INSERT INTO rides(date, Karol) Values (?,?)", (day, CARS_DICTIONARY[car]))
        if driver == 'Pioter':
            if data_exist:
                cur.execute("UPDATE rides SET Pioter=? WHERE date=?", (CARS_DICTIONARY[car], day))
            else:
                cur.execute("INSERT INTO rides(date, Pioter) Values (?,?)", (day, CARS_DICTIONARY[car]))
        cur.execute("SELECT * FROM rides WHERE date=?", (day,))


@connect_wrapper
def calculate_drives(cur):
    cur.execute('SELECT * FROM rides WHERE Karol NOT NULL AND Pioter NOT NULL')
    all_rides = cur.fetchall()
    cur.execute("SELECT * FROM rides WHERE date BETWEEN '2022-07-01' and '2022-07-30'")
    month_rides = cur.fetchall()
    all_rides_pioter = 0
    month_rides_pioter = 0
    all_rides_karol = 0
    month_rides_karol = 0
    for ride in all_rides:
        if ride[2] == ride[3]:
            if ride[2] in CARS_KAROL:
                all_rides_karol += 1
            else:
                all_rides_pioter += 1
    for ride in month_rides:
        if ride[2] == ride[3]:
            if ride[2] in CARS_KAROL:
                month_rides_karol += 1
            else:
                month_rides_pioter += 1
    return {'all_rides_karol': all_rides_karol,
            'all_rides_pioter': all_rides_pioter,
            'month_rides_karol': month_rides_karol,
            'month_rides_pioter': month_rides_pioter}

initial_connect()
