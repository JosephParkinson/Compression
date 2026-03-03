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
    if not isinstance(tree, tuple):
        return [(tree, depth)]

    left, right = tree
    return (
        get_depths(left, depth + 1) +
        get_depths(right, depth + 1)
    )

def huffman_tree_depths(s):
    frequency = character_counts(s)
    tree = tree_from_frequency(frequency)

    return get_depths(tree[0][0])