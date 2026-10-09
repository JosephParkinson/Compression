from common.text_stats import character_counts


def huffman_tree(frequency):
    if len(frequency) > 1:
        frequency.sort(key=lambda tup: tup[1])
        lowest = frequency[0]
        second_lowest = frequency[1]
        frequency.append(((lowest[0], second_lowest[0]), lowest[1] + second_lowest[1]))
        frequency.pop(0)
        frequency.pop(0)
        huffman_tree(frequency)
    return frequency

def huffman_depths_from_tree(tree, depth=0):
    if not isinstance(tree, tuple):
        return [(tree, depth)]

    left, right = tree
    return huffman_depths_from_tree(left, depth + 1) + huffman_depths_from_tree(
        right, depth + 1
    )


def huffman_depths(s):
    frequency = character_counts(s)
    tree = huffman_tree(frequency)

    tree_formatted = tree[0][0]

    return huffman_depths_from_tree(tree_formatted)
