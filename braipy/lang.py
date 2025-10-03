import json

class Lang:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as f:
            self.data = json.load(f)
    
    def find_character(self, codes, lang_dict):
        if not codes or codes[0] not in lang_dict:
            return None, 0
        
        current_code = codes[0]
        value = lang_dict[current_code]
        
        if isinstance(value, dict):
            found_char, consumed_count = self.find_character(codes[1:], value)
            if found_char:
                return found_char, consumed_count + 1
            else:
                return None, 0
        
        else:
            return value, 1
    
    
    def decode_message_recursive(self, text, error_m=" "):
        data = text.split(" ")
        result = ""
        i = 0
        while i < len(data):
            found_char, consumed = self.find_character(data[i:], self.data)
            
            if found_char:
                result += found_char
                i += consumed
            else:
                result += error_m
                i += 1
                
        return result

if __name__ == "__main__":
    Japanese = Lang("ja.json")
    test_text = "100000 110000 000011 100001 000010 010011"
    decoded_text = Japanese.decode_message_recursive(test_text)
    print(decoded_text)
