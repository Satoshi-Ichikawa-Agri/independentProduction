""" Flaskによる、管理者画面のコントローラー
input: 画像
output: 検出された個数を出力
"""
from flask import Flask
from flask import render_template
from flask import request

import image_Recognition as ir


# Flaskオブジェクトの生成
app = Flask(__name__)


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
    file = str(file)
    result, count = ir.main(file)

    return render_template("result.html", count=count)


if __name__ == "__main__":
    app.run(debug=True)


"""メモ欄
・画面でのインプットはOK
ただし、image_Recognition.pyを実行するとreturnができなくなり、結果画面まで遷移できなくなった。
※単純な画面遷移は出来た。
"""
