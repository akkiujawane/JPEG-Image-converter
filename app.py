from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return redirect(request.url)

    image = request.files['image']
    input_path = os.path.join(app.root_path, 'uploads', image.filename)
    output_path = os.path.join(app.root_path, 'static', 'output.jpg')
    image.save(input_path)

    with Image.open(input_path) as im:
        rgb_im = im.convert('RGB')
        rgb_im.save(output_path, 'JPEG')

    os.remove(input_path)

    return redirect(url_for('result'))


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
