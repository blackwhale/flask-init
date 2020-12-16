from flask import Blueprint, request
from flask_restplus import Api, Resource, fields
from utils.logger import get_logger


logger = get_logger()

hello_bp = Blueprint('hello', __name__)
api = Api(hello_bp)
ns = api.namespace(
    'hello',
    description='hello namespace',
    validate=True
)

hello_model = ns.model(
    'hello model',
    {
        'msg': fields.String(
            description='return message',
            required=False,
            validate=True
        ),
    }
)


@ns.route('/', methods=['GET'])
class Index(Resource):
    @ns.expect(hello_model)
    def get(self):
        msg = request.json.get('msg', 'Hello world')
        return {'msg': msg}
