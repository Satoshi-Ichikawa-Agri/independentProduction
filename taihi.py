""" かずまさんのレビュー結果
アドバイスあり
"""

def detect(imagefile_name, cascadefile_name):
    """ 分類器と画像を指定し、特定の物体を検知する
    Param: 
        imagefile_name: 対象となる静止画
        cascadefile_name: 静止画内の物体に合わせたカスケードファイル
    Return:
        dstimg: 検出しレクタングルされた静止画
    """
    outpath = "images/result.png"
    
    # 指定されたファイルを読み込む
    img = cv2.imread(imagefile_name)

    # 読み込んだ画像が空の時、処理を終了する
    if img is None:
        print('cannot load image')
        sys.exit(-1)
    
    # 画像オブジェクトのコピー(元画像の更新を防ぐ)
    dstimg = img.copy()
    dstimg = cv2.cvtColor(dstimg, cv2.COLOR_BGR2GRAY)

    # 分類器の準備(公式で配布しているファイルを引用)
    cascade = cv2.CascadeClassifier(cascadefile_name)

    # 分類器が空の時、処理を終了する
    if cascade.empty():
        print('cannnot load cascade file')
        sys.exit(-1)
    
    # 分類器で画像を処理する
    objects = cascade.detectMultiScale(img, 1.03, 3)
    count = len(objects)

    for (x, y, w, h) in objects:
        # print(x, y, w, h)
        cv2.rectangle(dstimg, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
    cv2.imwrite(outpath, dstimg)
    
    return outpath, count

if __name__ == '__main__':
    outpath, count = detect('images/cat2.jpg', 'cascade.xml')
    outpath = cv2.imread(outpath)
    print(count)
    cv2.imshow("", outpath)
    cv2.waitKey()
    cv2.destroyAllWindows()
