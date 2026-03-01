tree = "001D1E1A01C1B"

def encoding_from_tree():
    encoding = {}
    succesive_leaf_count = 0
    code = "0"
    i = 0
    while i < len(tree):
        if tree[i] == "0":
            succesive_leaf_count = 0
            code += "0"
            i = i + 1
        elif tree[i] == "1":
            succesive_leaf_count += 1
            encoding[tree[i + 1]] = code
            code = code[:-1]
            if(succesive_leaf_count >= 2):
                code = code[:-1]
            code += "1"
            i = i + 2
    return encoding

frequency_test = [
    ("D", 5),
    ("E", 1),
    ("B", 3),
    ("A", 2),
]

def tree_from_frequency(frequency):
    if(len(frequency) > 2):
        frequency.sort(key=lambda tup: tup[1])
        lowest = frequency[0]
        second_lowest = frequency[1]
        frequency.append(
            ((lowest[0], second_lowest[0]), lowest[1] + second_lowest[1])
        )
        frequency.pop(0)
        frequency.pop(0)
        tree_from_frequency(frequency)
    return frequency
    
# print(tree_from_frequency(frequency_test))
with open("Texts/romeo_and_juliet.txt", "r") as f:
    s = f.read()

def character_counts(text):
    characters = {}
    for i in text:
        if i not in characters.keys():
            characters[i] = 1
        else:
            characters[i] += 1
    return characters

print(tree_from_frequency(list(character_counts(s).items())))