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

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(404, 'Not Found')


    def get(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM products")
        fetchdata = cur.fetchall()
        cur.close()
        if(len(fetchdata) == 0):
            return 404
        
        return responses(fetchdata)

parser_name = reqparse.RequestParser()
parser_name.add_argument('name', type=str, help='Product\'s name (eg: quan)')
@namespace.route('/name')
class SearchByName(Resource):
    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(404, 'Not Found')
    @namespace.response(400, 'Invalid value')

    @namespace.expect(parser_name)
    def get(self):
        con = sqlite3.connect('database.db')

        cur = con.cursor()
        name = request.args.get('name') #name = ao
        if(name is None):
            # response = app.response_class(response=json.dumps("Invalid value"),
            #                         status=200,
            #                         mimetype='error')
            return 400
        cur.execute("SELECT * FROM products WHERE name LIKE \"%{}%\"".format(name))
        fetchdata = cur.fetchall()
        cur.close()
        response = responses(fetchdata)
        if(len(fetchdata) == 0):
            return 404
            # response = app.response_class(response=json.dumps("not found"),
            #                         status=200,
            #                         mimetype='error')
        
        return response

def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


@namespace.route('/price')
class SearchByPrice(Resource):

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(404, 'Not Found')
    @namespace.response(400, 'Invalid value')
    @namespace.response(250,'from and to must be numberic')
    @namespace.response(251,'from must be less than to')

    def get(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        froms = request.args.get('from') 
        tos = request.args.get('to') 
        if(froms is None or tos is None):
            # response = app.response_class(response=json.dumps("Invalid value"),
            #                         status=200,
            #                         mimetype='error')
            response = 400
            # return response
        if(not is_float(tos) or not is_float(froms)):
            # response = app.response_class(response=json.dumps("from and to must be numberic"),
            #                         status=200,
            #                         mimetype='error')
            response = 250
            return response
            
        tos = float(tos)
        froms = float(froms)
        if(tos < froms):
        #     response = app.response_class(response=json.dumps("from must be less than to"),
        #                             status=200,
        #                             mimetype='error')
            response = 251
            return response
        cur.execute("SELECT * FROM products WHERE {} > price AND price > {}".format(tos, froms))
        fetchdata = cur.fetchall()
        cur.close()
        response = responses(fetchdata)
        if(fetchdata == ()):
            response = 404
        #     response = app.response_class(response=json.dumps("not found"),
        #                             status=200,
        #                             mimetype='error')
        return response

@namespace.route('/filters')
class SearchByFilters(Resource):

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(404, 'Not Found')

    def get(self):
        con = sqlite3.connect('database.db')

        cur = con.cursor()
        type = request.args.get('type')
        size = request.args.get('size')
        color = request.args.get('color')
        
        if((not type is None) and (not size is None) and (not color is None)):
            cur.execute("SELECT * FROM products WHERE type LIKE \"%{}%\" AND size LIKE \"%{}%\" AND color LIKE \"%{}%\"".format(type, size, color))

        elif((not size is None) and (not type is None)):
            cur.execute("SELECT * FROM products WHERE type LIKE \"%{}%\" AND size LIKE \"%{}%\" ".format(type, size))

        elif((not type is None) and (not color is None)):
            cur.execute("SELECT * FROM products WHERE type LIKE \"%{}%\" AND color LIKE \"%{}%\" ".format(type, color))
        
        elif((not size is None) and (not color is None)):
            cur.execute("SELECT * FROM products WHERE size LIKE \"%{}%\" AND color LIKE \"%{}%\" ".format(size, color))

        elif(not type is None):
            cur.execute("SELECT * FROM products WHERE type LIKE \"%{}%\"".format(type))

        elif(not size is None):
            cur.execute("SELECT * FROM products WHERE size LIKE \"%{}%\"".format(size))

        elif(not color is None):
            cur.execute("SELECT * FROM products WHERE color LIKE \"%{}%\"".format(color))

        
        fetchdata = cur.fetchall()
        cur.close()
        response = responses(fetchdata)

        if(len(fetchdata) == 0):
            response = 404
        #     response = app.response_class(response=json.dumps("not found"),
        #                             status=200,
        #                             mimetype='error')
        return response


parser_add = reqparse.RequestParser()
parser_add.add_argument('id', type=int, help='Product\'s id (eg: 123)', location='form')
parser_add.add_argument('name', type=str, help='Product\'s name (eg: quan)', location='form')
parser_add.add_argument('type', type=str, help='Product\'s type (eg: quan)', location='form')
parser_add.add_argument('price', type=float, help='Product\'s price (eg: quan)', location='form')
parser_add.add_argument('description', type=str, help='Product\'s description (eg: quan)', location='form')
parser_add.add_argument('size', type=str, help='Product\'s size (eg: quan)', location='form')
parser_add.add_argument('image', type=str, help='Product\'s image (eg: quan)', location='form')
parser_add.add_argument('video', type=str, help='Product\'s video (eg: quan)', location='form')
parser_add.add_argument('color', type=str, help='Product\'s color (eg: quan)', location='form')
parser_add.add_argument('quantity', type=int, help='Product\'s quantity (eg: quan)', location='form')

@namespace.route('/add_product', methods=['PUT'])
class AddProduct(Resource):

    # @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(200, 'Successfully Added')
    @namespace.expect(parser_add, validate=True)
    def put(self):
        con = sqlite3.connect('database.db')
        id = request.form['id']
        name = request.form['name']
        type = request.form['type']
        price = request.form['price']
        description = request.form['description']
        size = request.form['size']
        image = request.form['image']
        video = request.form['video']
        color = request.form['color']
        quantity = request.form['quantity']
        
        cur = con.cursor()
        cur.execute("INSERT INTO products (ID, name, type, price, description, size, image, video, color, quantity) VALUES ({}, \"{}\", \"{}\", {}, \"{}\", \"{}\", \"{}\", \"{}\", \"{}\", {});".format
                    (id, name, type, price, description, size, image, video, color, quantity))
        con.commit()

        cur.close()
        # response = app.response_class(response=json.dumps("successfully added"),
        #                             status=200,
        #                             mimetype='notification')

        response = 200
        return response

parser_delete = reqparse.RequestParser()
parser_delete.add_argument('id', type=int, help='Product\'s id (eg: 123)', location='form')

@namespace.route('/delete_product', methods=['DELETE'])
class DeleteProduct(Resource):

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(202, 'successfully delete')
    @namespace.expect(parser_delete, validate=True)
    def delete(self):
        con = sqlite3.connect('database.db')

        id = request.form['id']

        cur = con.cursor()

        cur.execute("DELETE FROM products WHERE id={};".format(id))
        con.commit()

        cur.close()
        # response = app.response_class(response=json.dumps("successfully delete"),
        #                             status=200,
        #                             mimetype='notification')
        response = 202
        return response


@namespace.route('/edit_product', methods=['POST'])
class EditProduct(Resource):

    # @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.response(401, 'Error')
    @namespace.response(402, 'ID Not Found')
    @namespace.response(200, 'successfully edit')
    @namespace.expect(parser_add, validate=True)

    def post(self):
        con = sqlite3.connect('database.db')
        try:
            id = request.form['id']
        except:
            return 401
        # if(id is None):
        #     # response = app.response_class(response=json.dumps("id not NULL"),
        #     #                         status=200,
        #     #                         mimetype='error')
        #     return 
        
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
            # response = app.response_class(response=json.dumps("ID not found"),
            #                         status=200,
            #                         mimetype='error')
            response = 402
            cur.close()
            return response

        cur.execute("UPDATE products SET name = \"{}\", type = \"{}\", price = {}, description = \"{}\", size = \"{}\", image = \"{}\", video = \"{}\", color = \"{}\", quantity = {} WHERE id = {};".format
                    (name, type, price, description, size, image, video, color, quantity, id))
        
        con.commit()
        cur.close()
        response = 200

        return response
