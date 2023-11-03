from typing import Dict, Set
from time import time
import psycopg2

def valid_input(username, password, email = None):
    pass

def new_user(username, email, password):
    try:
        conn = psycopg2.connect(dbname='server_db')
        
        #example list all brewers and their countries 
        cur = conn.cursor()
        cur.execute('''
        SELECT * FROM users
        WHERE Name = %s;             
        ''',[username])
        print(cur.fetchone())
        if cur.fetchone() is not None: 
            return 1 #username taken
        
        cur.execute('''
        SELECT * FROM users
        WHERE Email = %s;             
        ''',[email])

        if cur.fetchone() is not None: 
            return 2 #email taken

        cur.execute('''
        INSERT INTO users (Name, Email, Password)
        VALUES (%s, %s, %s);
        ''', [username, email, password])

        conn.commit()
        return 3

    except psycopg2.Error as err:
        print("[DATABASE] error", err)
        return False
    finally:
        if (conn):
            conn.close()
            return False

def auth_login(username, password):
    try:
        conn = psycopg2.connect('dbname=server_db', )
        
        #example list all brewers and their countries 
        cur = conn.cursor()
        cur.execute('''
        SELECT Password
        FROM users
        WHERE Name = %s;
        ''', [username])

        usr = cur.fetchall()

        if usr == None: 
            conn.close()
            print("[DATABASE] User dosent exist")
            return False
        elif usr != None and usr[0] == password:
            conn.close()
            print("[DATABASE] Successful Login")
            return True #correct password
        else: 
            conn.close()
            print("[DATABASE] Failed Login")
            return False #incorrect password

    except psycopg2.Error as err:
        print("[DATABASE] error", err)
    finally:
        if (conn):
            conn.close()