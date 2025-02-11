from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/message', methods=['GET'])
def send_message():
    return jsonify({"message": "Hello from VM2!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
