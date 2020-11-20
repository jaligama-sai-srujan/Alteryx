# Normal Imports
import requests
import os
import sys

# ODS Related Imports
import audb_connect
import create_schema
import create_table
import create_column

# Credentials
collibraUsername = os.getenv('COLLIBRA_USERNAME', default=False)
collibraPwd = os.getenv('COLLIBRA_PASSWORD', default=False)

if(not collibraUsername or not collibraPwd):
    # TODO: Send alert through SNS topic
    print("collibraUsername or collibraPwd not set yet")
    sys.exit("Username/Password not set")
else:
    print("All Creds Set")

# Create a session to be used by all the requests
with requests.Session() as session:
    session.auth = (collibraUsername, collibraPwd)
    
# Get cursor object for querying ODS
cur = audb_connect.getCursor()

# Collibra Constants
parentCommunityName = 'AUDB'
communityName = 'Alteryx'
#domainName = 'Aurora ODS Physical Data Dictionary'

# Query to get metadata from table
#query = "select schemaname, tablename, columnname, data_type from u_ops.collibra_metadata_1_vw;"
cur.execute(query)
results = cur.fetchall()

# results field order
# schemaName, tableName, colName, colType 
schemaList = []
tableList = []
colList = []
colAttrList = []
for result in results:
    schemaList.append(result[0])
    tableList.append(result[1])
    colList.append(result[2])
    colAttrList.append(('Column Data Type', result[3]))
    
create_schema.ingest_schema(communityName, domainName, schemaList, session, parentCommunityName)
create_table.ingest_table(communityName, domainName, schemaList, tableList, None, session, parentCommunityName)
create_column.ingest_column(communityName, domainName, schemaList, tableList, colList, colAttrList, session, parentCommunityName)