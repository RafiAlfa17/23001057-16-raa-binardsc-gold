import re

from flask import Flask, jsonify
from flask import request
import flasgger
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

class CustomFlaskAppWithEncoder(Flask):
    json_provider_class = LazyJSONEncoder

app = CustomFlaskAppWithEncoder(__name__)


swagger_template = dict(
info = {
    'title': LazyString(lambda: 'API Documentation for Data Processing and Modeling'),
    'version': LazyString(lambda: '1.0.0'),
    'description': LazyString(lambda: 'Dokumentasi API untuk Data Processing and Modeling'),
    },
    host= LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'docs',
            "route": '/docs.json',
        }
    ],
    'static_url_path': "/flasgger_static",
    'swagger_ui': True,
    'specs_route': "/docs/"
}
swagger = Swagger(app, template=swagger_template,
                  config=swagger_config)

@swag_from("docs/hello_world.yml", methods=['GET'])
@app.route('/', methods=['GET'])
def hello_world():
    json_response = {
        'status_code': 200,
        'description': "Menyapa Hello World",
        'data': "Hello World",
    }

    response_data = jsonify(json_response)
    return response_data

@app.route('/text', methods=['GET'])
def hello_worldk():
    json_response = {
        'status_code': 200,
        'description': "KMenyapa Hello World",
        'data': "THello World",
    }

    response_data = jsonify(json_response)
    return response_data

if __name__ == '__main__':
    app.run()
