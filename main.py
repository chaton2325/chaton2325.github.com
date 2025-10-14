from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# --- Dataset : liste de points 2D
data = [
    [1.0, 1.0],
    [1.5, 2.0],
    [3.0, 4.0],
    [5.0, 7.0],
    [3.5, 5.0],
    [4.5, 5.0],
    [3.5, 4.5],
]

# --- Création du modèle KMeans
k = 2  # nombre de clusters
kmeans = KMeans(n_clusters=k, random_state=42)

# --- Apprentissage du modèle
kmeans.fit(data)

# --- Récupération des résultats
labels = kmeans.labels_          # cluster de chaque point
centroids = kmeans.cluster_centers_  # centroïdes

# --- Affichage des résultats
print("Étiquettes des clusters :", labels)
print("Centroïdes :", centroids)

# --- Visualisation (optionnelle)
colors = ['red', 'blue', 'green', 'purple', 'orange']
for i, point in enumerate(data):
    plt.scatter(point[0], point[1], color=colors[labels[i]])
for centroid in centroids:
    plt.scatter(centroid[0], centroid[1], color='black', marker='X', s=200)
plt.title("Clusters K-Means")
plt.show()
