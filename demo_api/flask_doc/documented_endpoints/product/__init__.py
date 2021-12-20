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
    def get(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM products")
        fetchdata = cur.fetchall()
        cur.close()
        if(fetchdata == []):
            return "1"
        
        return responses(fetchdata)

@namespace.route('/name')
class ShowProduct(Resource):

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        con = sqlite3.connect('database.db')

        cur = con.cursor()
        name = request.args.get('name') #name = ao
        if(name is None):
            response = app.response_class(response=json.dumps("Invalid value"),
                                    status=200,
                                    mimetype='error')
            
            return response
        cur.execute("SELECT * FROM products WHERE name LIKE \"%{}%\"".format(name))
        fetchdata = cur.fetchall()
        cur.close()
        response = responses(fetchdata)
        if(fetchdata == ()):
            response = app.response_class(response=json.dumps("not found"),
                                    status=200,
                                    mimetype='error')
        
        return response

def is_float(element) -> bool:
    try:
        float(element)
        return True
    except ValueError:
        return False


@namespace.route('/price')
class ShowProduct(Resource):

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        froms = request.args.get('from') 
        tos = request.args.get('to') 
        if(froms is None or tos is None):
            response = app.response_class(response=json.dumps("Invalid value"),
                                    status=200,
                                    mimetype='error')
            
            return response
        if(not is_float(tos) or not is_float(froms)):
            response = app.response_class(response=json.dumps("from and to must be numberic"),
                                    status=200,
                                    mimetype='error')
            return response
            
        tos = float(tos)
        froms = float(froms)
        if(tos < froms):
            response = app.response_class(response=json.dumps("from must be less than to"),
                                    status=200,
                                    mimetype='error')
            return response
        cur.execute("SELECT * FROM products WHERE {} > price AND price > {}".format(tos, froms))
        fetchdata = cur.fetchall()
        cur.close()
        response = responses(fetchdata)
        if(fetchdata == ()):
            response = app.response_class(response=json.dumps("not found"),
                                    status=200,
                                    mimetype='error')
        return response

@namespace.route('/filters')
class ShowProduct(Resource):

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
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

        if(fetchdata == ()):
            response = app.response_class(response=json.dumps("not found"),
                                    status=200,
                                    mimetype='error')
        return response


@namespace.route('/add_product', methods=['PUT'])
class ShowProduct(Resource):

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
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
        response = app.response_class(response=json.dumps("successfully added"),
                                    status=200,
                                    mimetype='notification')

        return response

@namespace.route('/delete_product', methods=['DELETE'])
class DeleteProduct(Resource):

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    def delete(self):
        con = sqlite3.connect('database.db')

        id = request.form['id']

        cur = con.cursor()

        cur.execute("DELETE FROM products WHERE id={};".format(id))
        con.commit()

        cur.close()
        response = app.response_class(response=json.dumps("successfully delete"),
                                    status=200,
                                    mimetype='notification')
        return response



@namespace.route('/edit_product', methods=['POST'])
class EditProduct(Resource):

    @namespace.marshal_list_with(product_model)
    @namespace.response(500, 'Internal Server error')
    def post(self):
        con = sqlite3.connect('database.db')

        id = request.form['id']
        if(id is None):
            # response = app.response_class(response=json.dumps("id not NULL"),
            #                         status=200,
            #                         mimetype='error')
            return 
        
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
        
        if(fetchdata == ()):
            response = app.response_class(response=json.dumps("ID not found"),
                                    status=200,
                                    mimetype='error')
            cur.close()
            return response

        cur.execute("UPDATE products SET name = \"{}\", type = \"{}\", price = {}, description = \"{}\", size = \"{}\", image = \"{}\", video = \"{}\", color = \"{}\", quantity = {} WHERE id = {};".format
                    (name, type, price, description, size, image, video, color, quantity, id))
        
        con.commit()
        cur.close()
        response = app.response_class(response=json.dumps("successfully edit"),
                                    status=200,
                                    mimetype='notification')

        return response


