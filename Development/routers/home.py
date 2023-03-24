from flask import Flask, render_template, url_for, session

import sys
sys.path.insert(0, '../')

from config import Config
from content import Content



class HomeRouter:
	def __init__(self, app: Flask):
		self.app: Flask= app
		self.cfg: Config= Config()
		self.content: Content= Content()


	def setup(self):
		self.assign_home_index()


	def assign_home_index(self):
		@self.app.route('/', methods=["GET"])
		@self.app.route('/home/', methods=["GET"])
		@self.app.route('/landingPage/', methods=["GET"])
		@self.app.route('/main/', methods=["GET"])
		@self.app.route('/mainPage/', methods=["GET"])
		@self.app.route('/overview/', methods=["GET"])
		def home_index():
			lang: str= session.get("LANG", "en")
			return render_template(
				'home.html',
				cfg= self.cfg,
				content= self.content,
				lang= lang,
			)