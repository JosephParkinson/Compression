from ASCII import binary, string

test_string = "Hello, world!"

with open("output_uncompressed.txt", "w") as f:
    f.write(test_string)

s = binary(test_string)

with open("output_binary_string.txt", "w") as f:
    f.write(s)

bytess = int(s, base=2).to_bytes(len(s) // 8, byteorder='big')
with open("output_raw_binary_8_bit.txt", "wb") as f:
    f.write(bytess)

with open("output_raw_binary_8_bit.txt", "rb") as f:
    raw = f.read()

bits = ''.join(f'{b:08b}' for b in raw)
print(bits)
print(string(bits))