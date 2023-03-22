from typing import Tuple

from flask import jsonify, Response
from werkzeug.exceptions import HTTPException

from app import app


@app.errorhandler(HTTPException)
def process_error(error: HTTPException) -> Tuple[Response, int]:
    code = error.code or 500
    response = jsonify({
        'error': error.name,
        'code': code,
    })
    return response, code
