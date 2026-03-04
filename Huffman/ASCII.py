from Huffman.settings import NUM_BITS

ASCII_CHARACTERS = [
    " ", 
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",    
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "1","2","3","4","5","6","7","8","9","0","-","=",
    "!","@","£","%","^","&","*","(",")","_","+",
    "[","]",";","'","\n",",",".","/",
    "{","}",":","|","<",">","?",
    "~","`",
    "\"", "\t", "\\",
    "§", "¬"
]

ASCII_CHARACTERS_64 = [
    " ", 
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",    
    "1","2","3","4","5","6","7","8","9","0","-","=",
    "[","]",";","'","\n",",",".","/",
    "{","}",":","|","<",">","?", "!",
    "~","`",
    "\"", "\t", "\\",
    "§", "¬", "Δ"
]

ASCII_CAPITALS = {
    "A": "a",
    "B": "b",
    "C": "c",
    "D": "d",
    "E": "e",
    "F": "f",
    "G": "g",
    "H": "h",
    "I": "i",
    "J": "j",
    "K": "k",
    "L": "l",
    "M": "m",
    "N": "n",
    "O": "o",
    "P": "p",
    "Q": "q",
    "R": "r",
    "S": "s",
    "T": "t",
    "U": "u",
    "V": "v",
    "W": "w",
    "X": "x",
    "Y": "y",
    "Z": "z",
    "\"": "2",
    "£": "3",
    "$": "4",
    "%": "5",
    "^": "6",
    "&": "7",
    "*": "8",
    "(": "9",
    ")": "0",
    "_": "-",
    "+": "=",
}

def int_to_bin(num, NUM_BITS):
    if(num > 2**NUM_BITS):
        return("ERROR: bit string too long")
    
    raw_bin = str(bin(num)[2:])
    missing_zeroes = NUM_BITS - len(raw_bin)
    return("0"*missing_zeroes + raw_bin)


ASCII_6_BIT = dict(zip(
    ASCII_CHARACTERS_64, 
    [int_to_bin(x, NUM_BITS) for x in range(len(ASCII_CHARACTERS))]
))

ASCII_7_BIT = dict(zip(
    ASCII_CHARACTERS, 
    [int_to_bin(x, NUM_BITS) for x in range(len(ASCII_CHARACTERS))]
))

ASCII_8_BIT = dict(zip(
    ASCII_CHARACTERS, 
    [bin(ord(char))[2:].zfill(8) for char in ASCII_CHARACTERS]
))