import pytest
import time
from triangulator.triangulator import triangulate_points

@pytest.mark.performance
def test_triangulation_speed():
    points = [(0,0),(1,0),(0,1),(1,1)]
    start = time.time()
    triangles = triangulate_points(points)
    end = time.time()
    duration = end - start
    assert duration < 1 

@pytest.mark.performance
def test_triangulation_10_points():
    points = [(i,i*0.5) for i in range(10)]
    start = time.time()
    triangles = triangulate_points(points)
    assert time.time() - start < 0.1

@pytest.mark.performance
def test_triangulation_100_points():
    points = [(i,i*0.5) for i in range(100)]
    start = time.time()
    triangles = triangulate_points(points)
    assert time.time() - start < 0.5

@pytest.mark.performance
def test_triangulation_1000_points():
    points = [(i,i*0.5) for i in range(1000)]
    start = time.time()
    triangles = triangulate_points(points)
    assert time.time() - start < 2