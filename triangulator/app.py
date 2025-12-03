from flask import Flask, Response
import requests
from triangulator.binary_utils import  encode_triangles
from triangulator.triangulator import triangulate

def create_app():
    app = Flask(__name__)

    @app.get("/triangulate/<int:ps_id>")
    def handle(ps_id):
        url = f"http://pointsetmanager/pointset/{ps_id}"
        r = requests.get(url)

        if r.status_code == 404:
            return "PointSet not found", 404

        points = decode_points(r.content)
        triangles = triangulate(points)
        encoded = encode_triangles(points, triangles)

        return Response(encoded, mimetype="application/octet-stream")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
