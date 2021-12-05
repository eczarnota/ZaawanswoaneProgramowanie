from opening import opens
from flask import Flask
from flask_restful import Resource, Api
from movie import Movie
from links import Links

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return opens('movies.csv', Movie)

api.add_resource(HelloWorld, '/movies/')

api.add_resource(HelloWorld, '/links/')

if __name__ == '__main__':
    app.run(debug=True)