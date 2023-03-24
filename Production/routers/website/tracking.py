from flask import Flask, render_template, url_for, redirect, session, request
from json import loads, dumps
from sys import path
path.insert(0, '../')

from plugins.config import Config
from plugins.content import Content
from plugins.database import DBHelper


class TrackingRouter:
	def __init__(self, app: Flask):
		self.app: Flask= app
		self.cfg: Config= Config()
		self.content: Content= Content()
		self.database: DBHelper= DBHelper()
		self.prefix: str= 'tracking'


	def setup(self):
		self.assign_tracking_index()


	def assign_tracking_index(self):
		@self.app.route('/{}/'.format(self.prefix), methods=["GET", "PATCH", "DELETE"])
		def tracking_index():
			if request.method == 'GET':
				current_project= session.get('CURRENT_PROJECT', None)
				lang: str = session.get("LANG", "en")
				mode: str = "light" if session.get("MODE", "dark") == "dark" else "dark"
				if current_project == None:
					return render_template(
						'website/trackingForm.html',
						cfg= self.cfg,
						content= self.content,
						lang= lang,
						mode= mode,
		   				dir= "rtl" if lang == 'ar' else "ltr",
		                primary_font_family="Cairo" if lang == "ar" else "Raleway",
		                secondary_font_family="Cairo" if lang == "ar" else "Poppins"
					)
				project= self.database.get_project_tracking_data(pid_= current_project)

				return render_template(
					'website/tracking.html',
					project= project,
					cfg=self.cfg,
	                content=self.content,
	                prefix=self.prefix,
	                lang=lang,
	                mode=mode,
	                dir= "rtl" if lang == 'ar' else "ltr",
	                primary_font_family="Cairo" if lang == "ar" else "Raleway",
	                secondary_font_family="Cairo" if lang == "ar" else "Poppins"
				)
			elif request.method == 'PATCH':
				body= dict(loads(request.data))
				project= self.database.get_project_tracking_data(
					pid_= body['id']
				)

				if project == None:
					return self.app.response_class(status= 404)

				if project['accessKey'] == body['accessKey']:
					from datetime import datetime
					session["CURRENT_PROJECT"]= body['id']
					self.database.update_tracking_data(
						pid= body['id'],
						token= 'lastLoginIn',
						value= str(datetime.now())
					)
					return self.app.response_class(status= 200)

				else:
					return self.app.response_class(status= 403)

			elif request.method== "DELETE":
				session.pop("CURRENT_PROJECT")
				return self.app.response_class(status= 200)

