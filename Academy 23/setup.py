from flask import Flask
from flask_session import Session

from config import Config
from content import Content
from database.helper import DBHelper


def init_app(app: Flask) -> bool:
    try:
        cfg: Config= Config()
        db_client= None
        database: DBHelper= DBHelper(db_client)
        con: Content= Content()

        app.config["SESSION_PERMANENT"] = False
        app.config["SESSION_TYPE"] = "filesystem"
        app.config["DEBUG"]= True
        Session(app)


        from routers.home.router import HomeRouter
        HomeRouter(
            app= app,
            database= database,
            cfg= cfg,
            con= con
        ).setup()

        return True
    except Exception as e:
        print(e)
        return False
