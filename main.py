# - encording: utf-8 -

'''
①④
②⑤
③⑥
'''

import typing
   
class Tenji:
    tenji_list = [["1", "3", "5", "7", "9", "b", "d", "f"], ["2", "3", "6", "7", "a", "b", "e", "f"], ["8", "9", "a", "b", "c", "d", "e", "f"], ["4", "5", "6", "7", "c", "d", "e", "f"], ["1", "3"], ["2", "3"]]
    
    def __init__(self, data: typing.List[bool]):
        self.data = data
        for i in range(64):
            if self.data == tuple([True if i == "1" else False for i in list((bin(i)[2:]).zfill(6))])[::-1]:
                self.text = chr(int("28"+hex(i)[2:], 16))
                print(chr(int("28"+hex(i)[2:], 16)))
                break
    
    def __str__(self):
        return self.text
    
    def push(self, data: dict):
        pass
        
    @classmethod
    def tenjitext_to_cls(cls, text: str):
        s_16 = hex(ord(text))[2:]
        data = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False}
        if s_16[3:] in Tenji.tenji_list[0]: # 左上
            data["1"] = True
        if s_16[3:] in Tenji.tenji_list[1]: # 左中
            data["2"] = True
        if s_16[3:] in Tenji.tenji_list[2]: # 右上
            data["4"] = True
        if s_16[3:] in Tenji.tenji_list[3]: # 左下
            data["3"] = True
        if s_16[2:3] in Tenji.tenji_list[4]: # 右中
            data["5"] = True
        if s_16[2:3] in Tenji.tenji_list[5]: # 右下
            data["6"] = True
        return cls(list(data.values()))
    
# print(Tenji.tenjitext_to_cls("⠼").data)
mytenji = [True, True, False, False, False, True]
print(mytenji)
