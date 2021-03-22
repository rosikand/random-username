"""
File: app.py
------------------
This is the runner file for the Flask app. 
"""

from flask import Flask, render_template, request
from random_username import get_random_username 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html') 

# background process happening without any refreshing
@app.route('/get_usernames')
def get_usernames():
    master_list = []
    for i in range(5):
        master_list.append(get_random_username())
    return render_template('usernames.html', username_list=master_list)
