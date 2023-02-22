import numpy as np
from matplotlib import pyplot as plt

from sklearn.decomposition import PCA,FastICA

def generate_data(time_range : np.array) -> np.array:
    
    size = len(time_range)

    f1 = np.sin(time_range) + 0.0001 * np.random.standard_normal(size = size)
    f2 = 2 * (time_range - np.floor(time_range)) + 0.0002 * np.random.standard_normal(size = size)
    f3 = 0.001 * time_range + 0.0001 * np.random.standard_normal(size = size)
    return np.stack([f1,f2,f3])

def rotate_data(data : np.array) -> np.array:

    a = np.random.standard_normal(size = [3,3])
    return np.matmul(a, data)

time_range = np.arange(1, 50, 0.05)
data = generate_data(time_range)
rotated_data = rotate_data(data)

#noise = np.random.standard_normal(size = len(time_range))
#plt.plot(time_range, data.transpose())
#plt.plot(time_range, rotated_data.transpose())
#plt.plot(time_range, noise)
#plt.show()

input_data = rotated_data.transpose()
pca = PCA()
pca_result = pca.fit(input_data).transform(input_data)

plt.plot(time_range, pca_result)
plt.show()

ica = FastICA()
print(data)