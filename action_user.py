from logging import debug, error
from flask import Flask, render_template, jsonify, request, json
import flask
from flask.wrappers import Request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123456'
app.config['MYSQL_DB'] = 'laptrinhcautruc'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/show')
def show_product():
    cur = mysql.connection.cursor()
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
    cur = mysql.connection.cursor()
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
    cur = mysql.connection.cursor()
    froms = request.args.get('from') 
    tos = request.args.get('to') 
    if(froms is None or tos is None):
        response = app.response_class(response=json.dumps("Invalid value"),
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

    if(not is_float(tos) or not is_float(froms)):
        response = app.response_class(response=json.dumps("from and to must be numberic"),
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
    cur = mysql.connection.cursor()
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



if __name__ == "__main__":
    app.run(debug=True)

