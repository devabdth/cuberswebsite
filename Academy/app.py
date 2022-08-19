from flask import Flask
from config import Config

# Routers
from routers import setup

config: Config = Config()
app: Flask = Flask("CUBERS_ACADEMY_WEBSITE")

setup(app= app, config= config)

if __name__ == '__main__':
    app.run(
        debug=config.is_debug_mode,
        port=config.port
    )
