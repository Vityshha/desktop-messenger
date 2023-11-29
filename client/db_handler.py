import sqlite3

def login(login, password, signal):
    con = sqlite3.connect("C:\\Users\\KFU\\Desktop\\desktop-messenger\\database\\users")
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == password:
        signal.emit('Успешная регистрация')
    else:
        signal.emit('Проверте правильность ввода данных')

    cur.close()
    con.close()


def register(login, password, signal):
    con = sqlite3.connect("C:\\Users\\KFU\\Desktop\\desktop-messenger\\database\\users")
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()

    if value != []:
        signal.emit('Такой ник уже используется')
    elif value == []:
        cur.execute(f'INSERT INTO users (login, password) VALUES ("{login}", "{password}");')
        signal.emit('Успешная регистрация')
        con.commit()

    cur.close()
    con.close()