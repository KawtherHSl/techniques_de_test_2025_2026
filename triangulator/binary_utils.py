import struct


def encode_triangles(points, triangles):
    result = struct.pack('<I', len(points))
    for x, y in points:
        result += struct.pack('<ff', x, y)
    result += struct.pack('<I', len(triangles))
    for a, b, c in triangles:
        result += struct.pack('<III', a, b, c)
    return result


# c pour le test decode_points_empty
def decode_points(data: bytes):
    """Format attendu : [count][x1][y1][x2][y2]..."""
    if len(data) == 0:
        return []   
    
    if len(data) < 4:
       
        raise struct.error("Data too short")

    # pour le nombre de points
    count = struct.unpack('<I', data[:4])[0]
    expected_size = 4 + count * 8

    if len(data) != expected_size:
        raise struct.error("Malformed data")

    points = []
    offset = 4
    for _ in range(count):
        x, y = struct.unpack('<ff', data[offset:offset+8])
        points.append((x, y))
        offset += 8
    
    return points
