import psycopg2
import configparser
import os

def loadFile():

    # loading config
    conf = configparser.ConfigParser()
    conf.read("conn.conf")
    db_name = conf.get("db", "db_name")
    db_usr = conf.get("db", "db_usr")
    db_password = conf.get("db", "db_password")
    db_host = conf.get("db", "db_host")
    db_port = conf.get("db", "db_port")
    sqlcom = conf.get("conf", "conf_command")
    # set up connection to database
    connectdb = psycopg2.connect(database=db_name, user=db_usr, password=db_password, host=db_host, port=db_port)
    cur = connectdb.cursor()
    cur.execute(sqlcom)
    rows = cur.fetchall()
    return rows

d