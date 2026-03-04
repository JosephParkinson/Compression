from Huffman.tree import huffman_depths
from Huffman.ASCII import int_to_bin, ASCII_6_BIT, ASCII_7_BIT, ASCII_8_BIT, ASCII_CAPITALS
from Huffman.settings import DEPTHS_ENCODING_BITS, BIT_LENGTH_ENCODING_LENGTH, NUM_BITS

if NUM_BITS == 6:
    ascii = ASCII_6_BIT 
elif NUM_BITS == 7:
    ascii = ASCII_7_BIT
else:
    ascii = ASCII_8_BIT

def character_to_code_dict(depths_sorted):
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


def encode_character_code_lengths(depths_sorted):
    # Tell the decoder how many bits the ASCII is
    output = int_to_bin(NUM_BITS, BIT_LENGTH_ENCODING_LENGTH)

    # Tell the decoder the first character and its bit length
    first_char = depths_sorted[0][0]
    current_length = depths_sorted[0][1]
    output += int_to_bin(current_length, DEPTHS_ENCODING_BITS) + ascii[first_char]

    for i in range(1, len(depths_sorted)):
        char_depth_tup = depths_sorted[i]
        char = char_depth_tup[0]
        new_length = char_depth_tup[1]
        if new_length == current_length: # No change in bit length, carry on
            output = output + ascii[char]
        else: 
            output = output + ascii["§"] # Tell decoder we are changing bit length
            output = output + int_to_bin(new_length, DEPTHS_ENCODING_BITS) # write new bit length down
            output = output + ascii[char]
    output = output + ascii["¬"] # Special end character
    
    return output

def message_to_ASCII_64(s):
    for upper in ASCII_CAPITALS.keys():
        s = s.replace(upper, f"Δ{ASCII_CAPITALS[upper]}")
    return s


def encode_message(s, code_dict):
    output = ""
    for char in s:
        output = output + code_dict[char]
    return output


def write_binary_string_to_file(binary_string, file_name):
    missing_zeroes = -len(binary_string) % 8
    encoding_for_file = binary_string + "0" * missing_zeroes

    bytes = int(encoding_for_file, base=2).to_bytes((len(encoding_for_file) + 7) // 8, byteorder='big')

    with open(file_name, "wb") as f:
        f.write(bytes)


def encode(s, file_name=None):  
    depths = huffman_depths(s)
    depths.sort(key=lambda tup: tup[1])

    length_encoding = encode_character_code_lengths(depths)
    
    code_dict = dict(character_to_code_dict(depths))

    message_encoding = encode_message(s, code_dict)

    encoding = length_encoding + message_encoding

    if file_name is not None:
        write_binary_string_to_file(encoding, f"Outputs/{file_name}")

    return encoding