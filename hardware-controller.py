from flask import Flask, jsonify, request
import subprocess
import sys
import requests
from threading import Thread
from time import sleep

app = Flask(__name__)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<device>/<status>")
def socket_control(device, status):
 if status == "1":
   subprocess.call("cd pihat && sudo ./pihat --repeats=10 --id=1 --channel=0 --state=1",shell=True)
   return jsonify(device='lights', status='1')
 else:
   subprocess.call("cd pihat && sudo ./pihat --repeats=10 --id=1 --channel=0 --state=0",shell=True)
   return jsonify(device='lights', status='0')
@app.route("/send")
def send_status():
  print "Sending status"
  payload = {"device": "Sensor 1", "status": "On"}
  r = requests.post("http://192.168.1.69:3000/sync", data=payload)
  return jsonify(r)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
