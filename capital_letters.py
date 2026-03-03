with open("Texts/romeo_and_juliet.txt", "r") as f:
    s = f.read()

uppers = [c for c in s if c.isupper()]
lowers = [c for c in s if c.islower()]
others = [c for c in s if not (c.islower() or c.isupper())]

print(f"Total chars: {len(s)}")
print(f"Uppers: {len(uppers)}")
print(f"Lowers: {len(lowers)}")
print(f"Others: {len(others)}")
print(f"Ratio of uppers to lowers: {len(uppers) / len(lowers)}")

new_length = len(uppers) * 2 + len(lowers) + len(others)

print(f"new length of string with special upper character: {new_length}")

print(f"current number of bits: {len(s)*7}")
print(f"new number of bits: {new_length * 6}")