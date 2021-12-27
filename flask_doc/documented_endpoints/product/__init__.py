from os import name
from flask import request, json
from flask_restx import Namespace, Resource, fields, reqparse
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

def responses(fetchdata):
    results = []
    keys = ['id', 'name', 'type', 'price', 'description',
            'size', 'image', 'video', 'color', 'quantity']
    for j in fetchdata:
        result = {}
        for x, i in enumerate(j):
            result[keys[x]] = i
        results.append(result)
    return results

@namespace.route('/show')
class ShowProduct(Resource):

    # @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(404, 'Not Found')
    @namespace.response(200, 'Success', product_model)
    def get(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM products")
        fetchdata = cur.fetchall()
        cur.close()
        if(len(fetchdata) == 0):
            return namespace.abort(404, 'Not Found')
            # return 404
        
        return responses(fetchdata)

parser_id = reqparse.RequestParser()
parser_id.add_argument('id', type=int, help='Product\'s id (eg: 5)')
@namespace.route('/id')
class SearchByID(Resource):
    @namespace.response(500, 'Internal Server error')
    @namespace.response(404, 'Not Found')
    @namespace.response(400, 'Invalid value')
    @namespace.response(200, 'Success', product_model)

    @namespace.expect(parser_id)
    def get(self):
        con = sqlite3.connect('database.db')

        cur = con.cursor()
        id = request.args.get('id') #name = ao
        if(name is None):
            return namespace.abort(400, 'Invalid value')
        cur.execute("SELECT * FROM products WHERE id = {}".format(id))
        fetchdata = cur.fetchall()
        cur.close()
        response = responses(fetchdata)
        if(len(fetchdata) == 0):
            return namespace.abort(404, 'Not Found')
            # return 404
        
        return response


parser_name = reqparse.RequestParser()
parser_name.add_argument('name', type=str, help='Product\'s name (eg: quan)')
@namespace.route('/name')
class SearchByName(Resource):
    # @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(404, 'Not Found')
    @namespace.response(400, 'Invalid value')
    @namespace.response(200, 'Success', product_model)

    @namespace.expect(parser_name)
    def get(self):
        con = sqlite3.connect('database.db')

        cur = con.cursor()
        name = request.args.get('name') #name = ao
        if(name is None):
            return namespace.abort(400, 'Invalid value')
            # return 400
        cur.execute("SELECT * FROM products WHERE name LIKE \"%{}%\"".format(name))
        fetchdata = cur.fetchall()
        cur.close()
        response = responses(fetchdata)
        if(len(fetchdata) == 0):
            return namespace.abort(404, 'Not Found')
            # return 404
        
        return response

def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


parser_price = reqparse.RequestParser()
parser_price.add_argument('from', type=float, help='Price product\'s from (eg: 100)')
parser_price.add_argument('to', type=float, help='Price product\'s to (eg: 200)')

@namespace.route('/price')
class SearchByPrice(Resource):

    @namespace.response(500, 'Internal Server error')
    @namespace.response(404, 'Not Found')
    @namespace.response(400, 'Invalid value - From and to must be numberic - From must be less than to')
    # @namespace.response(250,'from and to must be numberic')
    # @namespace.response(251,'from must be less than to')
    @namespace.response(200, 'Success', product_model)
    @namespace.expect(parser_price)
    def get(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        froms = request.args.get('from') 
        tos = request.args.get('to') 
        if(froms is None or tos is None):
            return namespace.abort(400, 'Invalid value')
            response = 400
            # return response
        if(not is_float(tos) or not is_float(froms)):
            # response = 250
            return namespace.abort(250, 'from and to must be numberic')
            
        tos = float(tos)
        froms = float(froms)
        if(tos < froms):
            # response = 251
            return namespace.abort(251, 'From must be less than to')
        cur.execute("SELECT * FROM products WHERE {} > price AND price > {}".format(tos, froms))
        fetchdata = cur.fetchall()
        cur.close()
        response = responses(fetchdata)
        if(fetchdata == ()):
            return namespace.abort(404, 'Not Found')
            # response = 404
        return response


parser_filter = reqparse.RequestParser()
parser_filter.add_argument('type', type=str, help='Product\'s type (eg: mem muot)')
parser_filter.add_argument('size', type=str, help='Product\'s size (eg: A)')
parser_filter.add_argument('color', type=str, help='Product\'s color (eg: vang)')
@namespace.route('/filters')
class SearchByFilters(Resource):

    # @namespace.doc(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(404, 'Not Found')
    @namespace.response(200, 'Success', product_model)
    @namespace.expect(parser_filter)
    def get(self):
        con = sqlite3.connect('database.db')

        cur = con.cursor()
        type = request.args.get('type')
        size = request.args.get('size')
        color = request.args.get('color')
        
        if((not type is None) and (not size is None) and (not color is None)):
            cur.execute("SELECT * FROM products WHERE type LIKE \"%{}%\" AND size = \"{}\" AND color LIKE \"%{}%\"".format(type, size, color))

        elif((not size is None) and (not type is None)):
            cur.execute("SELECT * FROM products WHERE type LIKE \"%{}%\" AND size = \"{}\" ".format(type, size))

        elif((not type is None) and (not color is None)):
            cur.execute("SELECT * FROM products WHERE type LIKE \"%{}%\" AND color LIKE \"%{}%\" ".format(type, color))
        
        elif((not size is None) and (not color is None)):
            cur.execute("SELECT * FROM products WHERE size = \"{}\" AND color LIKE \"%{}%\" ".format(size, color))

        elif(not type is None):
            cur.execute("SELECT * FROM products WHERE type LIKE \"%{}%\"".format(type))

        elif(not size is None):
            cur.execute("SELECT * FROM products WHERE size = \"{}\"".format(size))

        elif(not color is None):
            cur.execute("SELECT * FROM products WHERE color LIKE \"%{}%\"".format(color))

        
        fetchdata = cur.fetchall()
        cur.close()
        response = responses(fetchdata)

        if(len(fetchdata) == 0):
            return namespace.abort(404, 'Not Found')
            # response = 404
        return response


parser_add = reqparse.RequestParser()
parser_add.add_argument('id', type=int, help='Product\'s id (eg: 123)', location='form')
parser_add.add_argument('name', type=str, help='Product\'s name (eg: quan dai)', location='form')
parser_add.add_argument('type', type=str, help='Product\'s type (eg: quan)', location='form')
parser_add.add_argument('price', type=float, help='Product\'s price (eg: 50000)', location='form')
parser_add.add_argument('description', type=str, help='Product\'s description (eg: vai den tron bong)', location='form')
parser_add.add_argument('size', type=str, help='Product\'s size (eg: M)', location='form')
parser_add.add_argument('image', type=str, help='Product\'s image (eg: fgfg)', location='form')
parser_add.add_argument('video', type=str, help='Product\'s video (eg: dfg)', location='form')
parser_add.add_argument('color', type=str, help='Product\'s color (eg: den)', location='form')
parser_add.add_argument('quantity', type=int, help='Product\'s quantity (eg: 5)', location='form')
@namespace.route('/add_product', methods=['PUT'])
class AddProduct(Resource):

    # @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(200, 'Successfully Added')
    @namespace.response(400, 'ID already exist - ID not null')
    @namespace.expect(parser_add, validate=True)
    def put(self):
        con = sqlite3.connect('database.db')
        # id = request.form['id']

        try:
            id = request.form['id']
        except:
            return namespace.abort(400, 'ID not null')
            # return 401

        name = request.form.get('name', default=None)
        type = request.form.get('type', default=None)
        price = request.form.get('price', default=None)
        description = request.form.get('description', default=None)
        size = request.form.get('size', default=None)
        image = request.form.get('image', default=None)
        video = request.form.get('video', default=None)
        color = request.form.get('color', default=None)
        quantity = request.form.get('quantity', default=None)
        
        cur = con.cursor()

        cur.execute("SELECT id FROM products WHERE id = {};".format(id))
        fetchdata = cur.fetchall()
        
        if(len(fetchdata) > 0):
            cur.close()
            return namespace.abort(400, 'ID already exist')
        
        cur.execute("INSERT INTO products (ID, name, type, price, description, size, image, video, color, quantity) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", {});".format
                    (id, name, type, price, description, size, image, video, color, quantity))
        con.commit()
        cur.close()
        # response = 200
        return 'Successfully Added'
        # return response

parser_delete = reqparse.RequestParser()
parser_delete.add_argument('id', type=int, help='Product\'s id (eg: 123)', location='form')

@namespace.route('/delete_product', methods=['DELETE'])
class DeleteProduct(Resource):

    # @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(200, 'Successfully delete')
    @namespace.response(400, 'ID not found')
    @namespace.expect(parser_delete, validate=True)
    def delete(self):
        con = sqlite3.connect('database.db')

        id = request.form['id']

        cur = con.cursor()
        cur.execute("SELECT id FROM products WHERE id = {};".format(id))
        fetchdata = cur.fetchall()
        
        if(len(fetchdata) == 0):
            cur.close()
            return namespace.abort(400, 'ID not found')

        cur.execute("DELETE FROM products WHERE id={};".format(id))
        con.commit()

        cur.close()
        # response = 202
        return 'Successfully delete'
        # return response

@namespace.route('/edit_product', methods=['POST'])
class EditProduct(Resource):

    # @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(400, 'Error - ID Not Found')
    # @namespace.response(401, 'Error')
    # @namespace.response(402, 'ID Not Found')
    @namespace.response(200, 'Successfully edit')
    @namespace.expect(parser_add, validate=True)

    def post(self):
        con = sqlite3.connect('database.db')
        try:
            id = request.form['id']
        except:
            return namespace.abort(400, 'Error')
            # return 401
        
        name = request.form.get('name', default=None)
        type = request.form.get('type', default=None)
        price = request.form.get('price', default=None)
        description = request.form.get('description', default=None)
        size = request.form.get('size', default=None)
        image = request.form.get('image', default=None)
        video = request.form.get('video', default=None)
        color = request.form.get('color', default=None)
        quantity = request.form.get('quantity', default=None)

        cur = con.cursor()
        cur.execute("SELECT id FROM products WHERE id = {};".format(id))
        fetchdata = cur.fetchall()
        
        if(len(fetchdata) == 0):
            # response = 402
            cur.close()
            return namespace.abort(400, 'ID Not Found')
            # return response

        cols = ['name', 'type', 'price', 'description', 'size', 'image', 'video', 'color', 'quantity']
        inputs = [name, type, price, description, size, image, video, color, quantity]
        for i, col in enumerate(cols):
            if(not inputs[i] is None):
                cur.execute("UPDATE products SET {} = \"{}\" WHERE id = {};".format(col, inputs[i], id))
        
        con.commit()
        cur.close()
        # response = 200

        # return response
        return 'Successfully edit'


