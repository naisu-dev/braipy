def conv_brail(text):
    code_point = ord(text)
    if not (0x2800 <= code_point <= 0x283f):
        raise ValueError("点字じゃない")
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
    
    def __repr__(self):
        return self.text

    def __add__(self, other):
        if isinstance(other, Brail_6):
            return BrailString([self, other])
        elif isinstance(other, BrailString):
            return BrailString([self] + other.brail_list)
        else:
            return NotImplemented

class BrailString:
    def __init__(self, brail_list):
        self.brail_list = brail_list

    @classmethod
    def from_btext(cls, btext: str):
        brail_list = [Brail_6.text_from(char) for char in btext]
        return cls(brail_list)

    def __repr__(self):
        return "".join(brail.text for brail in self.brail_list)

    def __iter__(self):
        return iter(self.brail_list)

    def __len__(self):
        return len(self.brail_list)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return BrailString(self.brail_list[index])
        return self.brail_list[index]
    
    def __add__(self, other):
        if isinstance(other, BrailString):
            new_brail_list = self.brail_list + other.brail_list
            return BrailString(new_brail_list)
        elif isinstance(other, Brail_6):
            new_brail_list = self.brail_list + [other]
            return BrailString(new_brail_list)
        else:
            return NotImplemented
    
    def __radd__(self, other):
        if isinstance(other, Brail_6):
            return BrailString([other] + self.brail_list)
        else:
            return NotImplemented
