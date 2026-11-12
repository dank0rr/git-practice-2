"""Measure classification accuracy."""
def accuracy(expected, actual):
    if len(expected) != len(actual):
        raise ValueError("Lengths must match")
    return sum(a == b for a, b in zip(expected, actual)) / len(expected) if expected else 0.0
