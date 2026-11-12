"""Simple binary classification for the Git exercise."""
DEFAULT_THRESHOLD = 0.4

def classify(values, threshold=DEFAULT_THRESHOLD):
    return [int(value >= threshold) for value in values]
