from flask import Flask, render_template, request, Response

app = Flask(__name__)

# Basic Auth Credentials
USERNAME = 'Dinesh'
PASSWORD = 'Dineshs_2002'  
def check_auth(username, password):
    return username == USERNAME and password == PASSWORD

def authenticate():
    return Response(
        'Could not verify your login. Login required.', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'}
    )

@app.before_request
def require_auth():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        return authenticate()

@app.route('/')
def index():
    return render_template('index.html')
