import os 

from flask import Flask


port = int(os.environ['PORT'])
app = Flask(__name__)

@app.route('/')
def index():
   return 'Hello World!!!!!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)