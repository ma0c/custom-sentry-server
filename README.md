# Custom Sentry Server

This is a simple proof of concept to implement a [sentry server](https://sentry.io), that receives
an HTTP post on each error.

This server send a slack message via Hook

## Usage

[Create a slack hook](https://api.slack.com/incoming-webhooks)

On OSX and Linux

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
SLACK_HOOK_URL="put here your slack url hook" python server.py
```

On other terminal

```bash
python error.py
```

An error should appear in your slack
