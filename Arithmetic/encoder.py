from common.text_stats import character_counts


def assign_intervals(text):
    if not text:
        return {}

    total_length = len(text)
    counts = character_counts(text)
    counts.sort(key=lambda tup: tup[1])

    interval_sizes = [(char, count / total_length) for char, count in counts]

    intervals = []
    lower_bound = 0.0
    for _, interval_size in interval_sizes:
        upper_bound = lower_bound + interval_size
        intervals.append((lower_bound, upper_bound))
        lower_bound = upper_bound

    return dict(zip([char for char, _ in interval_sizes], intervals))


def encode(text):
    """Temporary arithmetic encoder output until full bitstream encoding is added."""
    return assign_intervals(text)
