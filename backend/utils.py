import qrcode
from PIL import Image

def generate_qr_code(data, logo_path=None, color="black", background="white"):
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
        logo.thumbnail((60, 60))
        logo_pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, logo_pos, logo)

    img_path = "static/qrcodes/qrcode.png"
    img.save(img_path)
    return img_path
