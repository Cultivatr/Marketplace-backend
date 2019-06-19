import os
from flask import Flask, request, jsonify
from flask_cors import CORS


app=Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Heroku Postgresql
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# Local PostgreSQL
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/cultivatr'

CORS(app, supports_credentials=True)

with app.app_context():
    from files.global_vars import global_variables
    global_vars = global_variables()
    import files.db_models
    import files.routes

@app.route('/', methods=['GET'])
def hello_world():
    return '<a href="https://cultivatr.ca/">Cultivatr</a>'

if __name__ == '__main__':
    app.debug = True
    app.run()
