# Brai.py
このライブラリを使用することで、pythonで点字を扱うことができます  
いまのところ8点点字は使用できないのでご注意ください  
また、このライブラリではブライユ式点字に則って  
①④  
②⑤  
③⑥  
という順番で使用してください

## インストール
```bash
# 環境によって使用するコマンドを変えてください
pip install git+https://github.com/naisu-dev/braipy.git
pip3 install git+https://github.com/naisu-dev/braipy.git

```

## 使用例
```python
import braipy

mytenji = braipy.Tenji([True, True, False, False, True, False])
print(mytenji) # ⠓
print(mytenji.data) # [True, True, False, False, True, False]

mytenji = mytenji.push([2, 2, 2, 2, 1, 0])
print(mytenji) # ⠜
print(mytenji.data) # [False, False, True, True, True, False]
```
