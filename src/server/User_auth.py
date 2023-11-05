from typing import Dict, Set
from time import time
import psycopg2

def new_user(username, email, password):
    conn = psycopg2.connect(dbname='server_db')
    
    #example list all brewers and their countries 
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM users
    WHERE Name = %s;             
    ''',[username])
    if cur.fetchone() is not None: 
        conn.close()
        return 1 
    
    cur.execute('''
    SELECT * FROM users
    WHERE Email = %s;             
    ''',[email])

    a = cur.fetchone()
    if a is not None: 
        conn.close()
        return 2 

    cur.execute('''
    INSERT INTO users (Name, Email, Password)
    VALUES (%s, %s, %s);
    ''', [username, email, password])

    conn.commit()
    conn.close()
    return 3

def auth_login(username, password):
    conn = psycopg2.connect('dbname=server_db', )
    
    #example list all brewers and their countries 
    cur = conn.cursor()
    cur.execute('''
    SELECT Password
    FROM users
    WHERE Name = %s;
    ''', [username])

    usr = cur.fetchone()
    print(usr)
    if usr == None: 
        conn.close()
        print("[DATABASE] User dosent exist")
        return False
    elif usr is not None and usr[0] == password:
        conn.close()
        print("[DATABASE] Successful Login")
        return True #correct password
    else: 
        conn.close()
        print("[DATABASE] Failed Login")
        return False #incorrect password