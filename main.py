import requests
import json
import os
os.system('cls')
import time
import random
import sqlite3
import os

def main():
    os.system("clear")
    loginRegist = input("Belépés(a) || Regisztráció(b)\n>>>")
    if loginRegist == "a" or loginRegist == "b":
        if loginRegist == "a":
            login()
        if loginRegist == "b":
            regist()
    else:
        main()


def login():
    cur.execute("SELECT name FROM login;")
    name = cur.fetchone()
    print(name)
    if name == "('asd',)":
        print("szia")
    


def regist():
    name = input("Név: ")
    email = input("email: ")
    password = input("Jelszavad: ")
    print(f"név: {name}, email: {email}, Jelszó: ******")
    ins = cur.execute(f"insert into login (name, email, password) values ('{name}','{email}', '{password}')")
    con.commit()
    return main()

    
    
os.system("cls")

global filmek_label
filmek_label = list()

con = sqlite3.connect("login.db")
cur = con.cursor()
try:
    cur.execute("CREATE TABLE login(id INT PRIMARY KEY ,name, email, password)")
except:
    pass

if __name__ =="__main__":
    main()