# Lesson 4B - Multiple Returns and Tuples: Score Stats
# STEP 1 ▸ Run it: only 64 prints. Return both in one line: return low, high.
# STEP 2 ▸ Unpack: lo, hi = quiz_stats(scores), then print Low and High.
# STEP 3 ▸ Add the average as a third value, and unpack all three.

scores = [72, 95, 88, 64]


def quiz_stats(scores):
    """Return the low and the high of the scores."""
    low = min(scores)
    high = max(scores)
    return low
    return high


stats = quiz_stats(scores)
print(stats)

# CHECK: (64, 95, 79.75) / Low: 64 High: 95 / Average: 79.75
# DONE EARLY: quiz_stats([]) crashes. Return None, None, None for an
# empty list. print("Empty:", quiz_stats([]))
# Expect: Empty: (None, None, None)
