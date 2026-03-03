from tree import huffman_tree_depths
from ASCII import int_to_bin, ASCII
from settings import depths_encoding_bits

with open("Texts/romeo_and_juliet.txt", "r") as f:
    romeo_and_juliet_text = f.read()

_depths = huffman_tree_depths(romeo_and_juliet_text)

_depths.sort(key=lambda tup: tup[1])

def codes_from_depths(depths_sorted):
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

code_dict = dict(codes_from_depths(_depths))

def encode_lengths(depths_sorted):
    first_char = depths_sorted[0][0]
    current_length = depths_sorted[0][1]
    output = int_to_bin(current_length, depths_encoding_bits) + ASCII[first_char]
    for i in range(1, len(depths_sorted)):
        char_depth_tup = depths_sorted[i]
        char = char_depth_tup[0]
        new_length = char_depth_tup[1]
        if new_length == current_length:
            output = output + ASCII[char]
        else:
            output = output + ASCII["§"]
            output = output + int_to_bin(new_length, depths_encoding_bits)
            output = output + ASCII[char]
    output = output + ASCII["•"]
    
    return output

LENGTH_ENCODING = encode_lengths(depths_sorted=_depths)

def encode_message(s, code_dict):
    output = ""
    for char in s:
        output = output + code_dict[char]

    return output

def payload():
    return encode_lengths(_depths) + encode_message(romeo_and_juliet_text, code_dict)

PAYLOAD = payload()

missing_zeroes = -len(PAYLOAD) % 8
PAYLOAD += "0" * missing_zeroes

bytess = int(PAYLOAD, base=2).to_bytes((len(PAYLOAD) + 7) // 8, byteorder='big')
with open("romeo_and_juliet_huffman.txt", "wb") as f:
    f.write(bytess)
