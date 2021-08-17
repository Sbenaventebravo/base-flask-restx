from flask import Flask, Blueprint
from flask_restx import Api
from blueprints.entity.namespace import api as entity_ns

api_entity = Blueprint("api_entity", __name__, url_prefix="/v1")

api = Api(api_entity, version="1.0", title="Entity API", description="A simple Entity API")

api.add_namespace(entity_ns)


