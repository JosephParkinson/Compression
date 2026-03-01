from settings import num_bits

NUM_BITS = num_bits

ASCII_CHARACTERS = [
    " ", 
    "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",    
    "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
    "1","2","3","4","5","6","7","8","9","0","-","=",
    "!","@","£","%","^","&","*","(",")","_","+",
    "[","]",";","'","\n",",",".","/",
    "{","}",":","|","<",">","?",
    "~","`",
    "\"", "\t"
]

def int_to_bin(num):
    if(num > 2**NUM_BITS):
        return("ERROR: bit string too long")
    
    raw_bin = str(bin(num)[2:])
    missing_zeroes = NUM_BITS - len(raw_bin)
    return("0"*missing_zeroes + raw_bin)

ASCII = dict(zip(
    ASCII_CHARACTERS, 
    [int_to_bin(x) for x in range(len(ASCII_CHARACTERS))]
))

def binary(string):
    output = ""
    for i in string:
        try:
            encoding = ASCII.get(i)
        except:
            raise ValueError(f"Unsupported character: {i}")
        output += encoding
    missing_zeroes = -len(output) % 8
    output += "0" * missing_zeroes
    return output

def string(binary):
    if(NUM_BITS not in [7, 8]): 
        return("ERROR: number of bits not supported")
    if(len(binary) % 8 != 0):
        return("ERROR: binary string wrong length")
    is_binary = all(i in ["0", "1"] for i in binary)
    if not is_binary:
        return("ERROR: binary string contains non binary character")
    
    split = [binary[x:x+NUM_BITS] for x in range(0, len(binary), num_bits)]

    output = ""
    for chunk in split:
        # TODO: find more elegant way of handling junk zeroes at the end of string
        if(len(chunk) == num_bits):
            output += list(ASCII.keys())[list(ASCII.values()).index(chunk)]

    return output