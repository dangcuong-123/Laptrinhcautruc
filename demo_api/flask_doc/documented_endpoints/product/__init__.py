from flask import request, json
from flask_restx import Namespace, Resource, fields
import sqlite3
namespace = Namespace('product', 'Product related endpoints')

product_model = namespace.model('product', {
    'id': fields.Integer(
        readonly=True,
        description='This is id of products'
    ),
    'name': fields.String(
        readonly=True,
        description='Product\'s name'
    ),
    'type': fields.String(
        readonly=True,
        description='Product\'s type'
    ),
    'price': fields.Float(
        readonly=True,
        description='Product\'s price'
    ),
    'description': fields.String(
        readonly=True,
        description='Product\'s description'
    ),
    'size': fields.String(
        readonly=True,
        description='Product\'s size'
    ),
    'image': fields.String(
        readonly=True,
        description='Product\'s image'
    ),
    'video': fields.String(
        readonly=True,
        description='Product\'s video'
    ),
    'color': fields.String(
        readonly=True,
        description='Product\'s color'
    ),
    'quantity': fields.Integer(
        readonly=True,
        description='Product\'s quantity'
    )
}, strict=True)

# product_model_x = namespace.model('product', {
#     'id': fields.Integer(
#         readonly=True,
#         description='This is id of products'
#     ),
#     'name': fields.String(
#         readonly=True,
#         description='Product\'s name'
#     )
# })


# hello_world_example = {'id': 123, 'name':'quan ao'}

@namespace.route('/show')
class ShowProduct(Resource):

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM products")
        fetchdata = cur.fetchall()
        cur.close()
        if(fetchdata == []):
            return "1"
        results = []
        keys = ['id', 'name', 'type', 'price', 'description',
                'size', 'image', 'video', 'color', 'quantity']
        for j in fetchdata:
            result = {}
            for x, i in enumerate(j):
                result[keys[x]] = i
            results.append(result)
            
        return results