import glob
from random import choice
from flask import request, render_template, send_file
from placepuppy import app

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<width>/<height>', methods=['GET'])
def image(width, height):
    images = glob.glob('placepuppy/static/img/*')
    src = choice(images)[11:]
    return send_file(src, mimetype='image/png')
