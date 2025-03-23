from flask import Flask, render_template, request, jsonify
import numpy as np
import deadlock  # Import the deadlock detection logic

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    data = request.json
    processes = int(data['processes'])
    resources = int(data['resources'])
    allocation = np.array(data['allocation']).reshape(processes, resources)
    request_matrix = np.array(data['request']).reshape(processes, resources)

    deadlock_detected, message = deadlock.detect_deadlock(processes, resources, allocation, request_matrix)

    return jsonify({"deadlock": deadlock_detected, "message": message})

if __name__ == "__main__":
    app.run(debug=True)
