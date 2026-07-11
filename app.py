from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Inventory Management System API",
        "author": "Collins Masira",
        "status": "API Running"
    })


if __name__ == "__main__":
    app.run(debug=True)
