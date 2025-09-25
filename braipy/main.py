from enum import IntEnum

def conv_brail(text):
    code_point = ord(text)

    if not (0x2800 <= code_point <= 0x28FF):
        raise ValuError("点字じゃない")

    offset = code_point - 0x2800

    dots = [
        (offset & 0b00000001) != 0,  # 点1
        (offset & 0b00000010) != 0,  # 点2
        (offset & 0b00000100) != 0,  # 点3
        (offset & 0b00001000) != 0,  # 点4
        (offset & 0b00010000) != 0,  # 点5
        (offset & 0b00100000) != 0,  # 点6
    ]

    if code_point >= 0x2840:
        dots.append((offset & 0b01000000) != 0)  # 点7
        dots.append((offset & 0b10000000) != 0)  # 点8

    elif code_point >= 0x2800:
        pass 
    return dots

def create_brail(dots):
    offset = 0
    if len(dots) not in [6, 8]:
        raise ValueError("6 or 8 only")

    if dots[0]: offset |= 0b00000001
    if dots[1]: offset |= 0b00000010
    if dots[2]: offset |= 0b00000100
    if dots[3]: offset |= 0b00001000
    if dots[4]: offset |= 0b00010000
    if dots[5]: offset |= 0b00100000

    if len(dots) == 8:
        if dots[6]: offset |= 0b01000000
        if dots[7]: offset |= 0b10000000

    code_point = 0x2800 + offset
    return chr(code_point)

class brailtype(IntEnum):
    six = 6
    eight = 8


class Brail:
    def __init__(self, btext: str):
        self.text = btext
        self.dots = conv_brail(btext)
        self.type = brailtype(len(self.dots)) # ここのtypeは形式的なものです！
    
    @classmethod
    def dots_from(cls, dots: list[bool]):
        return cls(create_brail(dots))
