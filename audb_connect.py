# DB Imports
import psycopg2

# Normal Imports
import os
import sys


# Credentials
dbname = os.getenv('AUDB_DBNAME', default=False)
host = os.getenv('AUDB_HOST', default=False)
port = os.getenv('AUDB_PORT', default=False)
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
