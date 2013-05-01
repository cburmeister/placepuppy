from flask import request
from placepuppy import app

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    return 'PUPPIES!!!!'
