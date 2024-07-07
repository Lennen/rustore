#!/usr/bin/env python
#import os

from flask import Flask, request, send_file
#from pymongo import MongoClient
#from bson.json_util import dumps
#from  Model import Model
from flask_cors import CORS

#from flask import Flask, request
#from flask_cors import CORS

app = Flask(__name__)
from app import views
cors = CORS(app, resources={r"/*": {"origins": "*"}})
