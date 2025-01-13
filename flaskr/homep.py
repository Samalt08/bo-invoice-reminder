from flask import(
    Blueprint, flash, g, redirect, render_template, request, url_for
)
import os

bp = Blueprint('homep', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if "file" in request.files:
            original_filename = request.files['file'].filename
            # original_filename = "sam"
            save_path = os.path.join('flaskr/filer', original_filename)
            file = request.files['file']
            file.save(save_path)
    return render_template('homep/HomePage.html')
