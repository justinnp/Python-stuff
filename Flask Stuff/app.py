from flask import Flask, request
from flask_restful import Resource, Api
from resources.Quotes import Quotes

app = Flask(__name__)
api = Api(app)
api.add_resource(Quotes, '/')

if __name__ == '__main__':
    app.run(debug=True)
