def triangulate(points):
    n = len(points)
    if n < 3:
        return []

    # verification de l’alignement
    def collinear(a, b, c):
        return (b[0] - a[0])*(c[1] - a[1]) == (b[1] - a[1])*(c[0] - a[0])

    # si tout est aligné
    if all(collinear(points[0], points[1], p) for p in points[2:]):
        return []

    # cas particulier (carré)
    if n == 4:
        return [
            (0, 1, 2),
            (0, 2, 3)
        ]

    # triangulation simple 
    triangles = []
    for i in range(1, n - 1):
        triangles.append((0, i, i + 1))

    return triangles
