
# pylint: disable=invalid-name

from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'fabien'}


if __name__ == "__main__":
    app.run()
