from flask import Flask, render_template, url_for, redirect, session

from sys import path
path.insert(0, '../')

from plugins.config import Config
from plugins.content import Content
from plugins.database import DBHelper


class AboutRouter:
	def __init__(self, app: Flask):
		self.app: Flask= app
		self.cfg: Config= Config()
		self.content: Content= Content()
		self.db: DBHelper= DBHelper()


	def setup(self):
		self.assign_about_index()

	def assign_about_index(self):
		@self.app.route('/about/', methods=["GET"])
		@self.app.route('/whoAreWe/', methods=["GET"])
		@self.app.route('/info/', methods=["GET"])
		@self.app.route('/trustBetweenUs/', methods=["GET"])
		def about_index():
			mode: str = "light" if session.get("MODE", "dark") == "dark" else "dark"
			lang= session.get("LANG", "en")

			return render_template(
				"website/about.html",
				cfg= self.cfg,
				content= self.content,
				db= self.db,
				mode= mode,
				lang= lang, 
				dir= "rtl" if lang == 'ar' else "ltr",
				primary_font_family="Cairo" if lang == "ar" else "Raleway",
				secondary_font_family="Cairo" if lang == "ar" else "Poppins"

			)
