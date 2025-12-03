def triangulate(points):
    n = len(points)
    if n < 3:
        return []

    # pour verifier l’alignement
    def collinear(a, b, c):
        return (b[0] - a[0])*(c[1] - a[1]) == (b[1] - a[1])*(c[0] - a[0])

    # triangulation simple 
    triangles = []
    for i in range(1, n - 1):
        triangles.append((0, i, i + 1))

    return triangles
