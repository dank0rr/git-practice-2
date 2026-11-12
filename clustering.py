"""Group values around a split point."""
def cluster(values, split=100.0):
    return [[v for v in values if v < split], [v for v in values if v >= split]]
