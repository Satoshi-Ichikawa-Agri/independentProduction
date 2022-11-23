""" 画像
"""

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect


# Flaskオブジェクトの生成
app = Flask(__name__)


@app.route("/")
def index():
    """ GET
    return: index.html
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
