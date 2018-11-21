from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import sys

app = Flask(__name__)
if sys.platform in ['win32','win64']:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/bloggerdb?charset=utf8"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/bloggerdb?charset=utf8"
    
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

