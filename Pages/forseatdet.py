import sys
from tkcalendar import Calendar,DateEntry
from datetime import date
from PIL import ImageTk, Image
import PIL
import datetime

import pymysql
import pymysql.cursors
import paramiko
import pandas as pd
from paramiko import SSHClient
from sshtunnel import SSHTunnelForwarder
import re
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from tkinter import messagebox
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
sql_hostname = '127.0.0.1'
mypkey = paramiko.RSAKey.from_private_key_file('dem.pem')
sql_username = 'root'
sql_password = 'Srishtisingh@12'
sql_main_database = 'movie'
sql_port = 3306
ssh_host = '34.229.131.207'
ssh_user = 'ec2-user'
ssh_port = 22
def querys(slot_id,status):
    with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=mypkey,
            remote_bind_address=(sql_hostname, sql_port)) as tunnel:
        try:
            conn = pymysql.connect(host='127.0.0.1', user=sql_username,
                    passwd=sql_password, db=sql_main_database,
                    port=tunnel.local_bind_port)
            cur=conn.cursor()
            for i in range(40):
                sql = "INSERT INTO seatdet (slot_id,status) VALUES (%s, %s)"
                val = (slot_id,status)
                cur.execute(sql,val)
                #cur.execute(q)
                conn.commit()
                #cur.execute("select * from User")
                #result = cur.fetchone()
                #print(result)
                #data = pd.read_sql_query(q, conn)
            conn.close()
            print("sucess")
            return 1
        except Exception as e:
            print(e)
            return 0
i=0	
slot_id=input("write slot id:")
status=input("write status :")
querys(slot_id,status)

