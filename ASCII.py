from settings import NUM_BITS

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
    "§", "•"
]

def int_to_bin(num, NUM_BITS):
    if(num > 2**NUM_BITS):
        return("ERROR: bit string too long")
    
    raw_bin = str(bin(num)[2:])
    missing_zeroes = NUM_BITS - len(raw_bin)
    return("0"*missing_zeroes + raw_bin)


ASCII = dict(zip(
    ASCII_CHARACTERS, 
    [int_to_bin(x, NUM_BITS) for x in range(len(ASCII_CHARACTERS))]
))