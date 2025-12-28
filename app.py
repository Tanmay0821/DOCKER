
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, this is my first Flask app!"

if __name__ == "__main__":
    app.run(debug=True)
