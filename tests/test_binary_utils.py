import struct

import pytest

from triangulator.binary_utils import decode_points, encode_triangles


def test_decode_points_valid_input():
    data = struct.pack('I', 2) + struct.pack('ff', 0, 1) + struct.pack('ff', 0, 2)
    points = decode_points(data)
    assert points == [(0,1),(0,2)]

def test_decode_points_invalid_input():
    data = b'\x00'
    with pytest.raises(struct.error):
        decode_points(data)

def test_decode_points_normal():
    data = struct.pack('Iffff', 2, 1.0, 2.0, 3.0, 4.0)
    points = decode_points(data)
    assert points == [(1.0, 2.0), (3.0, 4.0)]

def test_decode_points_empty():
    assert decode_points(b'') == []

def test_decode_points_malformed():
    data = b'\x01\x02'  # pour qlq chose court
    with pytest.raises(struct.error):
        decode_points(data)

def test_encode_triangles_normal():
    points = [(0, 0), (1, 1), (2, 2)]
    triangles = [(0,1,2)]
    b = encode_triangles(points, triangles)
    expected = struct.pack('<I', len(points))
    for x, y in points:
        expected += struct.pack('<ff', x, y)
    expected += struct.pack('<I', len(triangles))
    for a, b_, c in triangles:
        expected += struct.pack('<III', a, b_, c)
    assert b == expected

def test_encode_triangles_empty():
    assert encode_triangles([], []) == struct.pack('<I', 0) + struct.pack('<I', 0)
    


