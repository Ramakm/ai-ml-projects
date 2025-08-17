from flask import Flask, render_template, request, jsonify
import os
import uuid
from utils.image_processing import detect_plate
from utils.ocr import extract_text

UPLOAD_FOLDER = "static/uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Save file
    filename = str(uuid.uuid4()) + ".jpg"
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    # Detect plate
    plate_img = detect_plate(filepath)

    # OCR
    text = extract_text(plate_img)

    return jsonify({"filename": filename, "text": text})

if __name__ == "__main__":
    app.run(debug=True)
