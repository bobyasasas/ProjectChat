import os
import sqlite3


def file_exist_check(path_name):
    return os.path.isfile(path_name)


def add_contract_local(user_id, username):
    conn = sqlite3.connect('./config/contracts.db')
    c = conn.cursor()
    c.execute("insert into contacts(id,username) values (?,?)", (user_id, username))
    print("联系人插入成功.")
    conn.commit()
    conn.close()


class Config:
    def __init__(self):
        if not file_exist_check("./config/user.db"):
            conn = sqlite3.connect('./config/user.db')
            print("user.db初始化中...")
            c = conn.cursor()
            c.execute('''CREATE TABLE user
                   (
                   username           TEXT    NOT NULL,
                   session            TEXT     NOT NULL,
                   last_login_time    double      NOT NULL
                   );''')
            print("数据表user创建成功")
            conn.commit()
            conn.close()
        if file_exist_check("./config/contacts.db"):
            os.remove("./config/contacts.db")
        conn = sqlite3.connect('./config/contacts.db')
        print("contacts.db初始化中...")
        c = conn.cursor()
        c.execute('''CREATE TABLE contacts
                (
                id                 int    NOT NULL,
                username           TEXT    NOT NULL
                );''')
        print("数据表contracts创建成功")
        conn.commit()
        conn.close()
