import glob
from random import choice
from flask import request, render_template, send_file
from placepuppy import app
import PIL
from PIL import Image

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<int:width>/<int:height>', methods=['GET'])
def image(width, height):
    basewidth = width
    images = glob.glob('placepuppy/static/img/*')
    img = Image.open(choice(images))
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save('placepuppy/static/img/resized_img.png')
    src = choice(images)[11:]
    return send_file('static/img/resized_img.png', mimetype='image/png')
