# blueprints/basic_endpoints/__ini__.py
from flask import Blueprint, request

blueprint = Blueprint('api', __name__, url_prefix='/basic_api')

@blueprint.route('/product/show')
def hello_world():
    return {'message': 'Hello World!'}