from triangulator.triangulator import triangulate

# Exemple de points : carré
points = [(0, 0), (1, 0), (1, 1), (0, 1)]
triangles = triangulate(points)

print("Points :", points)
print("Triangles :", triangles)
