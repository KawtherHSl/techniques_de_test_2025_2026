from triangulator.triangulator import triangulate

if __name__ == "__main__":
    points = [(0,0), (1,0), (2,0), (2,1), (1,1), (0,1)]

    triangles = triangulate(points)
    
    print("Points :", points)
    print("Triangles :", triangles)

