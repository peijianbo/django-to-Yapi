import os
import json
import requests

yapi_host = 'http://192.168.10.16:3000'
cookie = '_yapi_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOjEzLCJpYXQiOjE2MzU1MDEzMDEsImV4cCI6MTYzNjEwNjEwMX0.McvHxRxMW59nqiDpK1pXuqx1f44WZ5v0dFOvnUBU01I; _yapi_uid=13'
project_token = 'a45042651a6e9edffff97c51c648e6d64609303f24bf5e766de6b3626dc0c518'
project_id = 95

django_host = 'http://127.0.0.1:6789'
django_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OTk5OSwidXNlcm5hbWUiOiJcdTgzZTBcdTgzZGMiLCJ0ZW5hbnRfaWQiOiJwcm9qZWN0X3RlbmFudF8xIn0.MoEGpFMHC6HYOFCcyVfxDfRxerOdL97amNlYhIv-hFA'
django_apis = [
    {
        'category': '数据库管理',
        'apis': [
            # database
            {'name': 'database-option', 'path': '/api/v1/database/databases/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'database-list', 'path': '/api/v1/database/databases/', 'method': 'GET', 'action': 'list'},
            {'name': 'database-retrieve', 'path': '/api/v1/database/databases/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
        ]
    },

    {
        'category': '存储管理',
        'apis': [
            # storage
            {'name': 'storage-option', 'path': '/api/v1/storage/storages/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'storage-list', 'path': '/api/v1/storage/storages/', 'method': 'GET', 'action': 'list'},
            {'name': 'storage-retrieve', 'path': '/api/v1/storage/storages/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            # cloud-disk
            {'name': 'cloud-disk-option', 'path': '/api/v1/storage/cloud-disks/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'cloud-disk-list', 'path': '/api/v1/storage/cloud-disks/', 'method': 'GET', 'action': 'list'},
            {'name': 'cloud-disk-retrieve', 'path': '/api/v1/storage/cloud-disks/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
        ]
    },

    {
        'category': '网络管理',
        'apis': [
            # subnet
            {'name': 'subnet-option', 'path': '/api/v1/network/subnets/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'subnet-list', 'path': '/api/v1/network/subnets/', 'method': 'GET', 'action': 'list'},
            {'name': 'subnet-retrieve', 'path': '/api/v1/network/subnets/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            # load-balance
            {'name': 'load-balance-option', 'path': '/api/v1/network/load-balances/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'load-balance-list', 'path': '/api/v1/network/load-balances/', 'method': 'GET', 'action': 'list'},
            {'name': 'load-balance-retrieve', 'path': '/api/v1/network/load-balances/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
        ]
    },

    {
        'category': '基础设施-机柜管理',
        'apis': [
            # cabinet
            {'name': 'cabinet-option', 'path': '/api/v1/infrastructure/cabinets/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'cabinet-list', 'path': '/api/v1/infrastructure/cabinets/', 'method': 'GET', 'action': 'list'},
            {'name': 'cabinet-retrieve', 'path': '/api/v1/infrastructure/cabinets/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'cabinet-create', 'path': '/api/v1/infrastructure/cabinets/', 'method': 'POST', 'action': 'create'},
            {'name': 'cabinet-update', 'path': '/api/v1/infrastructure/cabinets/{uuid}/', 'method': 'PUT', 'action': 'update'},
            {'name': 'cabinet-patch-update', 'path': '/api/v1/infrastructure/cabinets/{uuid}/', 'method': 'PATCH', 'action': 'patch-update'},
            {'name': 'cabinet-batch-import', 'path': '/api/v1/infrastructure/cabinets/batch-import/', 'method': 'POST', 'action': 'batch-import', 'comment': '批量导入'},
            {'name': 'cabinet-operate-status', 'path': '/api/v1/infrastructure/cabinets/operate-status/', 'method': 'POST', 'action': 'operate-status', 'comment': '上架/下架'},
        ]
    },
    {
        'category': '基础设施-网络设备',
        'apis': [
            # net device
            {'name': 'net-device-option', 'path': '/api/v1/infrastructure/net-devices/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'net-device-list', 'path': '/api/v1/infrastructure/net-devices/', 'method': 'GET', 'action': 'list'},
            {'name': 'net-device-retrieve', 'path': '/api/v1/infrastructure/net-devices/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'net-device-create', 'path': '/api/v1/infrastructure/net-devices/', 'method': 'POST', 'action': 'create'},
            {'name': 'net-device-update', 'path': '/api/v1/infrastructure/net-devices/{uuid}/', 'method': 'PUT', 'action': 'update'},
            {'name': 'net-device-patch-update', 'path': '/api/v1/infrastructure/net-devices/{uuid}/', 'method': 'PATCH', 'action': 'patch-update'},
            {'name': 'net-device-delete', 'path': '/api/v1/infrastructure/net-devices/{uuid}/', 'method': 'DELETE', 'action': 'delete'},
            {'name': 'net-device-batch-import', 'path': '/api/v1/infrastructure/net-devices/batch-import/', 'method': 'POST', 'action': 'batch-import', 'comment': '批量导入'},

            {'name': 'net-device-spec-option', 'path': '/api/v1/infrastructure/net-device-specs/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'net-device-spec-list', 'path': '/api/v1/infrastructure/net-device-specs/', 'method': 'GET', 'action': 'list'},
            {'name': 'net-device-spec-retrieve', 'path': '/api/v1/infrastructure/net-device-specs/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'net-device-spec-delete', 'path': '/api/v1/infrastructure/net-device-specs/{uuid}/', 'method': 'DELETE', 'action': 'delete'},
        ]
    },
    {
        'category': '基础设施-物理机管理',
        'apis': [
            # machine
            {'name': 'machine-option', 'path': '/api/v1/infrastructure/machines/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'machine-list', 'path': '/api/v1/infrastructure/machines/', 'method': 'GET', 'action': 'list'},
            {'name': 'machine-retrieve', 'path': '/api/v1/infrastructure/machines/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'machine-create', 'path': '/api/v1/infrastructure/machines/', 'method': 'POST', 'action': 'create'},
            {'name': 'machine-update', 'path': '/api/v1/infrastructure/machines/{uuid}/', 'method': 'PUT', 'action': 'update'},
            {'name': 'machine-patch-update', 'path': '/api/v1/infrastructure/machines/{uuid}/', 'method': 'PATCH', 'action': 'patch-update'},
            {'name': 'machine-batch-import', 'path': '/api/v1/infrastructure/machines/batch-import/', 'method': 'POST', 'action': 'batch-import', 'comment': '批量导入'},
            {'name': 'machine-batch-import-accessory', 'path': '/api/v1/infrastructure/machines/batch-import-accessory/', 'method': 'POST', 'action': 'batch-import-accessory', 'comment': '批量导入配件(内存/磁盘/电源)'},
            {'name': 'machine-reform', 'path': '/api/v1/infrastructure/machines/{uuid}/reform/', 'method': 'POST', 'action': 'reform', 'comment': '设备改造'},

            {'name': 'machine-spec-option', 'path': '/api/v1/infrastructure/machine-specs/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'machine-spec-list', 'path': '/api/v1/infrastructure/machine-specs/', 'method': 'GET', 'action': 'list'},
            {'name': 'machine-spec-retrieve', 'path': '/api/v1/infrastructure/machine-specs/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'machine-spec-create', 'path': '/api/v1/infrastructure/machine-specs/', 'method': 'POST', 'action': 'create'},
            {'name': 'machine-spec-delete', 'path': '/api/v1/infrastructure/machine-specs/{uuid}/', 'method': 'DELETE', 'action': 'delete'},

            {'name': 'machine-type-option', 'path': '/api/v1/infrastructure/machine-types/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'machine-type-list', 'path': '/api/v1/infrastructure/machine-types/', 'method': 'GET', 'action': 'list'},
            {'name': 'machine-type-retrieve', 'path': '/api/v1/infrastructure/machine-types/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'machine-type-create', 'path': '/api/v1/infrastructure/machine-types/', 'method': 'POST', 'action': 'create'},
            {'name': 'machine-type-delete', 'path': '/api/v1/infrastructure/machine-types/{uuid}/', 'method': 'DELETE', 'action': 'delete'},
        ]
    },
    {
        'category': '基础设施-内存',
        'apis': [
            # ram
            {'name': 'ram-option', 'path': '/api/v1/infrastructure/rams/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'ram-list', 'path': '/api/v1/infrastructure/rams/', 'method': 'GET', 'action': 'list'},
            {'name': 'ram-retrieve', 'path': '/api/v1/infrastructure/rams/{uuid}/', 'method': 'GET', 'action': 'retrieve'},

            {'name': 'ram-stock-option', 'path': '/api/v1/infrastructure/ram-stocks/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'ram-stock-list', 'path': '/api/v1/infrastructure/ram-stocks/', 'method': 'GET', 'action': 'list'},
            {'name': 'ram-stock-retrieve', 'path': '/api/v1/infrastructure/ram-stocks/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'ram-stock-create', 'path': '/api/v1/infrastructure/ram-stocks/{uuid}/', 'method': 'POST', 'action': 'create'},
            {'name': 'ram-stock-batch-import', 'path': '/api/v1/infrastructure/ram-stocks/batch-import/', 'method': 'POST', 'action': 'batch-import', 'comment': '批量导入'},

            {'name': 'ram-spec-option', 'path': '/api/v1/infrastructure/ram-specs/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'ram-spec-list', 'path': '/api/v1/infrastructure/ram-specs/', 'method': 'GET', 'action': 'list'},
            {'name': 'ram-spec-retrieve', 'path': '/api/v1/infrastructure/ram-specs/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'ram-spec-create', 'path': '/api/v1/infrastructure/ram-specs/', 'method': 'POST', 'action': 'create'},
            {'name': 'ram-spec-delete', 'path': '/api/v1/infrastructure/ram-specs/{uuid}/', 'method': 'DELETE', 'action': 'delete'},
        ]
    },
    {
        'category': '基础设施-磁盘',
        'apis': [
            # disk
            {'name': 'disk-option', 'path': '/api/v1/infrastructure/disks/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'disk-list', 'path': '/api/v1/infrastructure/disks/', 'method': 'GET', 'action': 'list'},
            {'name': 'disk-retrieve', 'path': '/api/v1/infrastructure/disks/{uuid}/', 'method': 'GET', 'action': 'retrieve'},

            {'name': 'disk-stock-option', 'path': '/api/v1/infrastructure/disk-stocks/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'disk-stock-list', 'path': '/api/v1/infrastructure/disk-stocks/', 'method': 'GET', 'action': 'list'},
            {'name': 'disk-stock-retrieve', 'path': '/api/v1/infrastructure/disk-stocks/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'disk-stock-create', 'path': '/api/v1/infrastructure/disk-stocks/{uuid}/', 'method': 'POST', 'action': 'create'},
            {'name': 'disk-stock-batch-import', 'path': '/api/v1/infrastructure/disk-stocks/batch-import/', 'method': 'POST', 'action': 'batch-import', 'comment': '批量导入'},
            {'name': 'disk-spec-option', 'path': '/api/v1/infrastructure/disk-specs/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'disk-spec-list', 'path': '/api/v1/infrastructure/disk-specs/', 'method': 'GET', 'action': 'list'},
            {'name': 'disk-spec-retrieve', 'path': '/api/v1/infrastructure/disk-specs/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'disk-spec-create', 'path': '/api/v1/infrastructure/disk-specs/', 'method': 'POST', 'action': 'create'},
            {'name': 'disk-spec-delete', 'path': '/api/v1/infrastructure/disk-specs/{uuid}/', 'method': 'DELETE', 'action': 'delete'},
        ]
    },
    {
        'category': '基础设施-光模块',
        'apis': [
            # optical module
            {'name': 'optical-module-option', 'path': '/api/v1/infrastructure/optical-modules/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'optical-module-list', 'path': '/api/v1/infrastructure/optical-modules/', 'method': 'GET', 'action': 'list'},
            {'name': 'optical-module-retrieve', 'path': '/api/v1/infrastructure/optical-modules/{uuid}/', 'method': 'GET', 'action': 'retrieve'},

            {'name': 'optical-module-stock-option', 'path': '/api/v1/infrastructure/optical-module-stocks/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'optical-module-stock-list', 'path': '/api/v1/infrastructure/optical-module-stocks/', 'method': 'GET', 'action': 'list'},
            {'name': 'optical-module-stock-retrieve', 'path': '/api/v1/infrastructure/optical-module-stocks/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'optical-module-stock-create', 'path': '/api/v1/infrastructure/optical-module-stocks/{uuid}/', 'method': 'POST', 'action': 'create'},
            {'name': 'optical-module-stock-batch-import', 'path': '/api/v1/infrastructure/optical-module-stocks/batch-import/', 'method': 'POST', 'action': 'batch-import', 'comment': '批量导入'},
            {'name': 'optical-module-spec-option', 'path': '/api/v1/infrastructure/optical-module-specs/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'optical-module-spec-list', 'path': '/api/v1/infrastructure/optical-module-specs/', 'method': 'GET', 'action': 'list'},
            {'name': 'optical-module-spec-retrieve', 'path': '/api/v1/infrastructure/optical-module-specs/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'optical-module-spec-create', 'path': '/api/v1/infrastructure/optical-module-specs/', 'method': 'POST', 'action': 'create'},
            {'name': 'optical-module-spec-delete', 'path': '/api/v1/infrastructure/optical-module-specs/{uuid}/', 'method': 'DELETE', 'action': 'delete'},
        ]
    },
    {
        'category': '基础设施-电源',
        'apis': [
            # power
            {'name': 'power-module-option', 'path': '/api/v1/infrastructure/power-modules/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'power-module-list', 'path': '/api/v1/infrastructure/power-modules/', 'method': 'GET', 'action': 'list'},
            {'name': 'power-module-retrieve', 'path': '/api/v1/infrastructure/power-modules/{uuid}/', 'method': 'GET', 'action': 'retrieve'},

            {'name': 'power-module-stock-option', 'path': '/api/v1/infrastructure/power-module-stocks/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'power-module-stock-list', 'path': '/api/v1/infrastructure/power-module-stocks/', 'method': 'GET', 'action': 'list'},
            {'name': 'power-module-stock-retrieve', 'path': '/api/v1/infrastructure/power-module-stocks/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'power-module-stock-create', 'path': '/api/v1/infrastructure/power-module-stocks/{uuid}/', 'method': 'POST', 'action': 'create'},
            {'name': 'power-module-stock-batch-import', 'path': '/api/v1/infrastructure/power-module-stocks/batch-import/', 'method': 'POST', 'action': 'batch-import', 'comment': '批量导入'},
            {'name': 'power-module-spec-option', 'path': '/api/v1/infrastructure/power-module-specs/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'power-module-spec-list', 'path': '/api/v1/infrastructure/power-module-specs/', 'method': 'GET', 'action': 'list'},
            {'name': 'power-module-spec-retrieve', 'path': '/api/v1/infrastructure/power-module-specs/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'power-module-spec-create', 'path': '/api/v1/infrastructure/power-module-specs/', 'method': 'POST', 'action': 'create'},
            {'name': 'power-module-spec-delete', 'path': '/api/v1/infrastructure/power-module-specs/{uuid}/', 'method': 'DELETE', 'action': 'delete'},
        ]
    },
    {
        'category': '基础设施-设备端口',
        'apis': [
            # device port
            {'name': 'device-port-option', 'path': '/api/v1/infrastructure/device-ports/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'device-port-list', 'path': '/api/v1/infrastructure/device-ports/', 'method': 'GET', 'action': 'list'},
            {'name': 'device-port-update', 'path': '/api/v1/infrastructure/device-ports/{uuid}/', 'method': 'PUT', 'action': 'update'},
            {'name': 'device-port-patch-update', 'path': '/api/v1/infrastructure/device-ports/{uuid}/', 'method': 'PATCH', 'action': 'patch-update'},
        ]
    },
    {
        'category': '基础设施-IP地址',
        'apis': [
            # IP address
            {'name': 'ip-address-option', 'path': '/api/v1/infrastructure/ip-addresses/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'ip-address-list', 'path': '/api/v1/infrastructure/ip-addresses/', 'method': 'GET', 'action': 'list'},
            {'name': 'ip-address-create', 'path': '/api/v1/infrastructure/ip-addresses/', 'method': 'POST', 'action': 'create'},
            {'name': 'ip-address-retrieve', 'path': '/api/v1/infrastructure/ip-addresses/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'ip-address-update', 'path': '/api/v1/infrastructure/ip-addresses/{uuid}/', 'method': 'PUT', 'action': 'update'},
            {'name': 'ip-address-patch-update', 'path': '/api/v1/infrastructure/ip-addresses/{uuid}/', 'method': 'PATCH', 'action': 'patch-update'},
            {'name': 'ip-address-delete', 'path': '/api/v1/infrastructure/ip-addresses/{uuid}/', 'method': 'DELETE', 'action': 'delete'},
        ]
    },
    {
        'category': '供应商管理',
        'apis': [
            # supplier
            {'name': 'supplier-option', 'path': '/api/v1/supplier/suppliers/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'supplier-list', 'path': '/api/v1/supplier/suppliers/', 'method': 'GET', 'action': 'list'},
            {'name': 'supplier-retrieve', 'path': '/api/v1/supplier/suppliers/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'supplier-create', 'path': '/api/v1/supplier/suppliers/', 'method': 'POST', 'action': 'create'},
            {'name': 'supplier-update', 'path': '/api/v1/supplier/suppliers/{uuid}/', 'method': 'PUT', 'action': 'update'},
            {'name': 'supplier-patch-update', 'path': '/api/v1/supplier/suppliers/{uuid}/', 'method': 'PATCH', 'action': 'patch-update'},
            {'name': 'supplier-delete', 'path': '/api/v1/supplier/suppliers/{uuid}/', 'method': 'DELETE', 'action': 'delete'},

            {'name': 'account-option', 'path': '/api/v1/supplier/cloud-accounts/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'account-list', 'path': '/api/v1/supplier/cloud-accounts/', 'method': 'GET', 'action': 'list'},
            {'name': 'account-retrieve', 'path': '/api/v1/supplier/cloud-accounts/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'account-create', 'path': '/api/v1/supplier/cloud-accounts/', 'method': 'POST', 'action': 'create'},
            {'name': 'account-update', 'path': '/api/v1/supplier/cloud-accounts/{uuid}/', 'method': 'PUT', 'action': 'update'},
            {'name': 'account-patch-update', 'path': '/api/v1/supplier/cloud-accounts/{uuid}/', 'method': 'PATCH', 'action': 'patch-update'},
            {'name': 'account-delete', 'path': '/api/v1/supplier/cloud-accounts/{uuid}/', 'method': 'DELETE', 'action': 'delete'},

            {'name': 'account-type-option', 'path': '/api/v1/supplier/account-types/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'account-type-list', 'path': '/api/v1/supplier/account-types/', 'method': 'GET', 'action': 'list'},
            {'name': 'account-type-retrieve', 'path': '/api/v1/supplier/account-types/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'account-type-create', 'path': '/api/v1/supplier/account-types/', 'method': 'POST', 'action': 'create'},
            {'name': 'account-type-update', 'path': '/api/v1/supplier/account-types/{uuid}/', 'method': 'PUT', 'action': 'update'},
            {'name': 'account-type-patch-update', 'path': '/api/v1/supplier/account-types/{uuid}/', 'method': 'PATCH', 'action': 'patch-update'},
            {'name': 'account-type-delete', 'path': '/api/v1/supplier/account-types/{uuid}/', 'method': 'DELETE', 'action': 'delete'},

            {'name': 'prop-field-option', 'path': '/api/v1/supplier/prop-fields/', 'method': 'OPTIONS', 'action': 'option'},
            {'name': 'prop-field-list', 'path': '/api/v1/supplier/prop-fields/', 'method': 'GET', 'action': 'list'},
            {'name': 'prop-field-retrieve', 'path': '/api/v1/supplier/prop-fields/{uuid}/', 'method': 'GET', 'action': 'retrieve'},
            {'name': 'prop-field-create', 'path': '/api/v1/supplier/prop-fields/', 'method': 'POST', 'action': 'create'},
        ]
    },
]

def get_django_api_meta(api_path):
    url = django_host + '/cmdb' + api_path
    headers = {'authorization': django_token}

    response = requests.options(url, headers=headers)
    data = json.loads(response.content)
    return data

def list_body(api):
    meta_data = get_django_api_meta(api['path'])
    res_body = {"type": "object", "properties": {"results": {"type": "array", "items": {"type": "object", "properties": {}}}}}

    order_fields = meta_data['order_fields']
    filter_fields = meta_data['filter_fields']
    for k, v in meta_data['actions']['GET'].items():
        if v['write_only']:
            continue

        if v['type'] == 'nested object':  # ForeignKey/OneToOne/ManyToMany/serializers.DictField 时为nested object
            properties = {}
            if v.get('children'):
                for c_k, c_v in v.get('children').items():
                    properties[c_k] = {'type': c_v['type'], 'description': c_v['label']}
                value = {'type': 'object', 'properties': properties, 'description': v['label']}
            elif v.get('child'): # serializers.DictField时为child
                value = {'type': 'object', 'description': v['label']}
        elif v['type'] == 'array':
            properties = {}
            if not v.get('child'):# TODO JSONField时也为array
                value = {'type': 'object', 'description': v['label']}
                # continue # JSONField时也为array,所以去掉这个continue了
            elif v.get('child'):
                for c_k, c_v in v.get('child').get('children').items():
                    properties[c_k] = {'type': c_v['type'], 'description': c_v['label']}
                value = {'type': 'array', 'items': {'type': 'object', 'properties': properties}, 'description': v['label']}
        else:
            value = {'type': v['type'], 'description': v['label']}
        res_body['properties']['results']['items']['properties'][k] = value

    req_query = [{'name': 'limit', 'required': 0},
                 {'name': 'offset', 'required': 0},
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

def create_body(api):
    meta_data = get_django_api_meta(api['path'])
    res_body = {"type": "object", "properties": {"results": {"type": "array", "items": {"type": "object", "properties": {}}}}}
    for k, v in meta_data['actions']['GET'].items():
        if v['write_only']:
            continue

        if v['type'] == 'nested object':
            properties = {}
            if v.get('children'):  # serializers.DictField时为child
                for c_k, c_v in v.get('children').items():
                    properties[c_k] = {'type': c_v['type'], 'description': c_v['label']}
                value = {'type': 'object', 'properties': properties, 'description': v['label']}
            elif v.get('child'):
                value = {'type': 'object', 'description': v['label']}
        elif v['type'] == 'array':
            properties = {}
            if not v.get('child'):  # JSONField时也为array
                value = {'type': 'object', 'description': v['label']}
                # continue
            elif v.get('child'):
                for c_k, c_v in v.get('child').get('children').items():
                    properties[c_k] = {'type': c_v['type'], 'description': c_v['label']}
                value = {'type': 'array', 'items': {'type': 'object', 'properties': properties},
                         'description': v['label']}
        else:
            value = {'type': v['type'], 'description': v['label']}
        res_body['properties']['results']['items']['properties'][k] = value

    req_body = {"type": "object", "required": [], "properties": {}}
    for k, v in meta_data['actions']['GET'].items():
        req_value = {"type": v['type'], "description": v['label']}
        if v['read_only']:
            continue
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

def retrieve_body(api):
    meta_data = get_django_api_meta(api['path'][:-7])
    res_body = {"type": "object", "properties": {"results": {"type": "array", "items": {"type": "object", "properties": {}}}}}
    for k, v in meta_data['actions']['GET'].items():
        if v['write_only']:
            continue

        if v['type'] == 'nested object':
            properties = {}
            if v.get('children'):  # serializers.DictField时为child
                for c_k, c_v in v.get('children').items():
                    properties[c_k] = {'type': c_v['type'], 'description': c_v['label']}
                value = {'type': 'object', 'properties': properties, 'description': v['label']}
            elif v.get('child'):
                value = {'type': 'object', 'description': v['label']}
        elif v['type'] == 'array':
            properties = {}
            if not v.get('child'):  # JSONField时也为array
                value = {'type': 'object', 'description': v['label']}
                # continue
            elif v.get('child'):
                for c_k, c_v in v.get('child').get('children').items():
                    properties[c_k] = {'type': c_v['type'], 'description': c_v['label']}
                value = {'type': 'array', 'items': {'type': 'object', 'properties': properties},
                         'description': v['label']}
        else:
            value = {'type': v['type'], 'description': v['label']}
        res_body['properties']['results']['items']['properties'][k] = value

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

def update_body(api):
    meta_data = get_django_api_meta(api['path'][:-7])

    res_body = {"type": "object", "properties": {"results": {"type": "array", "items": {"type": "object", "properties": {}}}}}
    for k, v in meta_data['actions']['GET'].items():
        if v['write_only']:
            continue

        if v['type'] == 'nested object':
            properties = {}
            if v.get('children'):  # serializers.DictField时为child
                for c_k, c_v in v.get('children').items():
                    properties[c_k] = {'type': c_v['type'], 'description': c_v['label']}
                value = {'type': 'object', 'properties': properties, 'description': v['label']}
            elif v.get('child'):
                value = {'type': 'object', 'description': v['label']}
        elif v['type'] == 'array':
            properties = {}
            if not v.get('child'):  # JSONField时也为array
                value = {'type': 'object', 'description': v['label']}
                # continue
            elif v.get('child'):
                for c_k, c_v in v.get('child').get('children').items():
                    properties[c_k] = {'type': c_v['type'], 'description': c_v['label']}
                value = {'type': 'array', 'items': {'type': 'object', 'properties': properties},
                         'description': v['label']}
        else:
            value = {'type': v['type'], 'description': v['label']}
        res_body['properties']['results']['items']['properties'][k] = value

    req_body = {"type": "object", "required": [], "properties": {}}
    for k, v in meta_data['actions']['GET'].items():
        req_value = {"type": v['type'], "description": v['label']}
        if v['read_only']:
            continue
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

def patch_update_body(api):
    meta_data = get_django_api_meta(api['path'][:-7])
    res_body = {"type": "object", "properties": {"results": {"type": "array", "items": {"type": "object", "properties": {}}}}}
    for k, v in meta_data['actions']['GET'].items():
        if v['write_only']:
            continue

        if v['type'] == 'nested object':
            properties = {}
            if v.get('children'):  # serializers.DictField时为child
                for c_k, c_v in v.get('children').items():
                    properties[c_k] = {'type': c_v['type'], 'description': c_v['label']}
                value = {'type': 'object', 'properties': properties, 'description': v['label']}
            elif v.get('child'):
                value = {'type': 'object', 'description': v['label']}
        elif v['type'] == 'array':
            properties = {}
            if not v.get('child'):  # JSONField时也为array
                value = {'type': 'object', 'description': v['label']}
                # continue
            elif v.get('child'):
                for c_k, c_v in v.get('child').get('children').items():
                    properties[c_k] = {'type': c_v['type'], 'description': c_v['label']}
                value = {'type': 'array', 'items': {'type': 'object', 'properties': properties},
                         'description': v['label']}
        else:
            value = {'type': v['type'], 'description': v['label']}
        res_body['properties']['results']['items']['properties'][k] = value

    req_body = {"type": "object", "required": [], "properties": {}}
    for k, v in meta_data['actions']['GET'].items():
        req_value = {"type": v['type'], "description": v['label']}
        if v['read_only']:
            continue
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
        "desc": "<p>部分字段更新</p>",
        "req_params": []
    }
    return data

def delete_body(api):
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

def option_body(api):
    meta_data = get_django_api_meta(api['path'])

    data = {
        "method": api['method'],
        'title': api['name'],
        'path': api['path'],

        "status": "undone",
        "res_body_type": "json",
        "res_body_is_json_schema": False,
        'res_body': json.dumps(meta_data['actions']['GET']),

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

def empty_body(api):

    data = {
        "method": api['method'],
        'title': api['name'],
        'path': api['path'],

        "status": "undone",
        "res_body_type": "json",
        "res_body_is_json_schema": True,
        'res_body': '',

        'req_query': [],
        'req_headers': [],
        'req_body_form': [],
        "req_body_type": "form",
        "req_body_is_json_schema": False,
        "req_body_other": '',
        "switch_notice": True,
        "message": "",
        "desc": f"<p>{api['comment']}</p>",
        "req_params": []
    }
    return data

def add_category(cat_name):
    headers = {'Content-Type': 'application/json', 'Cookie': cookie}

    # 判断是否存在，存在直接返回分类的name，id
    menu_url = yapi_host + f'/api/interface/list_menu?project_id={project_id}'
    response = requests.get(menu_url, headers=headers)
    cat_list = json.loads(response.content)['data']
    cat_dict = {i['name']: i['_id'] for i in cat_list}
    if cat_name in cat_dict:
        return cat_name, cat_dict[cat_name]

    add_cat_url = yapi_host + '/api/interface/add_cat'
    body = {
        "name": cat_name,
        "project_id": project_id,
        "token": project_token
    }
    response = requests.post(add_cat_url, json=body, headers=headers)
    cat = json.loads(response.content)['data']
    print(f'创建新分类:{cat["name"]}')
    return cat['name'], cat['_id']

def add_yapi():
    add_api_url = yapi_host + '/api/interface/add'

    headers = {'Content-Type': 'application/json'}
    for django_api in django_apis:
        name, id = add_category(django_api['category'])
        for api in django_api['apis']:
            action = api['action']
            path = api['path']
            if action == 'list':
                body = list_body(api)
            elif action == 'create':
                body = create_body(api)
            elif action == 'retrieve':
                body = retrieve_body(api)
            elif action == 'update':
                body = update_body(api)
            elif action == 'patch-update':
                body = patch_update_body(api)
            elif action == 'delete':
                body = delete_body(api)
            elif action == 'option':
                body = option_body(api)
            else:
                body = empty_body(api)

            body.update({'token': project_token, 'catid': id})
            response = requests.post(add_api_url, json=body, headers=headers)
            print(json.loads(response.content))


if __name__ == '__main__':
    add_yapi()
