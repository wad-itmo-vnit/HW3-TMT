from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run(host="localhost", port=5000)