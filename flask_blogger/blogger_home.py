from flask import Blueprint, render_template

blogger_bp = Blueprint('Blogger',
        __name__,
    )

@blogger_bp.route('/about')
def about():
    return render_template('Blogger/about.html')

@blogger_bp.route('/index')
def index():
    return render_template('Blogger/index.html')

@blogger_bp.route('/album')
def album():
    return render_template('Blogger/album.html')

@blogger_bp.route('/details')
def details():
    return render_template('Blogger/details.html')

@blogger_bp.route('/leacots')
def leacots():
    return render_template('Blogger/leacots.html')

@blogger_bp.route('/whisper')
def whisper():
    return render_template('Blogger/whisper.html')