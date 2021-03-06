from flask import jsonify, request, make_response
from flask_restful import Resource
from .utils import maximizeProfit

class Movies(Resource):

    #Post request to get the movie list from an actor and return the maximum profit and list of movies the actor should work on
    def post(self): 
        body = request.get_json(force=True)        
        movies = body['moviesList']
        res = maximizeProfit(movies)
        if 'error' in res:
            return make_response(jsonify(res), 422)
        return make_response(jsonify(res), 200)
