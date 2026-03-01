ASCII_CHARACTERS = [
    " ",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",    
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "-",
    "=",
    "!",
    "@",
    "£",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "+",
    "[",
    "]",
    ";",
    "'",
    "\n",
    ",",
    ".",
    "/",
    "{",
    "}",
    ":",
    "|",
    "<",
    ">",
    "?",
    "~",
    "`",
    "\"",
    "#"
]

def binary_7_bit(num):
    if(num > 127):
        return("ERROR: number greater than 127")
    
    raw_bin = str(bin(num)[2:])
    missing_zeroes = 7 - len(raw_bin)
    return("0"*missing_zeroes + raw_bin)

ASCII = dict(zip(ASCII_CHARACTERS, map(binary_7_bit, range(len(ASCII_CHARACTERS)))))

def binary(string):
    output = ""
    for i in string:
        output += ASCII.get(i)
    return output

def string(binary):
    if(len(binary) % 7 != 0):
        return("ERROR: binary string wrong length")
    
    is_binary = all(i in ["0", "1"] for i in binary)
    if not is_binary:
        return("ERROR: binary string contains non binary character")
    
    split = [binary[x:x+7] for x in range(0, len(binary), 7)]

    output = ""
    for chunk in split:
        output += list(ASCII.keys())[list(ASCII.values()).index(chunk)]
    return output

binary_string = binary("Hello world!")

with open("output.txt") as f:
    print(len(f.read()))