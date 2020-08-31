import os, json, collections
from parseFile import parseFile, getReverseDepends

def readFile():
    try:
        file = open('/var/lib/dpkg/status', 'r')
    except OSError:
        try:
            file = open('data/status.real', 'r')
        except OSError:
            raise SystemExit
    data = file.read()
    file.close()
    return data

def jsonResult():
    dataFile = readFile()
    jsonList = collections.OrderedDict()
    jsonList = parseFile(dataFile)
    getReverseDepends(jsonList)
    return jsonList

targetFile = open('data/dpkg_status.json', 'w')
json.dump(jsonResult(), targetFile, indent=4)
