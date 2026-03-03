from settings import NUM_BITS, DEPTHS_ENCODING_BITS
from ASCII import ASCII, int_to_bin

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


def decode_depths(code):
    depths = []
    current_length = int(code[:DEPTHS_ENCODING_BITS], 2)

    i = DEPTHS_ENCODING_BITS
    while i < len(code) - 1:
        binary = code[i: i + NUM_BITS]
        if(len(binary) == NUM_BITS):
            char = [key for key, val in ASCII.items() if val == binary][0]
        else:
            return "ERROR: not right length"         
        if char == "•":
            i += NUM_BITS
            break
        elif char == "§":
            i += NUM_BITS
            length_binary = code[i: i + DEPTHS_ENCODING_BITS]
            current_length = int(length_binary, 2)
            i += DEPTHS_ENCODING_BITS
        else:
            depths.append((char, current_length))
            i += NUM_BITS
    return depths, code[i:]


def decode(code):
    depths, message = decode_depths(code)
    
    codes = codes_from_depths(depths)

    decoded = ""

    length = 1
    while len(message) > 1:
        current_string = message[:length]
        if current_string in [x[1] for x in codes]:
            decoded = decoded + [x[0] for x in codes if x[1] == current_string][0]
            message = message[length:]
            length = 1
        else:
            length += 1

    return decoded


def decode_from_file(file_name):
    with open(file_name, "rb") as f:
        raw = f.read()

    payload = ''.join(f'{b:08b}' for b in raw)

    msg = decode(payload)

    return msg


print(decode_from_file("Outputs/r&J_test.txt"))