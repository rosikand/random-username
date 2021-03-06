"""
File: app.py
------------------
This is the file used to create the Flask app and assiociated routings. 
"""

from flask import Flask, render_template, request
from random_username import get_random_username 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html') 


@app.route('/get_usernames')
def get_usernames():
    # the following three lines are for generating multiple usernames at once. 
#     master_list = []
#     for i in range(5):
#         master_list.append(get_random_username())
    return render_template('usernames.html', username_list=get_random_username())
