import config

from flask import Flask, request, jsonify

api = Flask(__name__)

api.get("/")