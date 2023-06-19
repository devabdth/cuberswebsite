from flask import Flask, render_template, url_for, session, redirect
from json import dumps as jsonParser

from sys import path
path.insert(0, '../')


from plugins.config import Config
from plugins.content import Content
from plugins.database import DBHelper


class ProjectsRouter:
	def __init__(self, app: Flask):
		self.app: Flask= app
		self.cfg: Config= Config()
		self.content: Content= Content()
		self.db: DBHelper= DBHelper()

	def setup(self):
		self.assign_projects_index()
		self.assign_single_project_index()
		self.assign_websites_projects_index()
		self.assign_applications_projects_index()
		self.assign_systems_projects_index()

	def assign_websites_projects_index(self):
		@self.app.route('/projects/websites/', methods=["GET"])
		def websites_projects_index():
			mode: str= "light" if session.get("MODE", "dark") == "dart" else "light"
			lang= session.get("LANG", "en")
			return render_template(
				"website/projectsWebsites.html",
				cfg= self.cfg,
				projects=  list(self.db.websites_projects.values()),
				content= self.content,
				db= self.db,
				mode= mode,
				lang= lang,
				jsonParser= jsonParser,
				dir= "rtl" if lang == 'ar' else "ltr",
				primary_font_family= "Cairo" if lang == 'ar' else 'Raleway',
				secondary_font_family= "Cairo" if lang == 'ar' else "Poppins"
			)

	def assign_applications_projects_index(self):
		@self.app.route('/projects/applications/', methods=["GET"])
		def applications_projects_index():
			mode: str= "light" if session.get("MODE", "dark") == "dart" else "light"
			lang= session.get("LANG", "en")
			return render_template(
				"website/projectsApplications.html",
				cfg= self.cfg,
				projects= list(self.db.applications_projects.values()),
				content= self.content,
				db= self.db,
				mode= mode,
				lang= lang,
				jsonParser= jsonParser,
				dir= "rtl" if lang == 'ar' else "ltr",
				primary_font_family= "Cairo" if lang == 'ar' else 'Raleway',
				secondary_font_family= "Cairo" if lang == 'ar' else "Poppins"
			)

	def assign_systems_projects_index(self):
		@self.app.route('/projects/systems/', methods=["GET"])
		def systems_projects_index():
			mode: str= "light" if session.get("MODE", "dark") == "dart" else "light"
			lang= session.get("LANG", "en")
			return render_template(
				"website/projectsSystems.html",
				cfg= self.cfg,
				projects= list(self.db.systems_projects.values()),
				content= self.content,
				db= self.db,
				mode= mode,
				lang= lang,
				jsonParser= jsonParser,
				dir= "rtl" if lang == 'ar' else "ltr",
				primary_font_family= "Cairo" if lang == 'ar' else 'Raleway',
				secondary_font_family= "Cairo" if lang == 'ar' else "Poppins"
			)


	def assign_single_project_index(self):
		@self.app.route('/project/<pid>', methods=["GET"])
		def single_projcet_index(pid):
			mode: str = "light" if session.get("MODE", "dark") == "dark" else "dark"
			lang= session.get("LANG", "en")

			self.db.init_projects_data()
			project: dict= self.db.get_project_by_id(
				pid= pid
			)

			return render_template(
				"website/single_project.html",
				cfg= self.cfg,
				project= project,
				content= self.content,
				db= self.db,
				mode= mode,
				lang= lang,
				jsonParser= jsonParser,
				dir= "rtl" if lang == 'ar' else "ltr",
				primary_font_family="Cairo" if lang == "ar" else "Raleway",
				secondary_font_family="Cairo" if lang == "ar" else "Poppins"
			)



	def assign_projects_index(self):
		@self.app.route('/projects/', methods=["GET"])
		@self.app.route('/portfolio/', methods=["GET"])
		@self.app.route('/works/', methods=["GET"])
		def projects_index():
			mode: str = "light" if session.get("MODE", "dark") == "dark" else "dark"
			lang= session.get("LANG", "en")
			self.db.init_projects_data()
			return render_template(
				"website/projects.html",
				cfg= self.cfg,
				content= self.content,
				db= self.db,
				mode= mode,
				lang= lang,
				jsonParser= jsonParser, 
				dir= "rtl" if lang == 'ar' else "ltr",
				primary_font_family="Cairo" if lang == "ar" else "Raleway",
				secondary_font_family="Cairo" if lang == "ar" else "Poppins",
				website_projects= jsonParser(list(self.db.websites_projects.values())[:3])
					.replace(u'<', u'\\u003c').replace(u'>', u'\\u003e')
					.replace(u'&', u'\\u0026').replace(u"'", u'\\u0027'),
				applications_projects= jsonParser(list(self.db.applications_projects.values())[:3])
					.replace(u'<', u'\\u003c').replace(u'>', u'\\u003e')
					.replace(u'&', u'\\u0026').replace(u"'", u'\\u0027'),
				systems_projects= jsonParser(list(self.db.systems_projects.values())[:3])
					.replace(u'<', u'\\u003c').replace(u'>', u'\\u003e')
					.replace(u'&', u'\\u0026').replace(u"'", u'\\u0027')

			)
