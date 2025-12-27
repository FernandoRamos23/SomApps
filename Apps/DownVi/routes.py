from . import DownVi as app
from flask import render_template

@app.route('/')
def index():
    return render_template('DV_main/index.html')
