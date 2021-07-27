# data khadamati
import sqlite3
from sqlite3 import Error

temp = []
try:
    connect = sqlite3.connect('login.db')
except Error as error:
    print(error)


def insert(phonenumber='', username='', password=''):
    global temp
    try:
        a = ("""INSERT INTO signup_kh (FIRSTNAME,LASTNAME,PHONENUMBER,USERNAME,PASSWORD\
        ,ABILITY1,ABILITY2,ABILITY3,ABILITY4,ABILITY5)\
         VALUES ("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")"""
             .format(temp[0], temp[1], phonenumber, username, password, temp[2], temp[3], temp[4], temp[5], temp[6]))
        connect.execute(a)
        connect.commit()
    except Error as e:
        if str(e) == "UNIQUE constraint failed: signup_kh.USERNAME":
            print("username tekrari")
        else:
            print(e)


def data_temp(lis):
    global temp
    temp = []
    temp = lis
    while len(temp) != 7:
        temp.append("")


def print_data(x):
    for i in connect.execute("""SELECT {} FROM signup_kh """.format(x)):
        for j in i:
            yield j


def print_ability():
    a = []
    for i in connect.execute("""SELECT ABILITY1,ABILITY2,ABILITY3,ABILITY4,ABILITY5 FROM signup_kh """):
        for j in i:
            a.append(j)
    return set(a)


def print_hamal(x):
    a = []
    for i in connect.execute(f"""SELECT FIRSTNAME,LASTNAME FROM signup_kh WHERE ABILITY1 ="{x}" OR ABILITY2 ="{x}" OR ABILITY3 ="{x}" OR ABILITY4 ="{x}" OR ABILITY5 ="{x}" """):
        a.append(' '.join(i))
    return a


def check_login(user, pas):
    pas_bool = False
    usr_bool = False
    i1 = 0
    i2 = 0
    for k in zip(connect.execute("""SELECT USERNAME,PASSWORD FROM signup_kh """)):
        for i,j in k: 
            if str(user) == str(i) and str(pas) == str(j):
                return True,True
    for i in print_data("USERNAME"):
        i1 += 1
        if str(user) == str(i):
            usr_bool = True
            break
    return usr_bool, pas_bool


def del_row(x):
    connect.execute("""DELETE FROM signup_kh WHERE USERNAME = "{}" """.format(x))
    connect.commit()


def get_name(user):
    for w in zip(connect.execute("""SELECT USERNAME,ID,FIRSTNAME FROM signup_kh """)):
        for i, j, k in w:
            if str(i) == user or str(j) == user:
                return k
