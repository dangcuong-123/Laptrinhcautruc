from flask import Blueprint
from flask_restx import Api
from flask_doc.documented_endpoints.product import namespace as hello_world_ns

blueprint = Blueprint('documented_api', __name__)

api_extension = Api(
    blueprint,
    title='Flask RESTplus Demo',
    version='1.0',
    description='Application tutorial to demonstrate Flask RESTplus extension\
        for better project structure and auto generated documentation'
)

api_extension.add_namespace(hello_world_ns)