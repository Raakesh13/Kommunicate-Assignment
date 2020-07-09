from flask import Flask, jsonify
from flask_restful import Api
from resources.MoviesToWorkOn import MoviesToWorkOn

app = Flask(__name__)
api = Api(app)

api.add_resource(MoviesToWorkOn, '/moviestoworkon')

if __name__ == '__main__':
    app.run(debug=True)