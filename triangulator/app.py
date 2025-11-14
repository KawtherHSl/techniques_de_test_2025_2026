from flask import Flask, jsonify
from triangulator.binary_utils import encode_triangles, decode_points
from triangulator.triangulator import triangulate_points


app = Flask(__name__)

POINT_SETS = {
    "triangulable": [(0,0), (1,0), (0,1)], 
    "collinear": [(0,0),(1,1),(2,2)]       
}



@app.route('/triangulation/<pointSetId>', methods=['GET'])
def triangulate(pointSetId):
    points = POINT_SETS.get(pointSetId)
    if points is None:
        return jsonify({"error": "Point set not found"}), 404

    triangles = triangulate_points(points)

    if not triangles:
        return jsonify({"error": "Triangulation failed"}), 501

    triangles_list = [list(map(int, tri)) for tri in triangles]
    return jsonify({"triangles": triangles_list}), 200
