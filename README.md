# dpkg_status
This Flask API will read and return information from ```/var/lib/dpkg/status``` file, which stores information of installed packages in Linux system (Debian, Ubuntu)

You can find examples of those information in the file **data/status.real**

### Usage (in Terminal)
Running API: 
  - > git clone ht<span>tps://github.com/shilena91/dpkg_status.git
  - > python3 -m venv venv
  - > . venv/bin/activate
  - > pip install flask
  - > pip install flask-cors
  - > flask run
  
 If you want to export JSON data to a seperate file, modify the output file in **getData.py** and run ```python3 getData.py```

### Files
- **api.py** - creating API endpoint
- **getData.py** - read and write JSON data to a seperate file (ex. ```data/dpkg_status.json```)
- **parseFile.py** - parse information to JSON

In the future I will add a script to monitor and automatic update whenever there is a change in ```/var/lib/dpkg/status``` file, and possibly adding flags to **getData.py**, so user would easier decide input and output files
