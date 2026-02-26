from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/haven', methods=['POST'])
def haven_command():
    return jsonify({
        "response_type": "in_channel",
        "text": "🏡 Welcome to Haven! Here is your promotional message."
    })

if __name__ == '__main__':
