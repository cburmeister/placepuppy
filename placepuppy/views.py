from flask import request, redirect, url_for, render_template, send_file
from placepuppy import app, utils
import os
from werkzeug import secure_filename

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<int:width>/<int:height>', methods=['GET'])
def image(width, height):
    utils.resize_da_puppeh(width, height)
    return send_file('static/img/resized_img.png', mimetype='image/png')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return render_template('upload.html')
