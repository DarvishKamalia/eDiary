# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
# if __name__ == '__main__':
#     app.run()

import json


r = open ('test', 'r')
swag = json.load (r)
r.close
print swag["May 2015"][0]["Date"]
