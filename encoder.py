from tree import huffman_tree_depths
from ASCII import int_to_bin, ASCII
from settings import DEPTHS_ENCODING_BITS

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


def encode_lengths(depths_sorted):
    first_char = depths_sorted[0][0]
    current_length = depths_sorted[0][1]
    output = int_to_bin(current_length, DEPTHS_ENCODING_BITS) + ASCII[first_char]
    for i in range(1, len(depths_sorted)):
        char_depth_tup = depths_sorted[i]
        char = char_depth_tup[0]
        new_length = char_depth_tup[1]
        if new_length == current_length:
            output = output + ASCII[char]
        else:
            output = output + ASCII["§"]
            output = output + int_to_bin(new_length, DEPTHS_ENCODING_BITS)
            output = output + ASCII[char]
    output = output + ASCII["•"]
    
    return output


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


def encode(s, file_name):
    depths = huffman_tree_depths(s)
    depths.sort(key=lambda tup: tup[1])

    length_encoding = encode_lengths(depths)
    
    code_dict = dict(codes_from_depths(depths))
    message_encoding = encode_message(s, code_dict)

    encoding = length_encoding + message_encoding

    write_binary_string_to_file(encoding, file_name)

    return encoding


with open("Texts/romeo_and_juliet.txt", "r") as f:
    s = f.read()

encode(s, "Outputs/r&J_test.txt")