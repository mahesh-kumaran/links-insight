from flask import jsonify

class RequestException(Exception):
    def __init__(self, status_code, code, message):
        self.status_code = status_code
        self.code = code
        self.message = message

    def __str__(self):
        return "http_status_code: " + self.status_code + "|" + self.code + ": " + self.message

def bad_request(code, message):
    raise RequestException(400, code, message) 

def not_found(code, message):
    raise RequestException(404, code, message) 

def forbidden(code, message):
    raise RequestException(401, code, message)

def ok(code, message=None):
    result = {'code': code}
    
    if message is not None:
        result['message'] = message

    resp = jsonify(result)
    resp.status_code = 200
    return resp
