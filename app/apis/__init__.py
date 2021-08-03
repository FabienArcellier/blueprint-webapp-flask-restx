from flask_restx import Api

from app.apis.hello import api as hello

api = Api(
    title='api',
    version='1.0',
    description='',
    prefix='/api',
    doc='/api'
)

api.add_namespace(hello)
