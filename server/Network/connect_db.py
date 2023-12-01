import sqlite3 as sq


class Connect_DB:
    def __init__(self, database):
        self.database = database

    def create_db(self):
        """Создание БД"""
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS users (\
                        id INTEGER NOT NULL PRIMARY KEY,\
                        login TEXT NOT NULL,\
                        password TEXT NOT NULL,\
                        isActiv INTEGER)')

    def delete_table_db(self, name_table):
        """Удаление таблицы name_table из БД database"""
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute(f'DROP TABLE IF EXISTS{name_table}')

    def select_db(self, request):
        """
        Выбор данных из таблицы
        SELECT col1, col2,... FROM имя_таблицы WHERE условие
        """
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute(f'{request}')
            results = cur.fetchall()
            # for results in cur:
            #     print(results)
            return results

    def update_db(self, request):
        """
        Изменение данных в записи
        UPDATE имя_таблицы SET имя_столбца = новое значение WHERE условие
        """
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute(f'{request}')

    def delete_db(self, request):
        """
        Удаление записей из таблицы
        DELETE FROM имя_таблицы WHERE условие
        """
        with sq.connect(self.database) as con:
            cur = con.cursor()
            cur.execute(f'{request}')

    def count_select_db(self):
        """
        Подсчет записей
        SELECT count(имя_колонки) FROM имя_таблицы WHERE условие
        count, sum, avr, min. max
        """
        pass

    def group_bd(self):
        """
        Группировка, например по id
        GROUP BY имя_поля
        """
        pass

    def join_table(self, table1, table2):
        """
        Объединение таблиц
        JOIN таблица ON условие связывание
        """
        pass



if __name__ == '__main__':
    database = 'database\\users.db'
    db = Connect_DB(database)
    db.create_db()
