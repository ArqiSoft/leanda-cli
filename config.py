# _*_ encoding: utf-8 _*_
import os

DEBUG = True

WEB_API_URL = 'https://api.dev.dataledger.io/osdr/v1/api'
IDENTITY_SERVER_URL = 'https://id-dev.your-company.com/auth/realms/OSDR'
if 'WEB_API_URL' in os.environ.keys():
    WEB_API_URL = os.environ['WEB_API_URL']
if 'IDENTITY_SERVER_URL' in os.environ.keys():
    IDENTITY_SERVER_URL = os.environ['IDENTITY_SERVER_URL']

TOKEN_URL = '{}/protocol/openid-connect/token'.format(IDENTITY_SERVER_URL)
ME_URL = '%s/me' % WEB_API_URL

NODE = '%s/nodes/{}' % WEB_API_URL
CONTENTS = '%s/nodes/{}/nodes' % WEB_API_URL
BROWSE_CONTENTS = '%s/nodes/{cwd}/nodes?PageNumber={page}&PageSize={size}' % WEB_API_URL

DOWNLOAD = '%s/blobs/{bucket}/{id}' % WEB_API_URL
UPLOAD = '%s/blobs/{id}' % WEB_API_URL
REMOVE = '%s/nodecollections' % WEB_API_URL

TRAIN = '%s/machinelearning/models' % WEB_API_URL
PREDICT = '%s/machinelearning/predictions' % WEB_API_URL

LIST_MODELS = '%s/entities/files' % WEB_API_URL

FILE = 'File'
FOLDER = 'Folder'

MACHINE_LEARNING_MODEL = {'FileType': 'MachineLearningModel', }

ID_PATTERN = r'([0-9a-f]){8}-([0-9a-f]){4}-([0-9a-f]){4}-([0-9a-f]){4}-([0-9a-f]){12}'

LAST_UPDATED = '.updated.osdr'

REMOVE_DATA = '''
              [{"value": [{"id": "%s", "type": "File"}],
                "path": "/deleted",
                "op": "add",
              }]
              '''


