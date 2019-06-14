from flask import Flask, request
import gzip
import os
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
   print(request.values)
   return "OK"


@app.route("/api/<int:pk>/store/", methods=["GET", "POST"])
def store(pk):
    hook = os.environ.get("SLACK_HOOK_URL", "")
    print(hook)
    data = gzip.decompress(request.data).decode()
    requests.post(
        hook,
        json={
            "text": data
        }
    )

    return "OK"


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
