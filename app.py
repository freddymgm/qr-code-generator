from flask import Flask, render_template, request, send_file
import qrcode
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        color = request.form['color']
        icon = request.files['icon']

        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(url)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color=color, back_color="white")

        if icon and icon.filename != '':
            icon_img = Image.open(icon)
            icon_size = (qr_img.size[0] // 4, qr_img.size[1] // 4)
            icon_img = icon_img.resize(icon_size)
            pos = ((qr_img.size[0] - icon_img.size[0]) // 2, (qr_img.size[1] - icon_img.size[1]) // 2)
            qr_img.paste(icon_img, pos, icon_img)
        else:
            default_icon = Image.open(os.path.join('static', 'img', 'default_icon.png'))
            icon_size = (qr_img.size[0] // 4, qr_img.size[1] // 4)
            default_icon = default_icon.resize(icon_size)
            pos = ((qr_img.size[0] - default_icon.size[0]) // 2, (qr_img.size[1] - default_icon.size[1]) // 2)
            qr_img.paste(default_icon, pos, default_icon)

        img_io = io.BytesIO()
        qr_img.save(img_io, 'PNG')
        img_io.seek(0)
        return send_file(img_io, mimetype='image/png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)