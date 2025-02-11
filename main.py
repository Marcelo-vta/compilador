import sys

def calc(entry):
    entry_cut = "".join([char if char.isnumeric() else f" {char} " for char in entry]).split(" ")
    n_ops = [e for e in entry_cut if len(e)]

    sequence = {
        "+": ["num"],
        "-": ["num"],
        "num": ["+", "-"],
    }
    if not n_ops[0].isnumeric() or not n_ops[-1].isnumeric():
        return (False, 0)

    last_type = "start" 
    result = int(n_ops[0])

    for element in n_ops:

        if element.isnumeric():
            current_type = "num"
        elif element in ["+", "-"]:
            current_type = element
        else:
            return (False, 0)
        
        if last_type != "start":
            if current_type in sequence[last_type]:
                if current_type == "num":
                    if last_type == "+":
                        result += int(element)
                    if last_type == "-":
                        result -= int(element)
            else:
                return (False, 0)
            
        last_type = current_type

    return (True, result)

if __name__ == "__main__":
    input = sys.argv[1]
    if not calc(input)[0]:
        raise Exception("Input invalido")
    print(calc(input)[1])
    
            

            










