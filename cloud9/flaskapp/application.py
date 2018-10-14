# coding: utf-8
import json
from flask import Flask, Response

app = application = application = Flask(__name__)


@app.route("/test")
def test():
    return Response(json.dumps({'Output': 'Hello Test'}), mimetype='application/json', status=200)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

