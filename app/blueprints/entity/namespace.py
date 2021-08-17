from flask import request
from flask_restx import Namespace, Resource, fields

from uuid import uuid4

api = Namespace('entity', description='entity related operations')

entity = api.model('entity', {
    'id': fields.String(readonly=True, description='The entity identifier'),
    'name': fields.String(required=True, description='The entity name'),
})

ENTITIES = {}

@api.route('/<string:id>')
@api.param('id', 'The entity identifier')
@api.response(404, 'Entity not found')
class Entity(Resource):
    @api.doc('get_entity')
    @api.marshal_with(entity)
    def get(self, id):
        '''Fetch a entity given its identifier'''
        if ENTITIES.get(id):
            return {"id": id, **ENTITIES[id]}, 200
        api.abort(404)

    @api.doc('put_entity')
    @api.marshal_with(entity)
    def put(self, id):
        '''PUT a entity given its identifier'''
        if ENTITIES.get(id):
            if not request.is_json:
                return "Invalid Body", 400
            
            data = request.get_json()
            name = data.get("name", None)
            ENTITIES[id]["name"] = name

            return {"id": id, **ENTITIES[id]}, 200
        
        api.abort(404)

    @api.doc('delete_entity')
    def delete(self, id):
        '''Delete a entity given its identifier'''
        if ENTITIES.get(id):
            if ENTITIES.get(id):
                del ENTITIES[id] 
            return '', 204
        
        api.abort(404)
        

@api.route('')
class Entity(Resource):
    @api.doc('post_entity')
    @api.marshal_with(entity)
    def post(self):
        '''Post a new entity'''
        if not request.is_json:
            return "Invalid Body", 400
        
        data = request.get_json()
        
        id = str(uuid4())
        name = data.get("name", None)

        ENTITIES[id] = {"name": name}
        
        return {"id": id, **ENTITIES[id]}, 200

    def get(self):
        '''List of entities'''
        entities  = [{"id": key, **value}  for key, value in ENTITIES.items()]
        data = {
            "items": entities,
            "count": len(entities)
        }
        return data