from triangulator.triangulator import area, triangulate_points

def test_triangulation_three_points():
    points = [(0,0),(3,0),(0,4)]
    triangle = (0,1,2)
    assert area(triangle, points) == 6

def test_area_simple():
    points = [(0,0),(3,0),(0,4)]
    triangle = (0,1,2)
    assert area(triangle, points) == 6

def test_triangulation_empty():
    points = []
    assert triangulate_points(points) == []

def test_triangulation_two_points():
    points = [(0,0),(1,1)]
    assert triangulate_points(points) == []

def test_triangulation_collinear():
    points = [(0,0),(1,1),(2,2)]
    assert triangulate_points(points) == []

def test_triangulation_duplicates():
    points = [(0,0),(1,0),(0,1),(0,0)]
    triangles = triangulate_points(points)
    for tri in triangles:
        assert len(tri) == 3

def test_area_multiple():
    points = [(0,0),(3,0),(0,4),(1,1)]
    triangles = [(0,1,2),(0,2,3)]
    for tri in triangles:
        assert area(tri, points) > 0
