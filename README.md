# ImageTrim
## 使い方
beforeフォルダの画像をafterフォルダにコピーし黒枠のトリミングをします。
![image](https://user-images.githubusercontent.com/79146720/121325917-fe88ae80-c94c-11eb-8cc1-8352adf154af.png)
![image](https://user-images.githubusercontent.com/79146720/121325932-021c3580-c94d-11eb-8308-6226bfcab44b.png)

## 注意点
### トリミング元、トリミング先のパスを変更したい場合はBEFORE_IMAGE_PATH、AFTER_IMAGE_PATHを修正します。
![image](https://user-images.githubusercontent.com/79146720/121326093-3132a700-c94d-11eb-9d7e-d8ba9561a055.png)
### X座標0の列とY座標0の行の色が黒かで判断しているのでその中に黒(RGB値0,0,0)が含まれていると適切にトリミングできません。
![image](https://user-images.githubusercontent.com/79146720/121327396-5f64b680-c94e-11eb-953d-7bcbb9f208ab.png)
![image](https://user-images.githubusercontent.com/79146720/121327294-4a882300-c94e-11eb-92ce-893a285707cb.png)

以上です。
