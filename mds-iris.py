from sklearn import datasets
from sklearn.manifold import MDS
import matplotlib.pyplot as plt

# Load the iris dataset
iris = datasets.load_iris()
X = iris.data

# Perform MDS
mds = MDS(n_components=2)
X_r = mds.fit_transform(X)

# Plot the transformed data
plt.figure()
colors = ['navy', 'turquoise', 'darkorange']
lw = 2

for color, i, target_name in zip(colors, [0, 1, 2], iris.target_names):
    plt.scatter(X_r[iris.target == i, 0], X_r[iris.target == i, 1], color=color, alpha=.8, lw=lw,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('MDS of IRIS dataset')

plt.show()
