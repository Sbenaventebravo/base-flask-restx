from flask import Flask
from blueprints.entity.api import api_entity

app = Flask(__name__)
app.register_blueprint(api_entity)

if __name__ == "__main__":
    app.run(debug=True)