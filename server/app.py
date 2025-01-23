from flask import Flask, make_response, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_migrate import Migrate

from models import db, Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Movies(Resource):

    def get(self):
        movies_dict = [movie.to_dict() for movie in Movie.query.all()]
        response = make_response(movies_dict, 200)
        return response
    
api.add_resource(Movies, '/movies')

if __name__ == '__main__':
    app.run(port=5555, debug=True)