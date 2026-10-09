from Huffman.ASCII import int_to_bin


def codes_from_depths(depths_sorted):
    """Build canonical Huffman codes from (character, depth) pairs."""
    num = 0
    codes = []
    current_depth = depths_sorted[0][1]

    for char, new_depth in depths_sorted:
        if new_depth != current_depth:
            num = num << (new_depth - current_depth)
            current_depth = new_depth

        codes.append((char, int_to_bin(num, current_depth)))
        num += 1

    return codes
