""" Flaskによる、管理者画面のコントローラー
input: 画像
output: 検出された個数を出力
"""
from flask import Flask
from flask import render_template
from flask import request
import cv2

import image_Recognition as ir


# Flaskオブジェクトの生成
app = Flask(__name__, static_url_path="")

# 一旦「猫」限定でカスケードファイルを定義する
cascade_file = "haarcascade_frontalcatface_extended.xml"


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
        count: 検出結果の個数
    """
    file = request.files["uploadFile"]
    ir.imege_save(file)
    ir.convert_gray("static/images/test.jpg")
    result, count = ir.detect("static/images/test_gray.jpg", cascade_file)
    cv2.imwrite("static/images/test_gray_rectangle.jpg", result)

    return render_template("result.html", count=count)


if __name__ == "__main__":
    app.run(debug=True)


"""メモ欄
・画面でのインプットはOK
ただし、image_Recognition.pyを実行するとreturnができなくなり、結果画面まで遷移できなくなった。
※単純な画面遷移は出来た。
"""
