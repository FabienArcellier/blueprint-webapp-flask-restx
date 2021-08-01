from flask_restx import Namespace, Resource, fields, marshal

from app.infrastructure.memory_hello_repository import MemoryHelloRepository

api = Namespace('hello', description='hello world')

"""
The exposition model we are using.
"""
model = api.model('Hello', {
    'hello': fields.String(required=True, description='The username to say hello')
})
repository = MemoryHelloRepository()


@api.route('')
class Hello(Resource):
    def get(self):
        _hello = repository.get()
        return marshal(_hello, model)

    @api.expect(model)
    def put(self):
        _hello = api.payload
        repository.save(_hello)
        return marshal(_hello, model), 201
