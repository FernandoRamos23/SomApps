from flask import Flask
from flask import render_template, redirect, jsonify
from flask import request, session

from Apps.DownVi import DownVi

app = Flask(__name__)
app.register_blueprint(DownVi)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
