from flask import Blueprint, render_template

page_bp = Blueprint('page',
        __name__,
    )

@page_bp.route('/imgs')
def imgs_d():
    return render_template('page/test.html')

@page_bp.route('/login')
def page_login():
    return render_template('page/page-login.html')

@page_bp.app_errorhandler(404)
def page_not_found(error):
    return render_template('page/404.html')