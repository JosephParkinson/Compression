from Huffman.settings import DEPTHS_ENCODING_BITS, BIT_LENGTH_ENCODING_LENGTH
from Huffman.ASCII import ASCII_6_BIT, ASCII_7_BIT, ASCII_8_BIT, ASCII_CAPITALS, int_to_bin


def codes_from_huffman_depths(depths_sorted):
    num = 0
    codes = []
    current_depth = depths_sorted[0][1]

    for i in range(len(depths_sorted)):
        char_depth_tup = depths_sorted[i]
        char = char_depth_tup[0]
        new_depth = char_depth_tup[1]
        
        if(new_depth == current_depth):
            codes.append((char, int_to_bin(num, current_depth)))
            num += 1
        else:
            num = num << (new_depth - current_depth)
            current_depth = new_depth
            codes.append((char, int_to_bin(num, current_depth)))
            num += 1

    return codes


def decode_depths(code):
    depths = []
    # read the length of each ASCII encoding
    i = BIT_LENGTH_ENCODING_LENGTH
    ASCII_bit_length = int(code[:i], 2)
    if ASCII_bit_length == 6: 
        ascii = ASCII_6_BIT
    elif ASCII_bit_length == 7:
        ascii = ASCII_7_BIT
    else:
        ascii = ASCII_8_BIT
    
    current_length = int(code[i:i+DEPTHS_ENCODING_BITS], 2)
    i += DEPTHS_ENCODING_BITS

    while i < len(code) - 1:
        binary = code[i: i + ASCII_bit_length]
        if(len(binary) == ASCII_bit_length):
            char = [key for key, val in ascii.items() if val == binary][0]
        else:
            return "ERROR: not right length"         
        if char == "¬":
            i += ASCII_bit_length
            break
        elif char == "§":
            i += ASCII_bit_length
            length_binary = code[i: i + DEPTHS_ENCODING_BITS]
            current_length = int(length_binary, 2)
            i += DEPTHS_ENCODING_BITS
        else:
            depths.append((char, current_length))
            i += ASCII_bit_length
    return depths, code[i:], ASCII_bit_length

def decode_capitals(message):
    for upper in ASCII_CAPITALS.keys():
        message = message.replace("Δ"+ASCII_CAPITALS[upper], upper)

    return message


def decode(string, from_file=False):
    """
    If from_file is set to True, string must be the file name to read from
    Else, decode string
    """
    if from_file:
        with open(string, "rb") as f:
            raw = f.read()

        encoded = ''.join(f'{b:08b}' for b in raw)
    else:
        encoded = string
    
    depths, message, ASCII_bit_length = decode_depths(encoded)
    
    codes = dict(codes_from_huffman_depths(depths))
    codes = {v: k for k, v in codes.items()}

    decoded = ""

    min_code_length = min([len(code) for code in codes.keys()])
    length = min_code_length

    while len(message) > min_code_length:
        current_string = message[:length]
        if current_string in codes.keys():
            decoded = decoded + codes[current_string]
            message = message[length:]
            length = min_code_length
        else:
            length += 1

    if ASCII_bit_length == 6:
        decoded = decode_capitals(decoded)

    return decoded
