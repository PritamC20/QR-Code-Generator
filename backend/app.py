from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Swagger setup
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "QR Code Generator API"})
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

import routes

@app.route('/ar')
def ar_experience():
    return render_template('ar.html')

if __name__ == '__main__':
    app.run(debug=True)
