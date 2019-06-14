import os

from sentry_sdk import init
domain = os.environ.get("DOMAIN", "localhost:5000")
init(f'http://asd@{domain}/1')

division_by_zero = 1 / 0

