"""特定物体の識別処理

"""
import sys
import cv2
import numpy as np


def detect(imagefile_name, cascadefile_name):
    """ 分類器と画像を指定し、特定の物体を検知する
    Param: 
        imagefile_name: 対象となる静止画
        cascadefile_name: 静止画内の物体に合わせたカスケードファイル
    Return:
        dstimg: 検出しレクタングルされた静止画
    """
    # 指定されたファイルを読み込む
    img = cv2.imread(imagefile_name)

    # 読み込んだ画像が空の時、処理を終了する
    if img is None:
        print('cannot load image')
        sys.exit(-1)
    
    # 画像オブジェクトのコピー(元画像の更新を防ぐ)
    dstimg = img.copy()
    dstimg = cv2.cvtColor(dstimg,cv2.COLOR_BGR2GRAY)

    # 分類器の準備(公式で配布しているファイルを引用)
    cascade = cv2.CascadeClassifier(cascadefile_name)

    # 分類器が空の時、処理を終了する
    if cascade.empty():
        print('cannnot load cascade file')
        sys.exit(-1)
    
    # 分類器で画像を処理する
    objects = cascade.detectMultiScale(img, 1.03, 3)
    # print(objects)

    for (x, y, w, h) in objects:
        # print(x, y, w, h)
        cv2.rectangle(dstimg, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return dstimg

def count(img):
    #輪郭抽出
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #輪郭の個数を表示
    print(len(contours))


if __name__ == '__main__':
    # result = detect('images/cat2.jpg', 'haarcascade_frontalcatface.xml')
    result2 = detect('images/cat2.jpg', 'haarcascade_frontalcatface_extended.xml')
    # cv2.imwrite('images/result.jpg', result)
    cv2.imwrite('images/result2.jpg', result2)

    count(result2)

"""メモ欄
・猫のカスケードファイルは『haarcascade_frontalcatface_extended.xml』を採用する。
・detectMultiScaleの引数「scalefactor」は"1.03"を採用

実行中→検出したオブジェクトの個数を取り出す
"""





