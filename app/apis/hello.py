from flask_restx import Namespace, Resource

api = Namespace('hello', description='hello world')


@api.route('')
class Hello(Resource):
    def get(self):
        return {'hello': 'fabien'}
