# Braipy

Braipy は、**Pythonで点字を扱うためのライブラリ**です。  
6点式点字のエンコード・デコード、文字列変換、言語ごとの変換ロジックなどをサポートしています。

## 点字の並び順
点字は以下のように並んでいます：  
①④  
②⑤  
③⑥

## 主な機能

- **Brail_6 クラス**：6点式点字1文字を表し、バイナリ・点のリスト・点字文字（Unicode）から生成可能
- **BrailString クラス**：点字文字列の表現、テキスト⇔点字変換・連結・スライス・デコードなど
- **Lang クラス**：言語(例:日本語)ごとの点字辞書の取り扱い。JSON形式で定義
- **エンコード/デコード**：テキストから点字への変換、点字からテキストへの復号

```python
from braipy import Brail_6, BrailString, Lang

# 言語データのロード（例:日本語）
japanese = Lang("ja.json") 

# テキストを点字バイナリへ変換
binary = BrailString.encode("ないす", japanese)
print(binary) # -> "101000 110000 100111"

# 点字バイナリから BrailString オブジェクト生成
mybrail = BrailString.from_binary(binary)
print(mybrail) # -> "⠅⠃⠹"

# 点字を可読テキストへデコード
decoded_text = mybrail.translate(japanese)
print(decoded_text)  # "ないす"
```

## ライセンス

MIT License

## 貢献・連絡

Issue や Pull Request 大歓迎です！  
質問や要望があれば GitHub Issue へどうぞ。

---

**Braipy** は、Python で点字処理をしたい方におすすめのライブラリです。
