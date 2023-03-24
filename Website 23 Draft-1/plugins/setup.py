from flask import Flask
from flask_session import Session

class Initialization:
    def __init__(self, app: Flask):
        self.app: Flask= app


    def setup_app(self):
        self.app.config["SESSION_PERMANENT"] = False
        self.app.config["SESSION_TYPE"] = "filesystem"

        Session(self.app)

    def setup_routers(self):
        # Global Routers
        from routers.global_.leads import LeadsRouter
        LeadsRouter(app= self.app).setup()
        # Website Routers
        from routers.website.home import HomeRouter
        HomeRouter(app= self.app).setup()

        from routers.website.about import AboutRouter
        AboutRouter(app= self.app).setup()

        from routers.website.projects import ProjectsRouter
        ProjectsRouter(app= self.app).setup()

        from routers.website.images import ImagesRouter
        ImagesRouter(app= self.app).setup()

        from routers.website.tracking import TrackingRouter
        TrackingRouter(app= self.app).setup()

        from routers.website.blog import BlogRouter
        BlogRouter(app= self.app).setup()

        from routers.website.contact import ContactRouter
        ContactRouter(app= self.app).setup()

        from routers.website.config import ConfigRouter
        ConfigRouter(app= self.app).setup()