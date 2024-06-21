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
