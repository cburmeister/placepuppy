from flask import request, render_template, send_file
from placepuppy import app, utils

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<int:width>/<int:height>', methods=['GET'])
def image(width, height):
    utils.resize_da_puppeh(width, height)
    return send_file('static/img/resized_img.png', mimetype='image/png')
