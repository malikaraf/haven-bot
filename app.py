import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/haven', methods=['POST'])
def haven_command():
    return jsonify({
        "response_type": "in_channel",
        "text": "Welcome to Haven! Here is your promotional message."
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
