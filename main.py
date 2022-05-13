from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home_page():
    return render_template('index.html'), 200


if __name__ == "__main__":
    app.run(debug=True)
