from triangulator.triangulator import triangulate

points = [(0, 0), (1, 0), (1, 1), (0, 1)]
triangles = triangulate(points)

print("Points :", points)
print("Triangles :", triangles)

