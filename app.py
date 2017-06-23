from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response
#import requests
# Flask app should start in global layout
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def index():
	r = requests.get('http://192.168.66.128:9080/prweb/PRRestService/comm/commdata/GetServiceStatus')
	c = r.content
	j = json.loads(c)
	a= j['ONTStatus']+j['RGStatus']+j['STBStatus']
	return a
if __name__ == '__main__':
    app.run(debug=True)
