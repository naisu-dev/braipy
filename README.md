<div align = center><img src = "https://typograssy.deno.dev/api?text=Brai.py&comment=" alt = "brai.py"></div>

# Brai.py  
[![braipy](https://github.com/naisu-dev/braipy/actions/workflows/blank.yml/badge.svg?branch=main)](https://github.com/naisu-dev/braipy/actions/workflows/blank.yml)
![GitHub License](https://img.shields.io/github/license/naisu-dev/braipy)
![GitHub Created At](https://img.shields.io/github/created-at/naisu-dev/braipy)
![GitHub forks](https://img.shields.io/github/forks/naisu-dev/braipy?style=flat)
[![Email](https://img.shields.io/badge/email-naisudevcontact@gmail.com-blue.svg?style=flat)](mailto:naisudevcontact@gmail.com)  

This library allows you to work with braille in python! 
8 braille is not available at this time. 
> [!NOTE]
> Also, in this library, in accordance with the style of Braille.  
> From upper left to upper right: 1,2,3, and from upper right to lower right: 4,5,6. 
> The protruding part is denoted by "true" and the flat part by "false. 
> <b>⠫</b> &#8658; `[True, True, False, True, False, True]`
> <table><tr><td>①</td><td>④</td></tr><tr><td>②</td><td>⑤</td></tr><tr><td>③</td><td>⑥</td></tr></table>


## Install
```bash
# Use different commands depending on the environment
pip install git+https://github.com/naisu-dev/braipy.git
pip3 install git+https://github.com/naisu-dev/braipy.git

```

## Example of use
```python
import braipy


## Create a class from a list of bools
mytenji = braipy.Tenji([True, True, False, False, True, False])
print(mytenji) # ⠓
print(mytenji.data) # [True, True, False, False, True, False]


## Some class changes  0: False  1: True  2: To the opposite state from the present    3:as it is now
mytenji = mytenji.push([0, 2, 2, 2, 1, 3])
print(mytenji) # ⠜
print(mytenji.data) # [False, False, True, True, True, False]


## Create classes from Braille text
mytenji = braipy.Tenji.tenjitext_to_cls("⠇")
print(mytenji) # ⠇
print(mytenji.data) # [True, True, True, False, False, False]


## Create a list of classes from normal text
mytenji = braipy.Tenji.text_to_cls("helloworld", mode="translate") #Transformation with str.translate
mytenji = braipy.Tenji.text_to_cls("helloworld", mode="character") #Convert in your own way
## There are two modes. In translate mode, if there is text that is not in the dictionary, it will go through, but in character mode, an error will occur.
print(mytenji) # [⠓, ⠑, ⠇, ⠇, ⠕, ⠺, ⠕, ⠗, ⠇, ⠙]
```

# -Alpha function-
## Dictionary
Braipy will provide you with an original dictionary, but you can also use your own dictionary  
```python
import braipy

mydict = {
    "h": [True, True, True, True, True, True],
    "e": [True, False, False, False, True, True],
    "l": [True, False, True, False, True, True],
    "o": [False, True, False, False, True, True]
}

mytenji = braipy.Mytenji.text_to_cls("hello", mydict)
print(mytenji) # ["⠿", "⠱", "⠵", "⠵", "⠲"]  *A list of classes is returned
```

### This readme was translated from Japanese to English using deepl translation, so there may be some grammar errors.
