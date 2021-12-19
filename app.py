from logging import debug, error
from flask import Flask, render_template, jsonify, request, json
# from flask_mysqldb import MySQL
import sqlite3


app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '123456'
# app.config['MYSQL_DB'] = 'laptrinhcautruc'

# mysql = MySQL(app)

@app.route('/')
def home():
    con = sqlite3.connect('database.db')
    return render_template('index.html')

@app.route('/show')
def show_product():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM products")
    fetchdata = cur.fetchall()
    cur.close()
    if(fetchdata == []):
        return "1"
    response = app.response_class(response=json.dumps(fetchdata),
                                  status=200,
                                  mimetype='application/json')
    return response

@app.route('/name')
def search_by_name():
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
    response = app.response_class(response=json.dumps(fetchdata),
                                  status=200,
                                  mimetype='application/json')
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

@app.route('/price')
def search_by_price():
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
    response = app.response_class(response=json.dumps(fetchdata),
                                  status=200,
                                  mimetype='application/json')
    if(fetchdata == ()):
        response = app.response_class(response=json.dumps("not found"),
                                  status=200,
                                  mimetype='error')
    return response

@app.route('/filters')
def search_by_filters():
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
    response = app.response_class(response=json.dumps(fetchdata),
                                  status=200,
                                  mimetype='application/json')

    if(fetchdata == ()):
        response = app.response_class(response=json.dumps("not found"),
                                  status=200,
                                  mimetype='error')
    return response

@app.route('/add_product', methods=['POST'])
def add_product():
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
    
    cur.close()
    response = app.response_class(response=json.dumps("successfully added"),
                                  status=200,
                                  mimetype='notification')

    return response

@app.route('/delete_product', methods=['POST'])
def delete_product():
    con = sqlite3.connect('database.db')

    id = request.form['id']

    cur = con.cursor()

    cur.execute("DELETE FROM products WHERE id={};".format(id))
    cur.close()
    response = app.response_class(response=json.dumps("successfully delete"),
                                  status=200,
                                  mimetype='notification')

    return response

@app.route('/edit_product', methods=['POST'])
def edit_product():
    con = sqlite3.connect('database.db')

    id = request.form['id']
    if(id is None):
        response = app.response_class(response=json.dumps("id not NULL"),
                                  status=200,
                                  mimetype='error')
    
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
    cur.close()
    response = app.response_class(response=json.dumps("successfully edit"),
                                  status=200,
                                  mimetype='notification')

    return response

if __name__ == "__main__":
    app.run(debug=True)

