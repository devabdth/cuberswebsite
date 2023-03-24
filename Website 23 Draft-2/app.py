from flask import Flask
from config import Config
from routers.home.router import home_routes
from routers.about.router import about_routes
from routers.terms.router import terms_routes
from routers.services.router import services_routes
from routers.contact.router import contact_routes
from routers.portfolio.router import portfolio_routes
from routers.tracking.router import tracking_routes
import os


def projects():
    from routers.portfolio.router import projects
    return list(projects.values())[:3]


config: Config = Config()
app: Flask = Flask(
    "CUBERS_WEBSITE",
    template_folder= os.path.abspath(os.path.join(os.path.dirname(__file__), './templates/')),
    static_folder= os.path.abspath(os.path.join(os.path.dirname(__file__), './static/')),
)

tracking_routes(
    app= app,
    config= config
)

home_routes(
    app=app,
    config=config,
)

about_routes(
    app=app,
    config=config,
)

terms_routes(
    app=app,
    config=config,
)

services_routes(
    app=app,
    config= config,
)

contact_routes(
    app=app,
    config=config,
)

portfolio_routes(
    app=app,
    config=config,
)


if __name__ == '__main__':
    app.run(
        port=config.port,
        debug=config.is_debug_mode,
    )
