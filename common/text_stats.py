"""Text statistics shared by multiple encoders."""


def character_counts(text):
    """Return a list of (character, count) pairs preserving first-seen order."""
    counts = {}
    for character in text:
        counts[character] = counts.get(character, 0) + 1
    return list(counts.items())
