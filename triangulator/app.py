import struct

import requests
from flask import Flask, Response

from triangulator.binary_utils import decode_points, encode_triangles
from triangulator.triangulator import triangulate


def create_app():
    app = Flask(__name__)

    @app.get("/triangulate/<int:ps_id>")
    def handle(ps_id):
        url = f"http://pointsetmanager/pointset/{ps_id}"

        #  PointSetManager indispo
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException:
            return "PointSetManager unavailable", 503

        if r.status_code == 404:
            return "PointSet not found", 404

        # Décoder points
        try:
            points = decode_points(r.content)
        except struct.error:
            return "Malformed pointset data", 400

        # veifier PointSet vide
        if not points:
            return "PointSet empty", 400

        triangles = triangulate(points)
        encoded = encode_triangles(points, triangles)

        return Response(encoded, mimetype="application/octet-stream")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
