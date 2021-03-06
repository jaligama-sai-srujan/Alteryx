import json
import json_object_parser as parser

# create a json obj to store the parsed results
json_obj = []

# create community, domain and asset object
community_list = []
domain_list = []
asset_set = set()
asset_list = []

def ingest_schema(communityName, domainName, schemaList, session, parentCommunityName = None):
    
    community_list.append(communityName)
    domain_list.append((communityName, domainName, 'Physical Data Dictionary'))

    # adds all the schema to the asset list
    for schemaName in schemaList:
        asset_set.add((communityName, domainName, schemaName, 'Schema'))
    
    #convert asset set to a list
    asset_list = list(asset_set)
    
    for community in community_list:
        json_obj.append(parser.getCommunityObj(community, parentCommunityName))
    
    for communityName, domainName, domainType in domain_list:
        json_obj.append(parser.getDomainObj(communityName, domainName, domainType))
    
    for communityName, domainName, assetName, assetType in asset_list:
        json_obj.append(parser.getAssetObj(communityName, domainName, assetName, assetType))
    
    with open("schema_template.json", "w") as write_file:
        json.dump(json_obj, write_file)
    
    url = 'https://asu-dev.collibra.com/rest/2.0/import/json-job'
    # url = 'https://asu.collibra.com/rest/2.0/import/json-job'
    
    files = {'file': open('schema_template.json', 'rb')}
    payload = {'sendNotification':'true'}
 
    response = session.post(url, files=files, data=payload)
    
    # print(response.request.headers)
    
    if response:
        print(response.json())
    else:
        print(response.text)