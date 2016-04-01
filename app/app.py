# coding: utf-8
from flask import Flask, render_template, request, session, redirect, url_for, jsonify, Response
from module import auth, project_manager, form
from bson import json_util
from flask_restful import Resource, Api
from module.project_manager import ProjectManager
from module.message_manager import MessageManager
app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

api = Api(app)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/project/create', methods=['GET', 'POST'])
def create_project():
    if request.method == 'GET':
        return render_template('create_project.html')
    project = form.handle_project_creation_form(request.form, session['username'])
    result = ProjectManager().create_project(project)
    if result:
        return redirect(url_for('get_all_project'))
    else:
        return redirect(url_for('get_all_project'))


@app.context_processor
def test():
    def display():
        return '你好'

    return dict(display=display)


@app.route('/project/all', methods=['GET'])
def get_all_project():

    projects = ProjectManager().find_all_project()

    return render_template('project_display.html',
                           projects=projects,
                           cal_member=project_manager.cal_member)

    # raw = json_util.dumps(projects,ensure_ascii = False, indent=4)
    # resp = Response(response=raw, status=200, content_type='application/json; charset=utf-8')
    # return resp


@app.route('/project/user/', methods=['GET'])
def get_user_projects():
    username = session['username']
    projects = ProjectManager().find_all_project_by_username(username)
    return render_template('manage_project.html', projects=projects)


@app.route('/project/join', methods=['POST'])
def join_project():
    join_msg = form.handle_join_project_form(request.form)
    join_msg['project'] = {}
    project = ProjectManager().find_project_by_id(join_msg['project-id'])
    join_msg['project']['name'] = project['name']
    join_msg['project']['id'] = project['_id']
    join_msg['sender'] = session['username']
    join_msg['receiver'] = project['creator']['id']
    join_msg['status'] = 0
    result = MessageManager().add_message(join_msg)
    return redirect(url_for('get_all_project'))


@app.route('/_add_member')
def add_numbers():
    join_info = {}
    message_id = request.args.get('message-id',None)
    join_info['project-id'] = request.args.get('project-id',None)
    join_info['apply-role'] = request.args.get('apply-role',None)
    join_info['applier-id'] = request.args.get('applier-id',None)
    join_info['applier-name'] = request.args.get('applier-name',None)
    result = ProjectManager().add_member(join_info)
    if result:
        MessageManager().expire_message(message_id)
    return jsonify(result='123')


@app.route('/message/user/', methods=['GET'])
def get_message():
    messages = MessageManager().find_message_for_receiver(session['username'])
    print messages
    return render_template('manage_message.html', messages=messages)


@app.route('/auth/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    username = request.form['username']
    password = request.form['password']
    if auth.signup(username, password):
        session['username'] = username
        return render_template('homepage.html')
    else:
        error = 'sign up failed'
        return render_template('signup.html')


@app.route('/auth/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return render_template('login.html')


@app.route('/auth/login', methods=['POST', 'GET'])
def login():
    if 'username' in session:
        return render_template('homepage.html')
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    if auth.valid_login(username, password):
        session['username'] = username
        return render_template('homepage.html')
    else:
        error = 'invalid username/password'
        return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)