# data moshtari
import sqlite3
from sqlite3 import Error

try:
    connect = sqlite3.connect('login.db')
except Error as error:
    print(error)


def insert(firstname, lastname, phonenumber, username, password):
    try:
        a = ("""INSERT INTO signup_m (FIRSTNAME,LASTNAME,PHONENUMBER,USERNAME,PASSWORD)\
         VALUES ("{}","{}","{}","{}","{}")"""
             .format(firstname, lastname, phonenumber, username, password))
        connect.execute(a)
        connect.commit()
    except Error as e:
        if str(e) == "UNIQUE constraint failed: signup_m.USERNAME":
            print("username tekrari")
        else:
            print(e)


def print_data(x):
    for i in connect.execute("""SELECT {} FROM signup_m """.format(x)):
        for j in i:
            yield j


def check_login(user, pas):
    pas_bool = False
    usr_bool = False
    i1 = False
    i2 = False
    i_d = False
    for k in zip(connect.execute("""SELECT USERNAME,PASSWORD,ID FROM signup_m """)):
        for i, j, p in k:
            if (str(user) == str(i) or str(user) == str(p)) and str(pas) == str(j):
                return True, True
    for i in print_data("USERNAME"):
        i1 += 1
        if str(user) == str(i):
            usr_bool = True
            break
    for i in print_data("ID"):
        i_d += 1
        if str(user) == str(i):
            usr_bool = True
            break
    return usr_bool, pas_bool


def del_row(x, y):
    connect.execute("""DELETE FROM signup_m WHERE {} = "{}" """.format(x, y))
    connect.commit()


def get_name(user):
    for w in zip(connect.execute("""SELECT USERNAME,ID,FIRSTNAME FROM signup_m """)):
        for i, j, k in w:
            if str(i) == user or str(j) == user:
                return k


def get_id(user):
    for w in zip(connect.execute("""SELECT USERNAME,ID FROM signup_m """)):
        for i, j in w:
            if str(i) == user:
                return j


def hamash(x):
    a = []
    for i in connect.execute(f"""SELECT ID,FIRSTNAME,LASTNAME,PHONENUMBER,USERNAME,PASSWORD \
    FROM signup_m WHERE USERNAME = "{x}" OR ID ="{x}" """):
        for j in i:
            a.append(j)
    return a
