import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Home"

@app.route('/_ah/warmup')
def warmup():
        return ''
