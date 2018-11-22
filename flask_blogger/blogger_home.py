from flask import Blueprint, render_template, request
from bloggerdb.bloggerdb import db, Message, Photo, Article
import socket
import datetime

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
    """ 留言 """
    m_all = Message.query.all()
    m_me_list = [None, '']
    for m in m_all:
        m_me_list.append(m.m_content)
    # 获得留言
    req = request.args.get('desc')
    if req not in m_me_list:
        # 默认以主机名登录
        nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        hostname = socket.gethostname()
        hostname = Message(m_time = nowtime,m_name = hostname, m_content = req)
        db.session.add(hostname)
        db.session.commit()
    m_all = Message.query.all()
    m_list = []
    for m in m_all:
        m_list.append([m.m_name, m.m_time, m.m_content])
    return render_template('Blogger/leacots.html', m_list=m_list)


@blogger_bp.route('/whisper')
def whisper():
    return render_template('Blogger/whisper.html')