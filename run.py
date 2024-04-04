import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello,</h1> <h2>world!</h2>"

if __name__ == "__main__":
    app.run(
        host=os.environ.get("port", "0.0.0.0"),
        port=int(os.environ.get("port", "5000")),
        debug=True)
