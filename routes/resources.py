from flask import Blueprint, render_template
from models import Resource

bp = Blueprint('resources', __name__)

@bp.route('/resources')
def resources():
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)
