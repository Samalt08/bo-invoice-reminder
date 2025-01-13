from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('writings', __name__, url_prefix='/templates')



@bp.route('/templates', methods=['GET'])
def templates():
    templates = [
        "template 1",
        "template 2",
        "template 3",
        "template 4",
        "template 5"
    ]
    return render_template('shows/writers.html', templates=templates)