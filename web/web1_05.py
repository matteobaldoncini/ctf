import flask

app = flask.Flask(__name__)

@app.route("/")

def redir():
    return flask.redirect("http://localhost/get_flag.php")


@app.route("/sec/")
def second():
    return "<h1>Hello World</h1>"
