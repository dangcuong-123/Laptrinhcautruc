from flask import Blueprint
from flask_restx import Api
from flask_doc.documented_endpoints.product import namespace as product
from flask_doc.documented_endpoints.category import namespace as category

blueprint = Blueprint('documented_api', __name__)

api_extension = Api(
    blueprint,
    title='SP17 - Product module',
    version='2.0',
    description='This is API for Product module'
)

api_extension.add_namespace(product)
api_extension.add_namespace(category)