from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"


def runserver():
    app.run()
