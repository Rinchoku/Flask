import os 

from markupsafe import escape
from flask import Flask


port = int(os.environ['PORT'])
app = Flask(__name__)

@app.route('/')
def index():
   return 'Hello World!!!!!!'

@app.route('/demo/variables/all/<user_id>')
def demoAll(user_id):
    return f'<h1>Demo</h1><p>{escape(user_id)}</p>'

@app.route('/demo/variables/string/<string:user_id>')
def demoString(user_id):
    return f'<h1>Demo</h1><p>{escape(user_id)}</p>'

@app.route('/demo/variables/int/<int:user_id>')
def demoInt(user_id):
    return f'<h1>Demo</h1><p>{escape(user_id)}</p>'

@app.route('/demo/variables/path/<path:user_id>')
def demoPath(user_id):
    return f'<h1>Demo</h1><p>{escape(user_id)}</p>'

@app.route('/demo/variables/uuid/<uuid:user_id>')
def demoUUID(user_id):
    return f'<h1>Demo</h1><p>{escape(user_id)}</p>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)