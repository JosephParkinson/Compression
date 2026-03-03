from settings import num_bits, depths_encoding_bits
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

def decode(code):
    depths = []
    current_length = int(code[:depths_encoding_bits], 2)

    i = depths_encoding_bits
    while i < len(code) - 1:
        binary = code[i: i + num_bits]
        if(len(binary) == num_bits):
            char = [key for key, val in ASCII.items() if val == binary][0]
        else:
            return "ERROR: not right length"         
        if char == "•":
            i += num_bits
            break
        elif char == "§":
            i += num_bits
            length_binary = code[i: i + depths_encoding_bits]
            current_length = int(length_binary, 2)
            i += depths_encoding_bits
        else:
            depths.append((char, current_length))
            i += num_bits
    
    codes = codes_from_depths(depths)

    message = code[i:]

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

with open("Outputs/romeo_and_juliet_huffman.txt", "rb") as f:
    raw = f.read()

payload = ''.join(f'{b:08b}' for b in raw)

msg = decode(payload)

print(msg)

