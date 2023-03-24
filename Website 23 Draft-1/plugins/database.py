from os.path import join, abspath, dirname
from json import loads, dump
from pandas import DataFrame

from .config import Config


class DBHelper:
	def __init__(self):
		self.cfg: Config = Config()
		self.init_blog_data()
		self.init_projects_data()
		self.init_leads_data()
		self.init_tracking_data()

	def init_tracking_data(self):
		with open(abspath(join(dirname(__file__), '../jsons/trackingData.json')), 'r') as f:
			self.tracking_data= loads(f.read())


	def init_leads_data(self):
		with open(abspath(join(dirname(__file__), '../jsons/leads.json')), 'r') as f:
			self.leads_data= dict(loads(f.read()))
			self.newsletter_dataframe= DataFrame(self.leads_data["newsletter"], columns=["name", "email", "topics"])
			self.tickets_dataframe= DataFrame(self.leads_data["tickets"], columns=["name", "email", "message", "placedIn"])
			self.consult_ticktes_dataframe= DataFrame(self.leads_data["consultTicktes"], columns=["name", "email", "website", "message", "placedIn"])

	def init_blog_data(self):
		with open(abspath(join(dirname(__file__), '../jsons/blog.json')), 'r') as f:
			data: dict = dict(loads(f.read()))
			self.blogs = {}
			for blog in data.values():
				blog["url"] = blog["attachedUrl"].replace(
					"$url", self.cfg.base_url)
				for blog_part in blog["parts"]:
					blog_part["attachedUrl"] = blog_part["attachedUrl"].replace(
						"$url", self.cfg.base_url)
				self.blogs[blog["id"]] = blog

	def init_projects_data(self):
		with open(abspath(join(dirname(__file__), '../jsons/projects.json')), 'r') as f:
			data: dict = dict(loads(f.read()))

			# Setting up Website Projects
			self.websites_projects: dict = data["websites"]
			for web_proj in self.websites_projects.values():
				if '$url' in web_proj['action']:
					web_proj['action'] = web_proj['action'].replace(
						'$url', self.cfg.base_url)
				if '$id' in web_proj['action']:
					web_proj['action'] = web_proj['action'].replace(
						'$id', web_proj['id'])

			self.applications_projects: dict = data["applications"]
			for app_proj in self.applications_projects.values():
				if '$url' in app_proj['action']:
					app_proj['action'] = app_proj['action'].replace(
						'$url', self.cfg.base_url)
				if '$id' in app_proj['action']:
					app_proj['action'] = app_proj['action'].replace(
						'$id', app_proj['id'])
			self.systems_projects: dict = data["systems"]
			for sys_proj in self.systems_projects.values():
				if '$url' in sys_proj['action']:
					sys_proj['action'] = sys_proj['action'].replace(
						'$url', self.cfg.base_url)
				if '$id' in sys_proj['action']:
					sys_proj['action'] = sys_proj['action'].replace(
						'$id', sys_proj['id'])

	def get_project_by_id(self, pid: str = None):
		if pid == None:
			return

		for web_proj in self.websites_projects.keys():
			if pid == web_proj:
				return self.websites_projects[pid]

		for app_proj in self.applications_projects.keys():
			if pid == app_proj:
				return self.applications_projects[pid]

		for sys_proj in self.systems_projects.keys():
			if pid == sys_proj:
				return self.systems_projects[pid]


	def add_newsletter_subscription(self, payload):
		try:
			from datetime import datetime
			self.init_leads_data()
			is_subscribed= len(self.newsletter_dataframe.loc[self.newsletter_dataframe['email'] == payload["email"]]) != 0
			if is_subscribed:
				row= self.newsletter_dataframe.loc[self.newsletter_dataframe['email'] == payload["email"]].to_dict()
				row= {
					"name": row["name"][0],
					"email": row["email"][0],
					"topics": row["topics"][0],
				}
				row["topics"]= list(set(payload["topics"] + row["topics"]))
				self.newsletter_dataframe= self.newsletter_dataframe.drop(self.newsletter_dataframe.loc[self.newsletter_dataframe['email'] == payload["email"]].index)
				self.newsletter_dataframe= self.newsletter_dataframe.append(row, ignore_index= True)
				if self.save_leads_data():
					return True

			row= {
				"name": payload["name"],
				"email": payload["email"],
				"topics": list(payload["topics"]),
			}

			self.newsletter_dataframe= self.newsletter_dataframe.append(row, ignore_index= True)
			if self.save_leads_data():
				return True


			return False
		except Exception as e:
			print(e)
			return False

	def add_consult_ticket_placement(self, payload):
		try: 
			from datetime import datetime
			ticket_exists= len(self.consult_ticktes_dataframe.loc[self.consult_ticktes_dataframe["email"] == payload["email"]])
			if ticket_exists:
				return -1

			row= {
				"name": payload["name"],
				"email": payload["email"],
				"message": payload["msg"],
				"website": payload["url"],
				"placedIn": str(datetime.now())
			}

			self.consult_ticktes_dataframe= self.consult_ticktes_dataframe.append(row, ignore_index= True)
			if self.save_leads_data():
				return True

		except Exception as e:
			print(e)
			return False

	def add_ticket_placement(self, payload):
		try:
			from datetime import datetime
			ticket_exists= len(self.tickets_dataframe.loc[self.tickets_dataframe["email"] == payload["email"]])
			if ticket_exists:
				row= self.tickets_dataframe.loc[self.tickets_dataframe['email'] == payload["email"]].to_dict()
				row= {
					"name": row["name"][0],
					"email": row["email"][0],
					"message": row["message"][0],
					"placedIn": row["placedIn"][0]
				}

				row["message"]= '{}\n\n{}\n{}'.format(
					row["message"],
					payload["message"],
					datetime.now()
				)

				self.tickets_dataframe= self.tickets_dataframe.drop(self.tickets_dataframe.loc[self.tickets_dataframe['email'] == payload["email"]].index)
				self.tickets_dataframe= self.tickets_dataframe.append(row, ignore_index= True)
				if self.save_leads_data():
					return True

			row= {
				"name": payload["name"],
				"email": payload["email"],
				"message": "{}\n{}".format(payload["message"], str(datetime.now())),
				"placedIn": str(datetime.now())
			}

			self.tickets_dataframe= self.tickets_dataframe.append(row, ignore_index= True)
			if self.save_leads_data():
				return True


				return False
		except Exception as e:
			print(e)
			return False


	def save_leads_data(self):
		try:
			with open(abspath(join(dirname(__file__), '../jsons/leads.json')), 'w') as f:
				self.leads_data["newsletter"]= [{
					"name": row["name"],
					"email": row["email"],
					"topics": row["topics"],
				} for _, row in self.newsletter_dataframe.iterrows()]
				self.leads_data["tickets"]= [{
					"name": row["name"],
					"email": row["email"],
					"message": row["message"],
					"placedIn": row["placedIn"],
				} for _, row in self.tickets_dataframe.iterrows()]
				self.leads_data["consultTicktes"]= [{
					"name": row["name"],
					"email": row["email"],
					"message": row["message"],
					"website": row["website"],
					"placedIn": row["placedIn"],
				} for _, row in self.consult_ticktes_dataframe.iterrows()]
				dump(self.leads_data, f)
			return True
		except Exception as e:
			print(e)
			return False

	def write_tracking_data(self):
		with open(abspath(join(dirname(__file__), '../jsons/trackingData.json')), 'w') as f:
			dump(self.tracking_data, f)


	def get_project_tracking_data(self, pid_: str) -> False:
		for pid in self.tracking_data.keys():
			if pid == pid_:
				return self.tracking_data[pid]

		return None

	def update_tracking_data(self, **kwargs):
		print(kwargs)
		if 'project' in kwargs.keys():
			pass
		if 'token' in kwargs.keys() and 'value' in kwargs.keys():
			self.tracking_data[kwargs['pid']][kwargs['token']]= kwargs['value']
			self.write_tracking_data()
			return True

		raise KeyError('Missing important values to update!')


	def get_projects_by_category(self, category):
		if category == 'website':
			return self.websites_projects
		if category == 'application':
			return self.applications_projects
		if category == 'system':
			return self.systems_projects
