from triangulator.triangulator import triangulate


def test_triangulate_three_points():
    points = [(0, 0), (1, 0), (0, 1)]
    triangles = triangulate(points)
    assert triangles == [(0, 1, 2)]


def test_triangulate_square():
    points = [(0, 0), (1, 0), (1, 1), (0, 1)]
    triangles = triangulate(points)

    # il attnd 2 triangle
    assert len(triangles) == 2


def test_triangulate_aligned_points():
    points = [(0, 0), (1, 1), (2, 2)]
    triangles = triangulate(points)
    assert triangles == []  # aucun triangl possible
