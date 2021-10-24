import config

# !!!from models import DetectModel
from flask import Flask, Response, request, jsonify
import json
import numpy as np
from rest_commons import *
import jsonpickle


api = Flask(__name__)


@api.post("/recognize_one_photo")
def recognize_one_photo():
    api_token = request.args.get("token")
    if check_token(api_token) is False:
        return f"Authorization is false. Your api token {api_token} is wrong!"
    print(api_token)
    data = request.files.get('file')
    print(request.data)
    print(type(request.data))
    nparr = np.fromstring(str(request.data), np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")


@api.post("/recognize_batch")
def recognize_batch():
    api_token = request.args.get("token")
    if check_token(api_token) is False:
        return f"Authorization is false. Your api token {api_token} is wrong!"
    print(api_token)
    data = request.files.get('file')
    print(request.data)
    print(type(request.data))
    nparr = np.fromstring(str(request.data), np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")


@api.post("/detecting_one")
def detecting_one():
    api_token = request.args.get("token")
    if check_token(api_token) is False:
        return f"Authorization is false. Your api token {api_token} is wrong!"
    print(api_token)
    data = request.files.get('file')
    print(request.data)
    print(type(request.data))
    nparr = np.fromstring(str(request.data), np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")


@api.post("/detecting_batch")
def detecting_batch():
    api_token = request.args.get("token")
    if check_token(api_token) is False:
        return f"Authorization is false. Your api token {api_token} is wrong!"
    print(api_token)
    data = request.files.get('file')
    print(request.data)
    print(type(request.data))
    nparr = np.fromstring(str(request.data), np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")


@api.post("/detecting_video")
def detecting_video():
    api_token = request.args.get("token")
    if check_token(api_token) is False:
        return f"Authorization is false. Your api token {api_token} is wrong!"
    print(api_token)
    data = request.files.get('file')
    print(request.data)
    print(type(request.data))
    nparr = np.fromstring(str(request.data), np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # do some fancy processing here....
    # build a response dict to send back to client
    response = {'message': 'image received. size={}x{}'.format(img.shape[1], img.shape[0])
                }
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)
    return Response(response=response_pickled, status=200, mimetype="application/json")