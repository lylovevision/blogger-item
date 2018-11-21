# -*- coding: utf-8 -*-
from flask import Flask
from blogger_home import blogger_bp
from page_home import page_bp

app = Flask(__name__)

app.register_blueprint(page_bp)
app.register_blueprint(blogger_bp)


if __name__ == '__main__':
    run_cfg = {
        'host': '0.0.0.0',
        'port': 9876,
        'debug': True 
    }
    app.run(**run_cfg)