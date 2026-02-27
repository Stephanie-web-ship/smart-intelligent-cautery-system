from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Updated medically structured values
data = {
    "Tissue": {
        "minimum": "60°C",
        "safe": "70–100°C",
        "threshold": "110°C"
    },
    "Intestine": {
        "minimum": "60°C",
        "safe": "70–100°C",
        "threshold": "105°C"
    },
    "Skin": {
        "minimum": "60°C",
        "safe": "70–100°C",
        "threshold": "105°C"
    }
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_data/<material>")
def get_data(material):
    return jsonify(data.get(material, {}))

if __name__ == "__main__":
    app.run(debug=True)