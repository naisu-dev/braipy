# 参考： https://ja.wikipedia.org/wiki/英語の点字

data = {
    "a": [1, 0, 0, 0, 0, 0],
    "b": [1, 1, 0, 0, 0, 0],
    "c": [1, 0, 0, 1, 0, 0],
    "d": [1, 0, 0, 1, 1, 0],
    "e": [1, 0, 0, 0, 1, 0],
    "f": [1, 1, 0, 1, 0, 0],
    "g": [1, 1, 0, 1, 1, 0],
    "h": [1, 1, 0, 0, 1, 0],
    "i": [0, 1, 0, 1, 0 ,0],
    "j": [0, 1, 0, 1, 1, 0],
    "k": [1, 0, 1, 0, 0, 0],
    "l": [1, 1, 1, 0, 0, 0],
    "m": [1, 0, 1, 1, 0, 0],
    "n": [1, 0, 1 ,1 ,1, 0],
    "o": [1, 0, 1, 0, 1, 0],
    "p": [1, 1, 1, 1, 0, 0],
    "q": [1, 1, 1, 1, 1, 0],
    "r": [1, 1, 1, 0, 1, 0],
    "s": [0, 1, 1, 1, 0, 0],
    "t": [0, 1, 1, 1, 1, 0],
    "u": [1, 0, 1, 0, 0, 1],
    "v": [1, 1, 1, 0, 0, 1],
    "w": [0, 1, 0, 1, 1, 1],
    "x": [1, 0, 1, 1, 0, 1],
    "y": [1, 0, 1, 1, 1, 1],
    "z": [1, 0, 1, 0, 1, 1],
    ",": [0, 1, 0, 0, 0, 0],
    ";": [0, 1, 1, 0, 0, 0],
    ":": [0, 1, 0, 0, 1, 0],
    ".": [0, 1, 0, 0, 1, 1],
    "!": [0, 1, 1, 0, 1, 0],
    "(": [0, 1, 1, 0, 1, 1],
    ")": [0, 1, 1, 0, 1, 1],
    "?": [0, 1, 1, 0, 0, 1],
    "\"": [0, 1, 1, 0, 0, 1],
    "*": [0, 0, 1, 0, 1, 0],
    
}

for i in range(len(data)):
    for i_2 in range(6):
        data[list(data.keys())[i]][i_2] = bool(data[list(data.keys())[i]][i_2])

def en():
    return data
