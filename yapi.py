import os
import json
import requests

# your yapi session
yapi_host = 'http://192.168.10.16:3000'
project_token = '283f06fb79b76bf03ee03fc4e91bf69a80e5ccf343dabb0af674cdfbf7c19ca9'

# your django
django_host = 'http://127.0.0.1:5678'

# your django viewset apis
django_apis = [
    {
        'catid': 379, # your yapi project's category id
        'apis': [
            # project
            {'name': 'project-option', 'path': '/api/v1/project/projects/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'project-list', 'path': '/api/v1/project/projects/', 'method': 'GET', 'action': 'list'},
            {'name': 'project-create', 'path': '/api/v1/project/projects/', 'method': 'POST', 'action': 'create'},
            {'name': 'project-retrieve', 'path': '/api/v1/project/projects/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'project-update', 'path': '/api/v1/project/projects/{uuid}/', 'method': 'PUT', 'action': 'update'},
            {'name': 'project-patch-update', 'path': '/api/v1/project/projects/{uuid}/', 'method': 'PATCH', 'action': 'patch-update'},
            {'name': 'project-delete', 'path': '/api/v1/project/projects/{uuid}/', 'method': 'DELETE', 'action': 'delete'},
        ]
    },
]

def get_django_api_meta(api_path):
    url = django_host + api_path
    headers = {}

    response = requests.options(url, headers=headers)
    data = json.loads(response.content)
    return data['actions']['POST']

def list_data(api):
    meta_data = get_django_api_meta(api['path'])
    res_body = {"type": "object", "properties": {"results": {"type": "array", "items": {"type": "object", "properties": {}}}}}

    order_fields = []
    filter_fields = []
    for k, v in meta_data.items():
        value = {'type': v['type'], 'description': v['label']}
        if v.get('filter'):
            filter_fields.append(k)
        if v.get('order'):
            order_fields.append(k)
        res_body['properties']['results']['items']['properties'][k] = value

    req_query = [{'name': 'page', 'required': 0},
                 {'name': 'page_size', 'required': 0},
                 {'name': 'ordering', 'required': 0, 'desc': str(order_fields)},
                 {'name': 'search', 'required': 0, 'desc': str(filter_fields)}]
    data = {
        "method": api['method'],
        'title': api['name'],
        'path': api['path'],

        "status": "undone",
        "res_body_type": "json",
        "res_body_is_json_schema": True,
        'res_body': json.dumps(res_body),

        'req_query': req_query,
        'req_headers': [],
        "req_body_form": [],
        "switch_notice": False,
        "message": "",
        "desc": "<p>列表页<br></p>",
        "req_params": []
    }
    return data

def create_data(api):
    meta_data = get_django_api_meta(api['path'])
    res_body = {"type": "object", "properties": {"results": {"type": "object", "properties": {}}}}
    req_body = {"type": "object", "required": [], "properties": {}}
    for k, v in meta_data.items():
        res_body['properties']['results']['properties'][k] = {'type': v['type'], 'description': v['label']}
        req_value = {"type": v['type'], "description": v['label']}

        if v['required']:
            req_body['required'].append(k)

        if v['type'] == 'choice':
            req_value['enum'] = v['choices']
        req_body['properties'][k] = req_value

    data = {
        "method": api['method'],
        'title': api['name'],
        'path': api['path'],

        "status": "undone",
        "res_body_type": "json",
        "res_body_is_json_schema": True,
        'res_body': json.dumps(res_body),

        'req_query': [],
        'req_headers': [],
        'req_body_form': [],
        "req_body_type": "json",
        "req_body_is_json_schema": True,
        "req_body_other": json.dumps(req_body),
        "switch_notice": False,
        "message": "",
        "desc": "<p>创建</p>",
        "req_params": []
    }
    return data

def retrieve_data(api):
    meta_data = get_django_api_meta(api['path'][:-7])
    res_body = {"type": "object", "properties": {"results": {"type": "object", "properties": {}}}}
    for k, v in meta_data.items():
        res_body['properties']['results']['properties'][k] = {'type': v['type'], 'description': v['label']}

    data = {
        "method": api['method'],
        'title': api['name'],
        'path': api['path'],

        "status": "undone",
        "res_body_type": "json",
        "res_body_is_json_schema": True,
        'res_body': json.dumps(res_body),

        'req_query': [],
        'req_headers': [],
        "req_body_form": [],
        "switch_notice": False,
        "message": "",
        "desc": "<p>详情页</p>",
        "req_params": []
    }
    return data

def update_data(api):
    meta_data = get_django_api_meta(api['path'][:-7])
    res_body = {"type": "object", "properties": {"results": {"type": "object", "properties": {}}}}
    req_body = {"type": "object", "required": [], "properties": {}}
    for k, v in meta_data.items():
        res_body['properties']['results']['properties'][k] = {'type': v['type'], 'description': v['label']}
        req_value = {"type": v['type'], "description": v['label']}

        if v['required']:
            req_body['required'].append(k)

        if v['type'] == 'choice':
            req_value['enum'] = v['choices']
        req_body['properties'][k] = req_value
    data = {
        "method": api['method'],
        'title': api['name'],
        'path': api['path'],

        "status": "undone",
        "res_body_type": "json",
        "res_body_is_json_schema": True,
        'res_body': json.dumps(res_body),

        'req_query': [],
        'req_headers': [],
        "req_body_form": [],
        "req_body_type": "json",
        "req_body_is_json_schema": True,
        "req_body_other": json.dumps(req_body),
        "switch_notice": False,
        "message": "",
        "desc": "<p>全字段更新</p>",
        "req_params": []
    }
    return data

def patch_update_data(api):
    meta_data = get_django_api_meta(api['path'][:-7])
    res_body = {"type": "object", "properties": {"results": {"type": "object", "properties": {}}}}
    req_body = {"type": "object", "required": [], "properties": {}}
    for k, v in meta_data.items():
        res_body['properties']['results']['properties'][k] = {'type': v['type'], 'description': v['label']}
        req_value = {"type": v['type'], "description": v['label']}

        if v['required']:
            req_body['required'].append(k)

        if v['type'] == 'choice':
            req_value['enum'] = v['choices']
        req_body['properties'][k] = req_value
    data = {
        "method": api['method'],
        'title': api['name'],
        'path': api['path'],

        "status": "undone",
        "res_body_type": "json",
        "res_body_is_json_schema": True,
        'res_body': json.dumps(res_body),

        'req_query': [],
        'req_headers': [],
        "req_body_form": [],
        "req_body_type": "json",
        "req_body_is_json_schema": True,
        "req_body_other": json.dumps(req_body),
        "switch_notice": False,
        "message": "",
        "desc": "<p>全字段更新</p>",
        "req_params": []
    }
    return data

def delete_data(api):
    meta_data = {'msg': 'OK'}
    data = {
        "method": api['method'],
        'title': api['name'],
        'path': api['path'],

        "status": "undone",
        "res_body_type": "json",
        "req_body_is_json_schema": True,
        'res_body': json.dumps(meta_data),

        'req_query': [],
        'req_headers': [],
        "req_body_form": [],
        "switch_notice": False,
        "message": "",
        "desc": "<p>删除</p>",
        "req_params": []
    }
    return data

def option_data(api):
    meta_data = get_django_api_meta(api['path'])

    data = {
        "method": api['method'],
        'title': api['name'],
        'path': api['path'],

        "status": "undone",
        "res_body_type": "json",
        "res_body_is_json_schema": False,
        'res_body': json.dumps(meta_data),

        'req_query': [],
        'req_headers': [],
        "req_body_form": [],
        "req_body_type": "json",
        "req_body_is_json_schema": False,
        "req_body_other": "",
        "switch_notice": False,
        "message": "",
        "desc": "<p>API Meta</p>",
        "req_params": []
    }
    return data

def add_yapi():
    url = yapi_host + '/api/interface/add'
    headers = {'Content-Type': 'application/json'}
    for django_api in django_apis:
        catid = django_api['catid']
        for api in django_api['apis']:
            action = api['action']
            path = api['path']
            if action == 'list':
                data = list_data(api)
            elif action == 'create':
                data = create_data(api)
            elif action == 'retrieve':
                data = retrieve_data(api)
            elif action == 'update':
                data = update_data(api)
            elif action == 'patch-update':
                data = patch_update_data(api)
            elif action == 'delete':
                data = delete_data(api)
            elif action == 'option':
                data = option_data(api)

            data.update({'token': project_token, 'catid': catid})
            response = requests.post(url, json=data, headers=headers)
            print(json.loads(response.content))


if __name__ == '__main__':
    add_yapi()
