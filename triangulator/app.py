from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/triangulation/<pointSetId>', methods=['GET'])
def triangulate(pointSetId):
    return jsonify({"message": "Not implemented"}), 501

if __name__ == "__main__":
    app.run(debug=True)

