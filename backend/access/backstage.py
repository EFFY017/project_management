import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__) , '..'))

from flask import json, Blueprint
from logic import login, user
from util.access import *

backstage_access = Blueprint('backstage_access', __name__)

@backstage_access.route('/login', methods=['POST'])
def back_login():
    request_data = get_value_dict()
    if not check_dict(request_data, ['username', 'password']):
        return json.dumps('PARAM ERROR')

    data = login.login_super(request_data['username'], request_data['password'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@backstage_access.route('/create_super_account', methods=['POST'])
def back_create_super_account():
    request_data = get_value_dict()
    if not check_dict(request_data, ['username', 'password']):
        return json.dumps('PARAM ERROR')

    data = user.create_super_account(request_data['username'], request_data['password'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@backstage_access.route('/create_normal_account', methods=['POST'])
def back_create_normal_account():
    request_data = get_value_dict()
    if not check_dict(request_data, ['username', 'password', 'name', 'career', 'department']):
        return json.dumps('PARAM ERROR')

    data = user.create_normal_account(request_data['username'], request_data['password'], request_data['name'], request_data['career'], request_data['department'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@backstage_access.route('/delete_normal_account', methods=['POST'])
def back_delete_normal_account():
    request_data = get_value_dict()
    if not check_dict(request_data, ['username']):
        return json.dumps('PARAM ERROR')

    data = user.delete_normal_account(request_data['username'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@backstage_access.route('/modify_normal_account', methods=['POST'])
def back_modify_normal_account():
    request_data = get_value_dict()
    if not check_dict(request_data, ['username', 'password', 'name', 'career', 'department']):
        return json.dumps('PARAM ERROR')

    data = user.modify_normal_account(request_data['username'], request_data['password'], request_data['name'], request_data['career'], request_data['department'])

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps({'status': data})

@backstage_access.route('/show_normal_account', methods=['GET'])
def back_show_normal_account():
    request_data = get_value_dict()
    if not check_dict(request_data, ['username']):
        return json.dumps('PARAM ERROR')

    data = user.get_normal_account()

    if has_error(data):
        return json.dumps('BACKEND ERROR')
    else:
        return json.dumps(data)

@backstage_access.route('/export_normal_account_sample', methods=['GET'])
def back_export_normal_account_sample():
    # download file
    # file
    return json.dumps({'status': 'ok'})

@backstage_access.route('/import_normal_account', methods=['POST'])
def back_import_normal_account():
    # upload file
    # status: "ok"
    return json.dumps({'status': 'ok'})
