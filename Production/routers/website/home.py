from plugins.database import DBHelper
from plugins.content import Content
from plugins.config import Config
from plugins.utils import Utils
from flask import Flask, render_template, session, url_for, redirect

from sys import path
path.insert(0, '../')


class HomeRouter:
    def __init__(self, app: Flask):
        self.app: Flask = app
        self.cfg: Config = Config()
        self.content: Content = Content()
        self.db: DBHelper = DBHelper()

    def setup(self):
        self.assign_home_index()

    def assign_home_index(self):
        @self.app.route('/', methods=["GET"])
        @self.app.route('/home/', methods=["GET"])
        @self.app.route('/mainPage/', methods=["GET"])
        @self.app.route('/overview/', methods=["GET"])
        @self.app.route('/main/', methods=["GET"])
        @self.app.route('/landingPage/', methods=["GET"])
        def home_index():
            lang: str = session.get("LANG", "en")
            mode: str = "light" if session.get("MODE", "light") == "dark" else "dark"

            return render_template(
                "website/home.html",
                cfg=self.cfg,
                content=self.content,
                db=self.db,
                lang=lang,
                mode=mode,
                utils= Utils(),
                dir= "rtl" if lang == 'ar' else "ltr",
                primary_font_family="Cairo" if lang == "ar" else "Raleway",
                secondary_font_family="Cairo" if lang == "ar" else "Poppins"
            )
