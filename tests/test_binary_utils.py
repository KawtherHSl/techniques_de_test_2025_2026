import pytest
from triangulator.binary_utils import encode_triangles, decode_points
import struct


def test_decode_points_valid_input():
    data = struct.pack('I', 2) + struct.pack('ff', 0, 1) + struct.pack('ff', 0, 2)
    points = decode_points(data)
    assert points == [(0,1),(0,2)]

def test_decode_points_invalid_input():
    data = b'\x00'
    import pytest
    with pytest.raises(Exception):
        decode_points(data)

def test_decode_points_normal():
    import struct
    # 2 points : (1.0, 2.0) et (3.0, 4.0)
    data = struct.pack('Iffff', 2, 1.0, 2.0, 3.0, 4.0)
    points = decode_points(data)
    assert points == [(1.0, 2.0), (3.0, 4.0)]

def test_decode_points_empty():
    assert decode_points(b'') == []

import pytest

def test_decode_points_malformed():
    data = b'\x01\x02'  # trop court
    with pytest.raises(struct.error):
        decode_points(data)

def test_encode_triangles_normal():
    triangles = [(0,1,2)]
    b = encode_triangles(triangles)
    import struct
    expected = struct.pack('I', 1) + struct.pack('III', 0,1,2)
    assert b == expected

def test_encode_triangles_empty():
    assert encode_triangles([]) == struct.pack('I', 0)


def test_encode_triangles():
    triangles = [(0,1,2)]
    encoded = encode_triangles(triangles)
    assert isinstance(encoded, bytes)
