import sqlite3

class Authorization:
    def __init__(self, data_base_path):
        self.data_base_path = data_base_path
        self.correct = 1

    def login(self, login, password):
        with sqlite3.connect(self.data_base_path) as con:
            cur = con.cursor()

            cur.execute(f'SELECT * FROM users WHERE login="{login}";')
            value = cur.fetchall()

            if value != [] and value[0][2] == password:
                self.correct = 0
            else:
                self.correct = 1


    def register(self, login, password, ip):
        with sqlite3.connect(self.data_base_path) as con:
            cur = con.cursor()

            cur.execute(f'SELECT * FROM users WHERE login="{login}";')
            value = cur.fetchall()

            if value != []:
                self.correct = 1
            elif value == []:
                cur.execute(f'INSERT INTO users (login, password, addres) VALUES ("{login}", "{password}", "{ip}");')
                self.correct = 0
                con.commit()