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
    if(len(frequency) > 1):
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
    
def character_counts(text):
    characters = []
    for i in range(len(text)):
        existing_characters = [x[0] for x in characters]
        character = text[i]
        if character not in existing_characters:
            characters.append((character, 1))
        else:
            for x in characters:
                if x[0] == character:
                    characters[characters.index(x)] = (character, x[1] + 1)
                    break
    return characters

def get_depths(tree, depth=0):
    # Leaf
    if not isinstance(tree, tuple):
        return [(tree, depth)]

    # Internal node
    left, right = tree
    return (
        get_depths(left, depth + 1) +
        get_depths(right, depth + 1)
    )

def depth_per_node(tree):
    depth = 0
    depths = []
    i = 0
    while i < len(tree):
        char = tree[i]
        if char == "(":
            depth += 1
            i += 1
        elif char == ")":
            depth -= 1
            i += 1
        elif char in ["'", '"']:
            if tree[i + 1] == "\\":
                s = tree[i+2:i+3]
                if(s == "n"):
                    depths.append(("\n", depth))
                else:
                    depths.append(("\t", depth))
                i += 4
            else:
                new_char = tree[i + 1]
                depths.append((new_char, depth))
                i += 3
        else:
            i += 1
    return depths


def huffman_tree_depths(s):
    frequency = character_counts(s)
    tree = tree_from_frequency(frequency)

    return get_depths(tree[0][0])