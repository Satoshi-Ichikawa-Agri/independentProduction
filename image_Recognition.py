""" 特定物体の識別処理
"""
import sys
import cv2
from PIL import Image


def imege_save(upload_img):
    """Web上からアップロードされた画像ファイルを保存する
    Pillowで実装する。
    Param:
        upload_img:
    """
    img = Image.open(upload_img)

    while True:
        if img is None or img == "":
            break
        else:
            i = 1
            img.save("static/images/test" + str(i) + ".jpg")
            i += 1


def convert_gray(imagefile):
    """画像のグレー変換
    Param:
        imagefile: グレーに変換したい画像のパス
    """
    # 指定されたファイルを読み込む
    img = cv2.imread(imagefile)
    # 読み込んだ画像が空の時、処理を終了する
    if img is None:
        print("cannot load image")
        sys.exit(-1)
    # グレーに変える
    copy_img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # グレー変換した画像を保存する
    cv2.imwrite("static/images/test_gray.jpg", copy_img_gray)


def detect(image_file, cascade_file_name):
    """分類器と画像を指定し、特定の物体を検知する
    Param:
        imagefile_name: 対象となる静止画
        cascadefile_name: 静止画内の物体に合わせたカスケードファイル
    Return:
        copy_img_gray: 検出しレクタングルされた静止画
        number_of_individuals: 検出した個体数
    """
    img = cv2.imread(image_file)

    # 分類器の準備
    cascade = cv2.CascadeClassifier(cascade_file_name)

    # 分類器が空の時、処理を終了する
    if cascade.empty():
        print("cannnot load cascade file")
        sys.exit(-1)

    # 分類器で画像を処理する
    detected_results = cascade.detectMultiScale(img, 1.02, 3)

    # 検出したList数をカウントし、個体数として取り出す
    number_of_individuals = len(detected_results)

    # 分類器で検出した結果を取り出し、画像のrectangle加工を施す
    for (x, y, w, h) in detected_results:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow("rectangle", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return img, number_of_individuals


if __name__ == "__main__":
    detect()

"""メモ欄
・猫のカスケードファイルは『haarcascade_frontalcatface_extended.xml』を採用する。
・detectMultiScaleの引数「scalefactor」は"1.02"を採用
"""

"""detectMultiScale()の引数メモ
第1引数image: CV_8U 型の行列。ここに格納されている画像の中から物体が検出される
第2引数objects: 矩形を要素とするベクトル．それぞれの矩形は，検出した物体を含む
第3引数scaleFactor: 各画像スケールにおける縮小量を表す
第4引数minNeighbors: 物体候補となる矩形は，最低でもこの数だけの近傍矩形を含む必要がある
第5引数flags: このパラメータは，新しいカスケードでは利用されない。
第6引数minSize: 物体が取り得る最小サイズ．これよりも小さい物体は無視される。
"""

"""cv2.rectangle()の引数メモ
第1引数img: 対象の画像データ。Ndarray 型で指定。
第2引数pt1: 長方形の左上頂点の座標。(int型, int型)のtuple型で指定。
第3引数pt2: 長方形の右下頂点の座標。(int型, int型)のtupleで指定。
第4引数color: 線の色。(int型, int型, int型)のtupleで指定。
第5引数thickness: 線の太さ。int型で指定。
第6引数lineType: アルゴリズムの種類。OpenCVの独自コードで指定。
第7引数shift: ビット数。int型で指定。デフォルト引数。
"""
