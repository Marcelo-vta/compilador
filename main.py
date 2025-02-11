import sys

def calc(entry):
    entry_cut = [k for k in entry.split(" ") if len(k)]
    sequence = {
        "+": ["num"],
        "-": ["num"],
        "num": ["num", "+", "-"],
        "numspace": ["+", "-"],
    }
    if not entry_cut[0][0].isnumeric() or not entry_cut[-1][0].isnumeric():
        return (False, 0)

    last_type = "start" 
    result = int(entry_cut[0])

    for chars in entry_cut:
        if last_type == "num":
            last_type = "numspace"
        for char in chars:
            if char.isnumeric():
                current_type = "num"
            elif char in ["+", "-"]:
                current_type = char
            else:
                return (False, 0)
            if last_type != "start":
                if current_type in sequence[last_type]:
                    if current_type == "num":
                        if last_type == "-":
                            result -= int(char)
                        if last_type == "+":
                            result += int(char)
                else:
                    return (False, 0)
            last_type = current_type
    return (True, result)

if __name__ == "__main__":
    input = sys.argv[1]
    print(calc(input))
    
            

            










