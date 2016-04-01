# coding: utf-8

"""
    about types :
    0 => 国创
    1 => 上创
    2 => sitp
    3 => 挑战杯
    4 => 创新赛事
    5 => 企业课题
    6 => 创业项目
    7 => 其他

    about project status

    0 => 已创建, 等待加人中
    1 => 人员已满, 未开始
    2 => 已向管理员申请开始, 未通过
    3 => 已通过,开始提交资料

"""

from datetime import datetime


def handle_project_creation_form(form, creator_id):
    project = {}
    project['creator'] = {}
    project['creator']['id'] = creator_id
    project['creator']['name'] = form['creator_name']
    role = transform_roles(form['creator_role'])
    project['team'] = {}
    project['team']['charge_person'] = []
    project['team']['member'] = []
    project['team']['mentor'] = []
    project['team']['outside_mentor'] = []
    project['team'][role].append(dict(id=creator_id,name=form['creator_name']))
    project['name'] = form['project_name']
    project['created_time'] = datetime.now()
    project['status'] = 0
    project['types'] = []
    if form.has_key('guochuang'):
        project['types'].append(0)
    if form.has_key('shangchuang'):
        project['types'].append(1)
    if form.has_key('sitp'):
        project['types'].append(2)
    if form.has_key('tiaozhanbei'):
        project['types'].append(3)
    if form.has_key('chuangxin'):
        project['types'].append(4)
    if form.has_key('qiye'):
        project['types'].append(5)
    if form.has_key('chuangye'):
        project['types'].append(6)
    if form.has_key('other'):
        project['types'].append(7)
    project['member_number'] = int(form['member_number'])
    project['member_demand'] = form['member_demand']
    project['deadline'] = form['deadline']
    project['keyword'] = form['keywords'].split()
    project['basic'] = form['project_basic']
    project['introduction'] = form['project_introduction']

    return project


def handle_join_project_form(form):
    message = {}
    message['type'] = 'join'
    message['applier'] = {}
    message['applier']['name'] = form['applier-name']
    message['applier']['id'] = form['username']
    message['apply_role'] = transform_roles(form['apply-role'])
    message['apply-reason'] = form['apply-reason']
    message['project-id'] = form['project-id']
    return message


def transform_roles(role):
    roles = ['charge_person', 'member', 'mentor', 'outside_mentor']
    role_index = int(role)
    return roles[role_index]