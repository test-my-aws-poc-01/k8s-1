from flask import Response, jsonify

import os

from app import app


@app.route('/<path:xxx>')
@app.route('/', defaults={'xxx': '/'})
def hello_world(xxx: str) -> Response:
    msg = (
        f'Hello {xxx} from {app.config["STARTUP_IDENTIFIER"]} ({app.config["SERVICE_NAME"]})'
        f' {os.environ}'
    )
    app.logger.info(msg)
    return jsonify(msg)
