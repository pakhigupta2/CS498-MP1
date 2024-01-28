from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def stress_host():
    if request.method == 'POST':
        subprocess.Popen(["python3", "stress_cpu.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return "Stress CPU Started"
    if request.method == 'GET':
        return socket.gethostname()

if __name__ == '__main__':
    app.run('0.0.0.0',port=80)
