import sqlite3


class Authorization:
    def __init__(self, data_base_path):
        self.data_base_path = data_base_path

    def login(self, login, password):
        with sqlite3.connect(self.data_base_path) as con:
            cur = con.cursor()

            cur.execute(f'SELECT * FROM users WHERE login="{login}";')
            value = cur.fetchall()

            if value != [] and value[0][2] == password:
                print('Вход')
            else:
                print('Проверте правильность ввода данных')


    def register(self, login, password):
        with sqlite3.connect(self.data_base_path) as con:
            cur = con.cursor()

            cur.execute(f'SELECT * FROM users WHERE login="{login}";')
            value = cur.fetchall()

            if value != []:
                print('Такой ник уже используется')
            elif value == []:
                cur.execute(f'INSERT INTO users (login, password) VALUES ("{login}", "{password}");')
                print('Успешная регистрация')
                con.commit()