# coding: utf-8
from flask import Flask, render_template, request, session, redirect, url_for, jsonify, Response, g, abort
from module import authority, project, form
from bson import json_util
from module.project import ProjectManager
from module import message_mgr
from flask_httpauth import HTTPBasicAuth
from module.token import verify_auth_token, generate_auth_token, set_token_key
from module.application import ApplicationManager
from flask_cors import CORS


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
CORS(app)


# extensions

auth = HTTPBasicAuth()

# module init

# token module
set_token_key(app.secret_key)


@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    optional_id = verify_auth_token(username_or_token)
    if not optional_id:
        # try to authenticate with username/password
        if authority.valid_login(username_or_token, password):
            return True
        else:
            return False
    return True

# token resource


@app.route('/token', methods=['POST'])
@auth.login_required
def get_auth_token():
    token = generate_auth_token(g.user['username'])
    return jsonify({'data': {'token': token.decode('ascii'),'user': g.user}})


# user resource

@app.route('/user', methods=['POST'])
def create_user():
    user = request.json
    result = authority.signup(user['username'], user['password'])
    return jsonify({'result': 'success'})


# projects resource

@app.route('/projects', methods=['GET'])
@auth.login_required
def get_projects():
    offset = int(request.args.get('offset', 0))
    limit = int(request.args.get('limit', 5))
    status = request.args.get('status', None)
    projects = ProjectManager().find_all_project(offset=offset, limit=limit, status=status)
    data = {'data': projects}
    raw = json_util.dumps(data, ensure_ascii= False, indent=4)
    resp = Response(response=raw, status=200, content_type='application/json; charset=utf-8')
    return resp


@app.route('/project', methods=['POST'])
@auth.login_required
def new_project():
    project = request.json
    ProjectManager().create_project(project)
    return '213'


@app.route('/user/<username>/projects', methods=['GET'])
@auth.login_required
def get_projects_of_user(username):
    projects = ProjectManager().find_all_project_by_username(username)
    raw = json_util.dumps(projects, ensure_ascii=False, indent=4)
    resp = Response(response=raw, status=200, content_type='application/json; charset=utf-8')
    return resp

# message


@app.route('/user/<username>/messages', methods=['GET'])
@auth.login_required
def get_message_of_username(username):
    messages = message_mgr.find_message_for_receiver(username)
    data = {'data': messages}
    raw = json_util.dumps(data, ensure_ascii= False, indent=4)
    resp = Response(response=raw, status=200, content_type='application/json; charset=utf-8')
    return resp


# application

@app.route('/application', methods=['POST'])
@auth.login_required
def create_application():
    application = request.json
    result = ApplicationManager.insert_application(application)
    return jsonify({'result': 'success'})


@app.route('/application/<application_id>/approval', methods=['POST'])
@auth.login_required
def approve_application(application_id):
    ApplicationManager.approve_application(application_id)
    return jsonify({'result': 'success'})

# admin operation


@app.route('/admin/project/<project_id>/approval', methods=['POST'])
@auth.login_required
def approve_project(project_id):
    ProjectManager().approve_project(project_id)
    return jsonify({'result': 'success'})

@app.route('/')
def index():
    return 'nothing happen !'


if __name__ == '__main__':
    app.run(debug=True)