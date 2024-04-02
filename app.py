from flask import Flask
from flask import Flask, redirect, url_for, request, render_template
import os
import math
import base64

app = Flask(__name__)
basename = '/iotcloud'


@app.route(basename+"/hello_world")
def hello_world():
   d = {
      "username": whoami().strip(),
      "env": "labs",
      "avatar": "https://sibidharan.me/wp-content/uploads/2020/06/Logo-round.png"
   }
   return render_template('helloworld.html', data=d)
   

@app.route(basename+'/')
def hello():
   return "<h1/>Welcome to Selfmade Ninja Academy</h1>"

@app.route(basename+'/whoami')
def whoami():
   return os.popen('whoami').read()

@app.route(basename+'/encode')
def encode():
   string = request.args['data'] # GET
   string = base64.b64decode(string)
   return string

# original string: something/asdkhbasd/asdjbasd
# encoded string: something%2Fasdkhbasd%2Fasdjbasd


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7000, debug=True)