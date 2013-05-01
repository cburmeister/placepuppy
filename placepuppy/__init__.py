from flask import Flask

app = Flask(__name__)

import logging
from logging import FileHandler
file_handler = FileHandler('/tmp/placepuppy.log')
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

from placepuppy import views
