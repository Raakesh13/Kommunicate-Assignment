from flask import Flask, jsonify
from flask_restful import Api
from resources.Movies import Movies

app = Flask(__name__)
api = Api(app)

api.add_resource(Movies, '/movies')

if __name__ == '__main__':
    app.run(debug=True)