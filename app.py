""" Flaskによる、管理者画面のコントローラー
input: 画像
output: 検出された個数を出力
"""
import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import send_from_directory
import numpy as np

import image_Recognition as ir


# Flaskオブジェクトの生成
app = Flask(__name__, static_url_path="")


@app.route("/")
def index():
    """GET
    return: index.html
    """
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    """POST
    Return:
        result.html
        count
    """
    file = request.files["uploadFile"]
    ir.imege_save(file)
    ir.convert_gray("static/images/test.jpg")

    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)


"""メモ欄
・画面でのインプットはOK
ただし、image_Recognition.pyを実行するとreturnができなくなり、結果画面まで遷移できなくなった。
※単純な画面遷移は出来た。
"""
