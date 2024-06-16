<div align = center><img src = "https://typograssy.deno.dev/api?text=Brai.py&comment=" alt = "brai.py"></div>

# Brai.py  
![GitHub License](https://img.shields.io/github/license/naisu-dev/braipy)
![GitHub Created At](https://img.shields.io/github/created-at/naisu-dev/braipy)  
このライブラリを使用することで、pythonで点字を扱うことができます  
いまのところ8点点字は使用できないのでご注意ください  
> [!NOTE]
> また、このライブラリではブライユ式点字に則って、  
> 左上から下に1,2,3 右上から下に4,5,6
> という順番で使用してください
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

mytenji = braipy.Tenji([True, True, False, False, True, False])
print(mytenji)
print(mytenji.data)
# ⠓
# [True, True, False, False, True, False]

mytenji = mytenji.push([2, 2, 2, 2, 1, 0])
print(mytenji)
print(mytenji.data)
# ⠜
# [False, False, True, True, True, False]
```
