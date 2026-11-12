"""Simple linear prediction."""
def predict(values, slope=1.0, intercept=0.0):
    return [slope * value + intercept for value in values]
