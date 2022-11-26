""" Flaskによる、管理者画面のcontroller
input: 画像
output: 検出された個数を出力
"""
from flask import Flask
from flask import render_template
from flask import request
import cv2
import numpy as np

import image_Recognition as ir


# Flaskオブジェクトの生成
app = Flask(__name__, static_url_path="")

# 「猫」カスケードファイルを定義する
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
    # 画面のアップロードファイルを取得
    file = request.files["uploadFile"]

    # numpyarray型に変換
    file_ndarray = np.asarray(bytearray(file.read()), dtype=np.uint8)
    file_ndarray_decode = cv2.imdecode(file_ndarray, cv2.IMREAD_COLOR)

    # オリジナル画像をDBに保存する
    original_file_path = ir.imege_save(file_ndarray_decode, file)

    # グレースケール
    img_gray = ir.convert_gray(file_ndarray_decode)

    # detect&rectangle
    result, count = ir.detect(img_gray, cascade_file, original_file_path)

    return render_template("result.html", count=count)


if __name__ == "__main__":
    app.run(debug=True)


"""メモ欄
・画面でのインプットはOK
ただし、image_Recognition.pyを実行するとreturnができなくなり、結果画面まで遷移できなくなった。
※単純な画面遷移は出来た。
"""
