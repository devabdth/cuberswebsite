from flask import Flask, send_file, session

from os import mkdir
from os.path import join, abspath, dirname, exists


class ImagesRouter:
	def __init__(self, app: Flask):
		self.supported_cover_extensions: list= [
			'png', 'jpg', 'jpeg', 'webp', 'gif'
		]
		self.supported_asset_extensions: list= [
			'png', 'jpg', 'jpeg', 'webp', 'gif'
		]
		self.app: Flask= app
		self.assets_path= abspath(join(dirname(__file__), '../../assets'))
		self.covers_path= abspath(join(dirname(__file__), "../../assets/covers"))
		self.icons_path= abspath(join(dirname(__file__), "../../assets/icons"))
		self.blog_covers_path= abspath(join(dirname(__file__), "../../assets/covers/blog/"))
		self.blog_assets_path= abspath(join(dirname(__file__), "../../assets/assets"))

	def setup(self):
		if not exists(self.assets_path):
			mkdir(self.assets_path)

		if not exists(self.covers_path):
			mkdir(self.covers_path)

		if not exists(self.icons_path):
			mkdir(self.icons_path)

		if not exists(self.blog_covers_path):
			mkdir(self.blog_covers_path)

		if not exists(self.blog_assets_path):
			mkdir(self.blog_assets_path)

		self.assing_projects_covers()
		self.assing_projects_assets()
		self.assing_blog_covers()
		self.assing_projects_icons()

	def assing_blog_covers(self):
		@self.app.route('/images/blogCovers/<id>')
		def blog_covers(id):
			for sup_ext in self.supported_cover_extensions:
				path_= "{}.{}".format(id, sup_ext)
				if exists(join(self.blog_covers_path, path_)):
					return send_file(join(self.blog_covers_path, path_), mimetype="image/{}".format(sup_ext))

			return self.app.response_class(status= 404)

	def assing_projects_covers(self):
		@self.app.route('/images/covers/<pid>')
		def project_cover(pid):
			for sup_ext in self.supported_cover_extensions:
				path_= "{}.{}".format(pid, sup_ext)
				if exists(join(self.covers_path, path_)):
					return send_file(join(self.covers_path, path_), mimetype= 'image/{}'.format(sup_ext))


			return self.app.response_class(status= 404)


	def assing_projects_icons(self):
		@self.app.route('/images/icons/<pid>')
		def project_icon(pid):
			for sup_ext in self.supported_cover_extensions:
				path_= "{}.{}".format(pid, sup_ext)
				if exists(join(self.icons_path, path_)):
					return send_file(join(self.icons_path, path_), mimetype= 'image/{}'.format(sup_ext))


			return self.app.response_class(status= 404)


	def assing_projects_assets(self):
		@self.app.route('/images/assets/<fn>')
		def project_asset(fn):
			for sup_ext in self.supported_asset_extensions:
				path_= "{}".format(fn)
				print(join(self.blog_assets_path, path_))
				if exists(join(self.blog_assets_path, path_)):
					return send_file(join(self.blog_assets_path, path_), mimetype= 'image/{}'.format(sup_ext))


			return self.app.response_class(status= 404)

