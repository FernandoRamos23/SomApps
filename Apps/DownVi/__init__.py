from flask import Blueprint

DownVi = Blueprint(
    'DownVi', __name__,
    url_prefix='/DownVi',
    template_folder='templates',
    static_folder='static',
    static_url_path='/DownVi/static')

from . import routes, request