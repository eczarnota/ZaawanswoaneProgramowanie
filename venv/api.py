from opening import opens
from flask import Flask
from flask_restful import Resource, Api
from movie import Movie
from links import Links
from tags import Tags
from ratings import Ratings

app = Flask(__name__)
api = Api(app)

class movies(Resource):
    def get(self):
        return opens('movies.csv', Movie)

class links(Resource):
    def get(self):
        return opens('links.csv', Links)

class tags(Resource):
    def get(self):
        return opens('tags.csv', Tags)

class ratings(Resource):
    def get(self):
        return opens('ratings.csv', Ratings)

api.add_resource(movies, '/movies/')
api.add_resource(links, '/links/')
api.add_resource(tags, '/tags/')
api.add_resource(ratings, '/ratings/')

if __name__ == '__main__':
    app.run(debug=True)