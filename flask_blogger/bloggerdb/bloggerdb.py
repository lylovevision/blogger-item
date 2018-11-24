from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import sys

app = Flask(__name__)
if sys.platform in ['win32','win64']:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/bloggerdb?charset=utf8mb4"
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost:3306/bloggerdb?charset=utf8mb4"
    
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Article(db.Model):
    """ 文章 """

    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    a_id = db.Column(db.Integer, autoincrement=True, primary_key=True, comment='文章id')
    a_title = db.Column(db.String(100), unique=True, nullable=False, comment='文章题目')
    a_content = db.Column(db.Text, nullable=False, comment='文章内容')
    a_img_path = db.Column(db.String(100), nullable=False, comment='文章img')
    a_time = db.Column(db.String(50),default='CURRENT_TIMESTAMP', comment='文章时间')
    a_comment = db.Column(db.String(200), nullable=False, comment='文章评论')


class Photo(db.Model):
    """ 相册 """
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    p_id = db.Column(db.Integer, autoincrement=True, primary_key=True ,comment='相册id')
    p_name = db.Column(db.Text, nullable=False ,comment='相册名')
    p_address = db.Column(db.String(100) ,comment='相册地点')
    p_time = db.Column(db.String(50), default='CURRENT_TIMESTAMP' ,comment='相册时间')
    p_img_path = db.Column(db.String(100), nullable=False ,comment='相册文件夹路径')

class Message(db.Model):
    """ 留言 """
    __table_args__ = {'mysql_collate': 'utf8mb4_general_ci'}
    m_id = db.Column(db.Integer, autoincrement=True, primary_key=True,comment='留言id')
    m_time = db.Column(db.String(50), default='CURRENT_TIMESTAMP',comment='留言时间')
    m_name = db.Column(db.String(50), nullable=False,comment='留言名称')
    m_content = db.Column(db.Text, nullable=False,comment='留言内容')

# # 1.创建表
db.create_all()

# # 2.增加记录
# admin = User(username='admin', email='admin@example.com')
# guest = User(username='guest', email='guest@example.com')
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()

# #3.查询记录,注意查询返回对象，如果查询不到返回None
# User.query.all() #查询所有
# User.query.filter_by(username='admin').first()#条件查询
# User.query.order_by(User.username).all()#排序查询
# User.query.limit(1).all()#查询1条
# User.query.get(id = 123)#精确查询

# # 4.删除
# user = User.query.get(id = 123)
# db.session.delete(user)
# db.session.commit()