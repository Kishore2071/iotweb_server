from flask import Flask
from flask import Flask, redirect, url_for, request, render_template, session
import os
import math
import base64
from src import get_config
from src.User import User


basename = get_config("basename")
app = Flask(__name__, static_folder='assets', static_url_path=basename)
app.secret_key = get_config("secret_key")

@app.route(basename+"/dashboard")
def dashboard():
   return render_template('dashboard.html', session=session)

@app.route(basename+"/auth", methods=['POST'])
def authenticate():
   if session.get('authenticated'): #TODO: Need more validattion like login expiry
      return {
         "message": "Already Authenticated",
         "authenticated": True
      }, 202
   else:
      if 'username' in request.form and 'password' in request.form:
         username = request.form['username']
         password = request.form['password']
         try:
            User.login(username, password)
            session['authenticated'] = True
            # return {
            #    "message": "Successfully Authenticated",
            #    "authenticated": True
            # }, 200
            return redirect(url_for('dashboard'))
         except Exception as e:
            return {
               "message": str(e),
               "authenticated": False
            }, 401
      else:
         return {
            "message": "Not enough parameters",
            "authenticated": False
         }, 400

@app.route(basename+"/deauth")
def deauth():
   if session.get('authenticated'): #TODO: Need more validattion like login expiry
      #Remove / invalidate session from database
      session['authenticated'] = False
      # return {
      #    "message": "Successfully Deauthed",
      #    "authenticated": False
      # }, 200
      return redirect(url_for('dashboard'))

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7000, debug=True)