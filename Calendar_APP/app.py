from flask import Blueprint
from flask_restful import Api
from resources.controller import GetEvents

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(GetEvents, '/GetEvents')