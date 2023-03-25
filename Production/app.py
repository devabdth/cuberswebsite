from plugins.config import Config
from plugins.setup import Initialization

from os.path import abspath, dirname, join
from flask import Flask

# Configuration
cfg: Config= Config()

# Application
app: Flask= Flask(
    cfg.app_name,
    template_folder= abspath(join(dirname(__file__), "templates")),
    static_folder= abspath(join(dirname(__file__), "static")),
)

# Application Initializations
init= Initialization(app)
init.setup_app()
init.setup_routers()

# App Running without Gunicorn
if __name__ == '__main__':
    app.run(
        port= cfg.port,
        host= cfg.host,
        debug= cfg.mode == "DEBUG"
    )
