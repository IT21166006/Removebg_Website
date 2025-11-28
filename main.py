from flask import Flask, request, send_file, render_template
from rembg import remove, new_session
from PIL import Image
import io
import os

app = Flask(__name__)

# Railway gives PORT in environment
PORT = int(os.getenv("PORT", 8080))

# Use lightweight model to avoid memory crash
session = new_session("u2netp")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    input_image = Image.open(file.stream).convert("RGBA")

    output_image = remove(input_image, session=session)

    buffer = io.BytesIO()
    output_image.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(
        buffer,
        mimetype='image/png',
        as_attachment=True,
        download_name='output.png'
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
