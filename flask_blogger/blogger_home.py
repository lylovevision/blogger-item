from flask import ( 
    Blueprint, render_template, request,
    send_from_directory,redirect,url_for,abort,Flask
    )
from helper import random_filename, ensure_folder
from bloggerdb.bloggerdb import db, Message, Photo, Article
from werkzeug.datastructures import FileStorage
import socket
import datetime
import os



ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.upload_folder = os.path.join(ROOT, 'upload')
ensure_folder(app.upload_folder)

blogger_bp = Blueprint('Blogger',
        __name__,
    )

@blogger_bp.route('/album')
def album():
    """ 相册 """
    p_all = Photo.query.all()
    
    return render_template('Blogger/album.html', p_all=p_all)
# ##############################################

# #########################################


@blogger_bp.route('/about')
def about():
    return render_template('Blogger/about.html')

@blogger_bp.route('/details')
def details():
    dreq = request.args.get('param')
    desc = request.args.get('desc')
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
    else:
        pass
    return render_template('Blogger/details.html', aa_all=aa_all, mess_list=mess_list, dreq=dreq)


@blogger_bp.route('/index')
def index():
    a_all = Article.query.all()
    a_list = [a for a in a_all]

    return render_template('Blogger/index.html', a_list = a_list)


@blogger_bp.route('/leacots')
def leacots():
    """ 留言 """
    m_all = Message.query.all()
    m_me_list = [None, '']
    for m in m_all:
        m_me_list.append(m.m_content)
    req = request.args.get('desc')
    if req not in m_me_list:
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