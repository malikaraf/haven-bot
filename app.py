import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/haven', methods=['POST'])
def haven_command():
    return jsonify({
        "response_type": "in_channel",
        "text": "*<https://www.usehaven.com/|Haven>* is a next gen accounting firm + platform. Bookkeeping, taxes, tax credits, invoicing, bill pay and more for startups.\nWe are their customers and love them. Wanted to recommend them. If anyone wants an intro please let us know and we will introduce you to their CEO on slack.\nTheir team are ex EY/KPMG CPAs and they serve 1000+ amazing businesses. Every client has a dedicated CPA and slack channel that their team is available in 24/7, 365.\nTheir approach is tech-enabled, streamlining the accounting and tax process with powerful automation via their platform, while simultaneously providing the expert human touch.\nSome notable customers include: <https://sierra.ai/|Sierra>, <https://www.felixpago.com/en|Felix>, <https://superpower.com/|Superpower>, <https://flora.ai/|Flora>, to name a few.<https://www.usehaven.com/|Haven>"
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
