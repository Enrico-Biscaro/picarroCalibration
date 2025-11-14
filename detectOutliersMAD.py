import numpy as np

def detect_outliers_mad(data, threshold):
    median = np.median(data)
    deviations = np.abs(data - median)
    mad = np.median(deviations)
    if mad == 0:
        return np.zeros(len(data), dtype=bool)
    modified_z_scores = 0.6745 * deviations / mad
    return modified_z_scores > threshold