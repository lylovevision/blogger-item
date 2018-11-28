# -*- coding: utf-8 -*-
from blogger_home import blogger_bp
from page_home import page_bp
import os
from flask import (
    Flask, request, render_template, send_from_directory,
    redirect, url_for, abort
)
from werkzeug.datastructures import FileStorage
from helper import random_filename, ensure_folder
from bloggerdb.bloggerdb import db, Photo
import datetime

ALLOW_EXTENSIONS = set(['jpg', 'png', 'gif', 'jpeg', 'tga', 'psd', 'bmp'])
ROOT = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

app.upload_folder = os.path.join(ROOT, 'upload')
ensure_folder(app.upload_folder)

potime = ''

@app.route('/photo')
def view_index():
    global potime
    potime = request.args.get('nowtime')
    file_list = []
    sql_poall = Photo.query.filter_by(p_time = potime).first()
    if sql_poall in [None, '']:
        pass
    else:
        sqlponame_list = sql_poall.p_name
        # 划分字符串
        time_filename = sqlponame_list
        ss_list = time_filename.split('@@')
        ss_list.remove(ss_list[0])
        file_list =[]
        for s in ss_list:
            for sf in s.split('$▓㊣$'):
                if len(sf) > 34:
                    file_list.append(sf)
    return render_template('Blogger/photo_list.html', image_list=file_list)

# 判断图片格式
def allowed_file(filename_Format):
  return '.' in filename_Format and \
      filename_Format.rsplit('.', 1)[1] in ALLOW_EXTENSIONS

# nowtime = datetime.datetime.now().strftime('%Y-%m-%d')
# def potime_name():
#     global nowtime
#     potime = request.args.get('nowtime')
#     potime = nowtime
#     return potime

@app.route('/upload', methods=['POST'])
def view_upload():
    global potime
    myfile = request.files.get('myfile')
    if isinstance(myfile, FileStorage):
        new_name = random_filename(myfile.filename)
        if allowed_file(new_name):
            sql_poall = Photo.query.filter_by(p_time = potime).first()
            if sql_poall in [None, '']:
                print('*'*90)
                print(sql_poall)
                print(potime)
                abort(400)
            else:
                sqlponame_list = sql_poall.p_name
                Photo.query.filter_by(p_time = potime).update({'p_name' : sqlponame_list + '@@' + '$▓㊣$' + new_name})
                db.session.commit()
                save_path = os.path.join(app.upload_folder, new_name)
                myfile.save(save_path)
                return redirect(url_for('view_demo'))
        else:
            abort(400)
    else:
        abort(400)


@app.route('/image/<path:filename>')
def view_image(filename):
    full_path = os.path.join(app.upload_folder, filename)
    if not os.path.exists(full_path):
        return abort(404)
    return send_from_directory(app.upload_folder, filename)

@app.route('/demo')
def view_demo():
    '''
    # 从数据库中读出来的列表

    file_list = [
        '52508804ef2a522f9295c59865d00c08@1235464.jpg',
        'eb6a60e57f7c5e5985befc0380168c6c@asd12543.jpg'
    ]
    '''
    # @@2018-11-13$▓㊣$e742557bd90457ba9499a2baa792fd2c@Tulips.jpg@@2018-11-13$▓㊣$e742557bd90457ba9499a2baa792fd2c@Tulips.jpg 
    # '☞'+ str(potime) + '$▓㊣$' + new_name
    global potime
    # file_list = os.listdir(app.upload_folder)
    file_list = []
    sql_poall = Photo.query.filter_by(p_time = potime).first()
    if sql_poall in [None, '']:
        pass
    else:
        sqlponame_list = sql_poall.p_name
        # 划分字符串
        time_filename = sqlponame_list
        ss_list = time_filename.split('@@')
        ss_list.remove(ss_list[0])
        file_list =[]
        for s in ss_list:
            for sf in s.split('$▓㊣$'):
                if len(sf) > 34:
                    file_list.append(sf)
    print('*' * 90)
    print(file_list)
    return render_template('Blogger/photo_list.html', image_list=file_list)

app.register_blueprint(page_bp)
app.register_blueprint(blogger_bp)



if __name__ == '__main__':
    run_cfg = {
        'host': '0.0.0.0',
        'port': 9876,
        'debug': True 
    }
    app.run(**run_cfg)