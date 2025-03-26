import sqlite3 as sql


def connect_db():
    return sql.connect("database.db")
