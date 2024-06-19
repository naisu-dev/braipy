import typing
from .tenjidataset import data as transdata


class Tenji:
    tenji_list = [["1", "3", "5", "7", "9", "b", "d", "f"], ["2", "3", "6", "7", "a", "b", "e", "f"], ["8", "9", "a", "b", "c", "d", "e", "f"], ["4", "5", "6", "7", "c", "d", "e", "f"], ["1", "3"], ["2", "3"]]

    def __init__(self, data: typing.List[bool]):
        if len(data) != 6:
            raise ValueError("Incorrect number of elements")
        else:
            self.data = data
            for i in range(64):
                if self.data == (list([
                        True if i == "1" else False
                        for i in list((bin(i)[2:]).zfill(6))
                ])[::-1]):
                    self.text = chr(int("28" + (hex(i)[2:]).zfill(2), 16))
                    break

    def __repr__(self):
        return self.text

    def push(self, data: typing.List[int] = [2, 2, 2, 2, 2, 2]):
        org_data = self.data
        if len(data) != 6:
            raise ValueError("Incorrect number of elements")
        else:
            for i in range(6):
                if data[i] == 0:
                    org_data[i] = False
                elif data[i] == 1:
                    org_data[i] = True
                elif data[i] == 2:
                    if org_data[i] == True:
                        org_data[i] = False
                    else:
                        org_data[i] = True
                elif data[i] == 3:
                    pass
                else:
                    raise ValueError("Incorrect value range.")
        return Tenji(org_data)

    def translate(self, lang):
        # クラスから文字になおす関数
        pass

    @classmethod
    def tenjitext_to_cls(cls, text: str):
        s_16 = hex(ord(text))[2:]
        data = {"1": False, "2": False, "3": False, "4": False, "5": False, "6": False}
        if s_16[3:] in Tenji.tenji_list[0]:  # upper left
            data["1"] = True
        if s_16[3:] in Tenji.tenji_list[1]:  # center left
            data["2"] = True
        if s_16[3:] in Tenji.tenji_list[2]:  # upper right
            data["4"] = True
        if s_16[3:] in Tenji.tenji_list[3]:  # lower left
            data["3"] = True
        if s_16[2:3] in Tenji.tenji_list[4]:  # center right
            data["5"] = True
        if s_16[2:3] in Tenji.tenji_list[5]:  # lower right
            data["6"] = True
        return cls(list(data.values()))

    @classmethod
    def text_to_cls(cls, text: str, *, mode: str = "translate", tenjidict: dict = transdata):
        # character or translate
        if mode == "translate":
            for i in tenjidict.keys():
                tenjidict[i] = Tenji(tenjidict[i]).text
            return text.translate(str.maketrans(tenjidict))
        elif mode == "character":
            pass
        else:
            raise ValueError('Either "translate" or "character".')
