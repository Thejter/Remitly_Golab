import json

def checkResourceFieldInJsonFile(jsonFileDirectory):
    # load file
    try:
        downloadedJsonFile = open(jsonFileDirectory, "r")
        data = downloadedJsonFile.read()
        downloadedJsonFile.close()
    except:
        # could not open or read JSON file
        return True
    
    # parse JSON
    try:
        parsedJson = json.loads(data)
    except:
        # could not parse JSON file
        return True
        
    #get Resource field value
    try:
        policyDocument = parsedJson["PolicyDocument"]
    except:
        # could not find PolicyDocument field in JSON file
        return True
    
    try:
        statement = policyDocument["Statement"][0]
    except:
        # could not find Statement fields and get first one in JSON file
        return True
    
    try:
        resource = statement["Resource"]
    except:
        # could not find Resource field in JSON file
        return True
    
    # check if Resource field value is equal to a single asterisk
    return resource != "*"