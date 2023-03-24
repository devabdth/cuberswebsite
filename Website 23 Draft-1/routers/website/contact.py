from flask import Flask, render_template, url_for, session

from sys import path
path.insert(0, '../')


from plugins.config import Config
from plugins.content import Content
from plugins.database import DBHelper


class ContactRouter:
	def __init__(self, app: Flask):
		self.app: Flask = app
		self.cfg: Config = Config()
		self.content: Content = Content()
		self.db: DBHelper = DBHelper()


	def setup(self):
		self.assign_contact_index()


	def assign_contact_index(self):
		@self.app.route('/contact/', methods=["GET"])
		@self.app.route('/findUs/', methods=["GET"])
		@self.app.route('/reachUs/', methods=["GET"])
		@self.app.route('/booking/', methods=["GET"])
		def contact_index():
			lang= session.get('LANG', 'en')
			mode= session.get('MODE', 'light')
			return render_template(
				'website/contact.html',
				cfg= self.cfg,
				db= self.db,
				mode= mode,
				lang= lang,
				content= self.content,
				dir= "rtl" if lang == "ar" else "ltr",
				primary_font_family="Cairo" if lang == "ar" else "Raleway",
				secondary_font_family="Cairo" if lang == "ar" else "Poppins"
			)
