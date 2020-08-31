from flask import Flask, abort
from flask_cors import CORS
from getData import readFile, jsonResult
from parseFile import parseFile, getReverseDepends
import json


app = Flask(__name__)
CORS(app)

# This block of code is for getting data from a seperate json file,
# that file can be created by running 'getData.py',
# you can find it in 'data/dpkg_status.json'

# class Package:
#     def __init__(self, Package, Description, Reverse_Depends, Depends):
#         self.Package = Package
#         self.Description = Description
#         self.Depends = Depends
#         self.Reverse_Depends = Reverse_Depends

# class PackageEncoder(JSONEncoder):
#     def default(self, object):
#         return object.__dict__

# def getDpkgData():
#     try:
#         data = open('data/dpkg_status.json', 'r')
#     except OSError as error:
#         return None, error

#     with data:
#         packages = []
#         try:
#             data = json.load(data)
#         except json.decoder.JSONDecodeError as error:
#             return None, error
#         for d in data:
#             if 'Depends' not in d:
#                 d['Depends'] = None
#             packages.append(Package(d['Package'], d['Description'], d['Reverse_Depends'], d['Depends']))
#         return packages, None


@app.route('/api/dpkg', methods=['GET'])
def hello():
    return json.dumps(jsonResult(), indent=4)
  
   
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, port=80)
