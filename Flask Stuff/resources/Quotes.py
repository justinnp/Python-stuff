from flask_restful import Resource
from resources.scraper import getQuotes

class Quotes(Resource):
    def get(self):
        return getQuotes(), 200