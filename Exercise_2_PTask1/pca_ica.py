import numpy as np


def generate_data(time_range : range) -> np.array:
    
    time_range = np.array(time_range)
    size = len(time_range)

    f1 = np.sin(time_range) + 0.0001 * np.random.normal(size = size)
    f2 = 2 * (time_range - np.floor(time_range)) + 0.0002 * np.random.normal(size = size)
    f3 = 0.001 * time_range + 0.0001 * np.random.normal(size = size)
    f = np.stack([f1,f2,f3])

    a = np.random.normal(size = [3,3])

    return np.matmul(a, f)


result = generate_data(range(100, 1, 0.01))