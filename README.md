# ImageTrim
## 使い方
beforeフォルダの画像をafterフォルダにコピーし黒枠のトリミングをします。
![image](https://user-images.githubusercontent.com/79146720/121325917-fe88ae80-c94c-11eb-8cc1-8352adf154af.png)
![image](https://user-images.githubusercontent.com/79146720/121325932-021c3580-c94d-11eb-8308-6226bfcab44b.png)

## 処理
1.画像を別フォルダにコピーする(バックアップ処理)
2.コピー画像をクレースケールにする
3.画像のグレースケール値が0（黒色）の座標を取得する
4.3で取得した座標を元にトリミング処理をする

## 注意点
### トリミング元、トリミング先のパスを変更したい場合はBEFORE_IMAGE_PATH、AFTER_IMAGE_PATHを修正します。
![image](https://user-images.githubusercontent.com/79146720/121326093-3132a700-c94d-11eb-9d7e-d8ba9561a055.png)
### X座標0の列とY座標0の行の色が黒かで判断しているのでその中に黒(RGB値0,0,0)が含まれていると適切にトリミングできません。
![image](https://user-images.githubusercontent.com/79146720/121327396-5f64b680-c94e-11eb-953d-7bcbb9f208ab.png)
![image](https://user-images.githubusercontent.com/79146720/121327294-4a882300-c94e-11eb-92ce-893a285707cb.png)

## 参考資料
### Python, Pillowで画像の一部をトリミング（切り出し/切り抜き）
https://note.nkmk.me/python-pillow-image-crop-trimming/
### [Python]ファイル/ディレクトリ操作
https://qiita.com/supersaiakujin/items/12451cd2b8315fe7d054
### PythonのPILのgetpixel関数の使い方を現役エンジニアが解説【初心者向け】
https://techacademy.jp/magazine/28381
### cv2.imreadがNoneを返す・cv2.imwriteがエラーを吐く
https://anton0825.hatenablog.com/entry/2018/02/12/000000
### Python でグレースケール(grayscale)化
https://qiita.com/yoya/items/dba7c40b31f832e9bc2a
### PythonにおけるOpenCVのインストール方法について現役エンジニアが解説【初心者向け】
https://techacademy.jp/magazine/51404
### 【Python】画像の切り出し方法【OpenCV】
https://qiita.com/ikanamazu/items/d752225a0a9834ce0d41

以上です。
