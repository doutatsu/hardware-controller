from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<device>/<status>")
def socket_control(device, status):
 if status == "1":
   subprocess.call("sudo ./pihat --repeats=10 --id=1 --channel=0 --state=1",shell=True)
 else:
   subprocess.call("sudo ./pihat --repeats=10 --id=1 --channel=0 --state=0",shell=True)
 return jsonify(device='lights', status='1')

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)