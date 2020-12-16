from flask import Flask, request
from flask_restplus import Api

from core.api.v1.hello import ns as hello_ns
from core.api.healthcheck import ns as hc_ns


app = Flask(__name__)
app.url_map.strict_slashes = False

api_instance = Api(app,
                   version='1.0',
                   title='My test app',
                   description='My test app')

api_instance.add_namespace(hello_ns, path='/api/v1/hello')
api_instance.add_namespace(hc_ns, path='/healthcheck')
