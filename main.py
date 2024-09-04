from flask import Flask
from routes.router import router
import logging

def main() -> Flask:

    app = Flask(__name__)
    app.register_blueprint(router)
    return app


app = main()

if __name__ == '__main__':
    logging.getLogger('generalLogger')
    app.run(
        host='0.0.0.0',
        port=5000
    )