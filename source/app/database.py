#!/usr/bin/env python

# File: db.py
# Written By: Luis Moraguez
# Description: Contains all database settings and methods for use with Flask App

# IMPORTS
import datetime
import os
from peewee import *

# DATABASE SETTINGS
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")

if os.getenv("TESTING") == "true":
    print("Running in test mode => Using Sqlite in memory")
    db = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    db = MySQLDatabase(MYSQL_DATABASE,user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOST,port=MYSQL_PORT)

# DATABASE MODELS

## Contact Model
class Contact(Model):
    firstname = CharField()
    lastname = CharField()
    email = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = db


# DATABASE CONNECT AND INITIALIZE TABLES IF THEY DON'T EXISTS
print(db)
db.connect()
db.create_tables([Contact])
db.close()