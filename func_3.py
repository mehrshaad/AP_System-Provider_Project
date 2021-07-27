import sqlite3
from random import randint as hosne_niyaat
from sqlite3 import Error


try:
    connect = sqlite3.connect('login.db')
except Error as error:
    print(error)


def insert(charge):
    try:
        a = ("""INSERT INTO data (CHARGE)\
         VALUES ("{}")"""
             .format(charge))

        connect.execute(a)
        connect.commit()
    except Error as e:
        print(e)


def print_data(x):
    for i in connect.execute("""SELECT {} FROM data """.format(x)):
        for j in i:
            yield j


def sum_sood():
    a = connect.execute("""SELECT SUM(CHARGE) FROM data""")
    return round(list(a)[0][0] * (2/3))


def search_work_with_mekanizm_reghabati_ke_ba_hosne_niyaat_kar_mikone_fk(x):
    lis = []
    for i in connect.execute("""SELECT FIRSTNAME, LASTNAME FROM signup_kh WHERE ABILITY1 =\
     {} OR ABILITY2 = {} OR ABILITY3 = {} OR ABILITY4 = {} OR ABILITY5 = {}""".format(x, x, x, x, x)):
        lis.append(i)
    return lis[hosne_niyaat(0, len(lis))]


def print_between(ability, x, y):
    a = []
    for i in connect.execute(f"""SELECT FIRSTNAME,LASTNAME FROM data WHERE\
    ABILITY1 ="{ability}" OR ABILITY2 ="{ability}" OR ABILITY3 ="{ability}" OR ABILITY4 ="{ability}" OR ABILITY5 ="{ability}" AND\
      DATE BETWEEN {x} AND {y} """):
        a.append(' '.join(i))
    return a
