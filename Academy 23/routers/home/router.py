import sys
sys.path.insert(0, '../')

from flask import Flask, render_template, session, url_for, redirect

from config import Config
from content import Content
from database.helper import DBHelper

class HomeRouter:
    def __init__(self, app: Flask, cfg: Config, con: Content, database: DBHelper):
        self.app: Flask= app
        self.cfg: Config= cfg
        self.con: Content= con
        self.database: DBHelper= DBHelper


    def setup(self):
        self.assign_home_route()


    def assign_home_route(self):
        @self.app.route('/', methods=["GET"])
        @self.app.route('/home/', methods=["GET"])
        @self.app.route('/index/', methods=["GET"])
        @self.app.route('/landingPage/', methods=["GET"])
        @self.app.route('/mainPage/', methods=["GET"])
        def home_route():
            lang= session.get("LANG", "en")
            return render_template(
                'home/index.html',
                cfg= self.cfg,
                con= self.con,
                db= self.database,
                lang= lang
            )
