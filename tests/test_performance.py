import struct
import time

import pytest

from triangulator.binary_utils import decode_points
from triangulator.triangulator import triangulate


@pytest.mark.slow
def test_decode_performance1():
    data = struct.pack('<I', 10)
    for _ in range(10):
        data += struct.pack('<ff', 1.0, 2.0)

    start = time.time()
    decode_points(data)
    assert time.time() - start < 0.5

@pytest.mark.slow
def test_decode_performance2():
    data = struct.pack('<I', 100)

    for _ in range(100):
        data += struct.pack('<ff', 1.0, 2.0)

    start = time.time()
    decode_points(data)
    assert time.time() - start < 0.5


@pytest.mark.slow
def test_decode_performance3():
    data = struct.pack('<I', 1000)
    for _ in range(1000):
        data += struct.pack('<ff', 1.0, 2.0)

    start = time.time()
    decode_points(data)
    assert time.time() - start < 0.5


@pytest.mark.slow
def test_triangulation_performance():
    points = [(i, i * 0.5) for i in range(2000)]
    start = time.time()
    triangulate(points)
    assert time.time() - start < 1.0
