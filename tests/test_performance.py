import pytest
import time
from triangulator.binary_utils import decode_points, encode_triangles
from triangulator.triangulator import triangulate
import struct


@pytest.mark.slow
def test_decode_performance():
    data = struct.pack('<I', 1000)
    for _ in range(1000):
        data += struct.pack('<ff', 1.0, 2.0)

    start = time.time()
    decode_points(data)
    assert time.time() - start < 0.5

    


