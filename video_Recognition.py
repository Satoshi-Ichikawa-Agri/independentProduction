"""内臓カメラで個体の識別をする
"""
import cv2


# 動画を読み込む
cap = cv2.VideoCapture(0)

# 動画ファイル保存用の設定
# カメラのFPSを取得
fps = int(cap.get(cv2.CAP_PROP_FPS))  
# カメラの横幅を取得
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  
# カメラの縦幅を取得
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  
# 動画保存時のfourcc設定(mp4用)
fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v") 
# 動画の仕様(ファイル名、fourcc, FPS, サイズ)
video = cv2.VideoWriter(
    "images/video.mp4", fourcc, fps, (w, h)
)  


while True:
    ret, frame = cap.read()
    if ret is False:
        break
    cv2.imshow("Image", frame)
    video.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()


cv2.imshow("Image", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
