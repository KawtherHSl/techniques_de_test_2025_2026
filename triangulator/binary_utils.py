import struct

def encode_triangles(points, triangles):
    result = struct.pack('<I', len(points))
    for x, y in points:
        result += struct.pack('<ff', x, y)
    result += struct.pack('<I', len(triangles))
    for a, b, c in triangles:
        result += struct.pack('<III', a, b, c)
    return result