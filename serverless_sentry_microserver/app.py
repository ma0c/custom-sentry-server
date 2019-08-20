from chalice import Chalice
import os
import gzip
from botocore.vendored import requests

app = Chalice(app_name='serverless_sentry_microserver')


@app.route('/')
def index():
    return {'status': 'OK'}


@app.route("/api/{pk}/store", methods=["GET", "POST"], cors=True)
def store(pk):
    print("Before request")
    request = app.current_request
    hook = os.environ.get("SLACK_HOOK_URL", "")
    print("hook")
    print(hook)
    data = gzip.decompress(request.raw_body).decode()
    print("data")
    print(data)
    requests.post(
        hook,
        json={
            "text": data
        }
    )

    return "OK"


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
