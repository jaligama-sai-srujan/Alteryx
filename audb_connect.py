# DB Imports
import psycopg2

# Normal Imports
import os
import sys


# Credentials
dbname = 'audb'
host = 'audb-ro.bi-prod.asu.edu'
port = '5432'
#user = os.getenv('AUDB_USERNAME', default=False)
#pwd = os.getenv('AUDB_PASSWORD', default=False)

if(not user or not pwd):
    # TODO: Send alert through SNS topic
    print("Alteryx User or Alteryx Pwd not set yet")
    sys.exit("Username/Password not set")
else:
    print("Alteryx Credentials Set")

# Create a DB Connection
try:
    conn=psycopg2.connect(dbname= dbname, host= host, port= port, user= user, password= pwd, sslmode='require')
except:
    print("error")
    


def getCursor():
    # Returns the DB connection cursor
    return conn.cursor()