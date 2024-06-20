<div align = center><h1>このライブラリはまだ作成途中なので使用を推奨しません<br>This library is still under construction and is not recommended for use.</h1></div>

<div align = center><img src = "https://typograssy.deno.dev/api?text=Brai.py&comment=" alt = "brai.py"></div>

# Brai.py  
![GitHub License](https://img.shields.io/github/license/naisu-dev/braipy)
![GitHub Created At](https://img.shields.io/github/created-at/naisu-dev/braipy)
![GitHub forks](https://img.shields.io/github/forks/naisu-dev/braipy?style=flat)  

このライブラリを使用することで、pythonで点字を扱うことができます  
いまのところ8点点字は使用できないのでご注意ください  
> [!NOTE]
> また、このライブラリではブライユ式点字に則って  
> 左上から下に1,2,3 右上から下に4,5,6という順番で使用し  
> 出っ張っているところをTrue、平らなところをFalseで表してください  
> <b>⠫</b> &#8658; `[True, True, False, True, False, True]`
> <table><tr><td>①</td><td>④</td></tr><tr><td>②</td><td>⑤</td></tr><tr><td>③</td><td>⑥</td></tr></table>


## インストール
```bash
# 環境によって使用するコマンドを変えてください
pip install git+https://github.com/naisu-dev/braipy.git
pip3 install git+https://github.com/naisu-dev/braipy.git

```

## 使用例
```python
import braipy


## boolのリストからクラスを作成
mytenji = braipy.Tenji([True, True, False, False, True, False])
print(mytenji) # ⠓
print(mytenji.data) # [True, True, False, False, True, False]


## クラスの一部変更  0: False  1: True  2: 現在から反対の状態にする    3:現在のまま
mytenji = mytenji.push([0, 2, 2, 2, 1, 3])
print(mytenji) # ⠜
print(mytenji.data) # [False, False, True, True, True, False]


## 点字のテキストからクラスを作成
mytenji = braipy.Tenji.tenjitext_to_cls("⠇")
print(mytenji) # ⠇
print(mytenji.data) # [True, True, True, False, False, False]


## 通常のテキストからクラスのリストを作成
mytenji = braipy.Tenji.text_to_cls("helloworld", mode="traslate") #str.translateで変換
mytenji = braipy.Tenji.text_to_cls("helloworld", mode="character") #独自の方法で変換
## ２つのモードがあります　translateモードだと、辞書に無いテキストがあるとスルーしますが、characterモードだと、エラーが出ます
print(mytenji) # [⠓, ⠑, ⠇, ⠇, ⠕, ⠺, ⠕, ⠗, ⠇, ⠙]
```

# -alpha機能-
## 辞書
Braipyではオリジナルの辞書を用意しますが、独自の辞書を使用することもできます  
```python
import braipy

mydict = {
    "h": [True, True, True, True, True, True],
    "e": [True, False, False, False, True, True],
    "l": [True, False, True, False, True, True],
    "o": [False, True, False, False, True, True]
}

mytenji = braipy.Mytenji.text_to_cls("hello", mydict)
print(mytenji) # ["⠿", "⠱", "⠵", "⠵", "⠲"]  *クラスのリストが返っています
```
