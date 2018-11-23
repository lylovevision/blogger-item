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

@blogger_bp.route('/details')
def details():
    # 获取请求参数
    dreq = request.args.get('param')
    desc = request.args.get('desc')
    # 判断有哪种请求方式
    if dreq and desc:
        aa_all = Article.query.filter_by(a_id=dreq).first()
        mess_list = aa_all.a_comment
        mess_list = mess_list.split('$▓㊣$')
        mess_list = [x for x in mess_list if x != ' ']
        mess_list.append(desc)
        mess_list = list(set(mess_list))

        a_update = Article.query.filter_by(a_id = dreq).update({'a_comment' : '$▓㊣$'.join(mess_list)})
        db.session.commit()
        aa_all = Article.query.filter_by(a_id=dreq).first()
        mess_list = aa_all.a_comment
        mess_list = mess_list.split('$▓㊣$')
        mess_list = [x for x in mess_list if x != ' ']
    elif dreq:
        aa_all = Article.query.filter_by(a_id=dreq).first()
        mess_str = aa_all.a_comment
        mess_list = mess_str.split('$▓㊣$')
        print('sdafsdafdsk')
    # 如果两种都没有
    else:
        pass
    return render_template('Blogger/details.html', aa_all=aa_all, mess_list=mess_list, dreq=dreq)


@blogger_bp.route('/index')
def index():
    a_all = Article.query.all()
    a_list = [a for a in a_all]

    return render_template('Blogger/index.html', a_list = a_list)

@blogger_bp.route('/album')
def album():
    return render_template('Blogger/album.html')



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