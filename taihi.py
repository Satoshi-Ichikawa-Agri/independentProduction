"""個体の識別をする
"""
import cv2
import face_recognition
import numpy as np
from PIL import Image


deactivate
def find_face():
    """ 物体を検出する関数
    カスケード分類器とは、、、
    物体検出を行うためには検出したい物体がどんな特徴を持っているのか、
    該当する物体を含む画像と含まない画像（＝学習用画像）を用意し、検出したい物体の特徴を抽出します。
    この特徴を「特徴量」と呼びますが、学習用画像すべての「特徴量」をまとめたデータのことを
    「カスケード分類器」と呼びます。
    """
    # カスケードファイルを指定して、分類機を作成
    cascade_file = "haarcascade_eye.xml"
    cascade = cv2.CascadeClassifier(cascade_file)
    # 画像を読み込み、グレイスケール(白黒)に変換
    img = cv2.imread(original_woman_image)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 顔検出
    face_list = cascade.detectMultiScale(img_gray)

    return face_list














# # 動画を読み込む
# cap = cv2.VideoCapture(0)

# # 動画ファイル保存用の設定
# # カメラのFPSを取得
# fps = int(cap.get(cv2.CAP_PROP_FPS))  
# # カメラの横幅を取得
# w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
# # カメラの縦幅を取得
# h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  
# # 動画保存時のfourcc設定(mp4用)
# fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v") 
# # 動画の仕様(ファイル名、fourcc, FPS, サイズ)
# video = cv2.VideoWriter(
#     "images/video.mp4", fourcc, fps, (w, h)
# )  


# while True:
#     ret, frame = cap.read()
#     if ret is False:
#         break
#     cv2.imshow("Image", frame)
#     video.write(frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
# cap.release()


# cv2.imshow("Image", frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
