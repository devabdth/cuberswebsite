from plugins.database import DBHelper
from plugins.content import Content
from plugins.config import Config
from plugins.utils import Utils
from flask import Flask, render_template, url_for, session

from sys import path
path.insert(0, '../')


class BlogRouter:
    def __init__(self, app: Flask):
        self.app: Flask = app
        self.cfg: Config = Config()
        self.content: Content = Content()
        self.database: DBHelper = DBHelper()
        self.utils: Utils = Utils()

    def setup(self):
        self.assign_all_blogs_index()
        self.assign_single_article_index()

    def assign_single_article_index(self):
        @self.app.route('/articles/<id>', methods=["GET"])
        def single_article_index(id):
            lang = session.get('LANG', 'en')
            mode = session.get('MODE', 'en')
            from json import dumps
            return render_template(
                'website/singleBlog.html',
                article_id= id,
                dumps= dumps,
                cfg=self.cfg,
                content=self.content,
                db=self.database,
                lang=lang,
                dir='rtl' if lang == 'ar' else 'ltr',
                mode=mode,
                primary_font_family="Cairo" if lang == "ar" else "Raleway",
                secondary_font_family="Cairo" if lang == "ar" else "Poppins",
                utils=self.utils
            )

    def assign_all_blogs_index(self):
        @self.app.route('/blog/', methods=['GET'])
        @self.app.route('/blogs/', methods=['GET'])
        @self.app.route('/articles/', methods=['GET'])
        @self.app.route('/journals/', methods=['GET'])
        def all_blogs_index():
            lang = session.get('LANG', 'en')
            mode = session.get('MODE', 'en')
            from json import dumps
            return render_template(
                'website/blog.html',
                cfg=self.cfg,
                dumps= dumps,
                content=self.content,
                db=self.database,
                lang=lang,
                dir='rtl' if lang == 'ar' else 'ltr',
                mode=mode,
                primary_font_family="Cairo" if lang == "ar" else "Raleway",
                secondary_font_family="Cairo" if lang == "ar" else "Poppins",
                utils=self.utils
            )
