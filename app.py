from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        app.run(host="localhost", port=8080, debug=True)
