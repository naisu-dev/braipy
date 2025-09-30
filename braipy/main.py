def conv_brail(text):
    code_point = ord(text)

    if not (0x2800 <= code_point <= 0x283f):
        raise ValuError("点字じゃない")

    offset = code_point - 0x2800

    dots = [
        (offset & 0b00000001) != 0, 
        (offset & 0b00000010) != 0, 
        (offset & 0b00000100) != 0, 
        (offset & 0b00001000) != 0, 
        (offset & 0b00010000) != 0, 
        (offset & 0b00100000) != 0, 
    ]
    
    return dots

def create_brail(dots):
    offset = 0
    if len(dots) not in [6]:
        raise ValueError("6 only")

    if dots[0]: offset |= 0b00000001
    if dots[1]: offset |= 0b00000010
    if dots[2]: offset |= 0b00000100
    if dots[3]: offset |= 0b00001000
    if dots[4]: offset |= 0b00010000
    if dots[5]: offset |= 0b00100000

    code_point = 0x2800 + offset
    return chr(code_point)

class Brail_6:
    def __init__(self, dots: list):
        self.text = create_brail(dots)
        self.dots = dots
    
    @classmethod
    def text_from(cls, btext: str):
        return cls(conv_brail(btext))

class LangModel:
    def __init__(self, file_path):
        self.file_path = file_path
        with open(file_path, "r") as f:
            self.file = f.read()

my_brail = Brail_6([1, 1, 1, 0, 0, 1])
print(my_brail.text)

