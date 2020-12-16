import boto3

from flask import Blueprint, request
from flask_restplus import Api, Resource, fields

hc_bp = Blueprint('health', __name__)
api = Api(hc_bp)
ns = api.namespace('healthcheck', description='Health Check')

hc_model = ns.model("health check", {
})


@ns.route('/', methods=['GET', 'POST'])
class Index(Resource):
    @ns.expect(hc_model)
    def get(self):
        return {'status': 'on'}

    @ns.expect(hc_model)
    def post(self):
        return {'status': 'on'}
