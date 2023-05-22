import numpy as np
import Levenshtein as lev
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# List of flower names
flower_names = [
    'Rose', 'Tulip', 'Daisy', 'Sunflower', 'Lily', 'Orchid', 'Carnation', 'Daffodil', 'Iris', 'Marigold', 
    'Hyacinth', 'Lilac', 'Jasmine', 'Chrysanthemum', 'Poppy', 'Pansy', 'Peony', 'Violet', 'Magnolia', 'Hibiscus', 
    'Azalea', 'Camellia', 'Freesia', 'Geranium', 'Lavender', 'Begonia', 'Amaryllis', 'Dahlia', 'Zinnia', 'Gardenia'
]

# Create a 2D array to store the Levenshtein distances
distances = np.zeros((len(flower_names), len(flower_names)))

# Calculate the Levenshtein distance between each pair of words
for i in range(len(flower_names)):
    for j in range(len(flower_names)):
        distances[i, j] = lev.distance(flower_names[i], flower_names[j])

# Perform MDS
mds = MDS(n_components=2, dissimilarity='precomputed')
coords = mds.fit_transform(distances)

# Plot the transformed data
plt.figure()
plt.scatter(coords[:, 0], coords[:, 1], marker = 'o')

for label, x, y in zip(flower_names, coords[:, 0], coords[:, 1]):
    plt.annotate(label, xy = (x, y), xytext = (-10, 10), textcoords = 'offset points')
plt.show()
