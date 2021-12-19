# main.py
from flask import Flask
from flask_doc.documented_endpoints import blueprint as documented_endpoints
from flask_doc.basic_endpoints import blueprint as basic_endpoints
from logging import debug

app = Flask(__name__)
app.config['RESTPLUS_MASK_SWAGGER'] = False

app.register_blueprint(documented_endpoints)
app.register_blueprint(basic_endpoints)

if __name__ == "__main__":
    app.run(debug=True)