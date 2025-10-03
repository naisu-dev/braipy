import json

class Brail_6:
    def __init__(self, binary: str):
        if len(binary) != 6:
            raise ValueError("Binary string must be 6 characters long.")
        dots = [char == '1' for char in binary]
        self.text = self._dots_to_btext(dots)
        self.dots = dots

    @classmethod
    def from_dots(cls, dots: list):
        binary = "".join(["1" if dot else "0" for dot in dots])
        return cls(binary)

    @classmethod
    def from_btext(cls, btext: str):
        dots = cls._btext_to_dots(btext)
        return cls.from_dots(dots)

    def __repr__(self):
        return self.text

    def __add__(self, other):
        if isinstance(other, Brail_6):
            return BrailString([self, other])
        elif isinstance(other, BrailString):
            return BrailString([self] + other.brail_list)
        else:
            return NotImplemented

    @staticmethod
    def _btext_to_dots(btext):
        code_point = ord(btext)
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

    @staticmethod
    def _dots_to_btext(dots):
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

class BrailString:
    def __init__(self, brail_list):
        self.brail_list = brail_list

    @classmethod
    def from_btext(cls, btext: str):
        brail_list = [Brail_6.from_btext(char) for char in btext]
        return cls(brail_list)
    
    @classmethod
    def from_binary(cls, binary_string: str):
        binary_codes = binary_string.split()
        brail_list = [Brail_6(code) for code in binary_codes]
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

    def translate(self, lang: "Lang"):
        brail_dots_list = [brail.dots for brail in self.brail_list]
        result = ""
        i = 0
        while i < len(brail_dots_list):
            found_char, consumed = self._find_character(brail_dots_list[i:], lang.data)

            if found_char:
                result += found_char
                i += consumed
            else:
                result += "-"
                i += 1
        return result

    def _find_character(self, codes, lang_dict):
        if not codes:
            return None, 0

        binary = "".join(["1" if dot else "0" for dot in codes[0]])
        
        if binary not in lang_dict:
            return None, 0
        
        value = lang_dict[binary]
        
        if isinstance(value, dict):
            found_char, consumed_count = self._find_character(codes[1:], value)
            if found_char:
                return found_char, consumed_count + 1
            else:
                return None, 0
        else:
            return value, 1

class Lang:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as f:
            self.data = json.load(f)

if __name__ == "__main__":
    Japanese = Lang("ja.json")
    mybrail = BrailString.from_binary("000010 011101 010000 111010")
    print(mybrail)
    decoded_text = mybrail.translate(Japanese)
    print(decoded_text)
