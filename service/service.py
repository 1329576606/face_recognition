from flask import Flask, request
import json
import face_client;

app = Flask(__name__)

# =============================================================================
# Routes

@app.route('/ping', methods=['GET', 'POST'])
def ping_handler():
    return json.dumps({
        'status': 'ok',
        'error': [],
        'method': 'ping',
        'result': []
    })

@app.route('/encoding', methods=['GET'])
def add_handler():
    path = request.form['fileUrl']
    encodings=face_client.face_encodings_from_url(path)
    for encoding in encodings:
        res=encoding.tolist()
        return json.dumps({
            'status': 'ok',
            'error': [],
            'method': 'add',
            'result': res
        })

# =============================================================================
# Error Handling

@app.errorhandler(400)
def bad_request(e):
    return json.dumps({
        'status': 'fail',
        'error': ['bad request'],
        'method': '',
        'result': []
    }), 400

@app.errorhandler(404)
def page_not_found(e):
    return json.dumps({
        'status': 'fail',
        'error': ['not found'],
        'method': '',
        'result': []
    }), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return json.dumps({
        'status': 'fail',
        'error': ['method not allowed'],
        'method': '',
        'result': []
    }), 405

@app.errorhandler(500)
def server_error(e):
    return json.dumps({
        'status': 'fail',
        'error': [str(e)],
        'method': '',
        'result': []
    }), 500

app.run(use_reloader=False, host='0.0.0.0', port=5000, debug=Flask)