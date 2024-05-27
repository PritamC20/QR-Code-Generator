from flask import request, jsonify, send_file
from app import app
import qrcode
from PIL import Image
import io

@app.route('/generate', methods=['POST'])
def generate_qr_code():
    data = request.form.get('url')
    color = request.form.get('color', 'black')
    background = request.form.get('background', 'white')
    logo_path = request.files.get('logo_path')

    if not data:
        return jsonify({'error': 'No URL provided'}), 400

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=color, back_color=background).convert('RGB')

    if logo_path:
        logo = Image.open(logo_path)
        box = (img.size[0] // 2 - logo.size[0] // 2, img.size[1] // 2 - logo.size[1] // 2)
        img.paste(logo, box, mask=logo)

    byte_io = io.BytesIO()
    img.save(byte_io, 'PNG')
    byte_io.seek(0)

    return send_file(byte_io, mimetype='image/png')
