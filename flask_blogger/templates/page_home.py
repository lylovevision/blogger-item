from flask import Blueprint, render_template

page_bp = Blueprint('page',
        __name__,
    )

@page_bp.route('/imgs')
def bg():
    return render_template('page/test.html')

@page_bp.route('/login')
def page_login():
    return render_template('page/page-login.html')