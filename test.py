from ASCII import binary, string
from settings import num_bits, test_string

def run_test():
    with open("Outputs/output_uncompressed.txt", "w") as f:
        f.write(test_string)

    s = binary(test_string)
    bytess = int(s, base=2).to_bytes((len(s) + 7) // 8, byteorder='big')
    with open(f"Outputs/output_raw_binary_{num_bits}_bit.txt", "wb") as f:
        f.write(bytess)

    with open(f"Outputs/output_raw_binary_{num_bits}_bit.txt", "rb") as f:
        raw = f.read()

    bits = ''.join(f'{b:08b}' for b in raw)

