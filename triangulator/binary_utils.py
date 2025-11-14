import struct

def decode_points(data):
  
    points = []
    if not data:
        return points

   
    n = struct.unpack('I', data[:4])[0]
    offset = 4

    for _ in range(n):
        x = struct.unpack('f', data[offset:offset+4])[0]
        offset += 4
        y = struct.unpack('f', data[offset:offset+4])[0]
        offset += 4
        points.append((x, y))
    return points


def encode_triangles(triangles):
   
    b = struct.pack('I', len(triangles))
    for tri in triangles:
        b += struct.pack('III', *tri)
    return b

