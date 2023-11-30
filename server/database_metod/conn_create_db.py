import sqlite3 as sq


class Create_Data_Base():
    def __init__(self, database):
        with sq.connect(database) as con:
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS users (\
                        id INTEGER NOT NULL PRIMARY KEY,\
                        login TEXT NOT NULL,\
                        password NOT NULL)')


class Del_Data_Base():
    def __init__(self, database, name_table):
        with sq.connect(database) as con:
            cur = con.cursor()
            cur.execute(f'DROP TABLE IF EXISTS{name_table}')



if __name__ == '__main__':
    database = 'database\\users.db'
    db = Create_Data_Base(database)
