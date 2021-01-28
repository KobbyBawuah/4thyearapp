from flask_frozen import Freezer
from main import app

freezer = Freezer(app)

if name == 'main':
    freezer.freeze()
