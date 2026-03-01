from ASCII import binary, string
s = binary("Hello, world!")
bytess = int(s, base=2).to_bytes(len(s) // 8, byteorder='big')

with open("output.txt", "w") as f:
    f.write(binary("Hello, world!"))

with open("output.bin", "wb") as f:
    f.write(bytess)

with open("output.bin", "rb") as f:
    raw = f.read()

bits = ''.join(f'{b:08b}' for b in raw)
print(bits)
print(string(bits))