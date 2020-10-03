# DeepHazerd
Hazerd Map Prediction by Deep Learning

## 環境設定
## pip installl
```
pip install -r requirements.txt
```
## API キーの準備
ライブラリをインストールあとに
```
earthengine authenticate
```
 
各種root ディレクトリ（このreadmeがあるディレクトリ）に```api_keys.json```という名前で以下のJSON ファイルを作ってください。（安全のためgitignoreされています）
```api_keys.json```
```
{
    "hogehoge-api" : <your token>,
   }
```
