"""Group values around a split point."""
def cluster(values, split=0.5):
    return [[v for v in values if v < split], [v for v in values if v >= split]]
