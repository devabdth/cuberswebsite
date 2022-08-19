from app import app
from config import Config

if __name__ == '__main__':
    config: Config = Config()
    app.run(debug=True, port=config.port)
