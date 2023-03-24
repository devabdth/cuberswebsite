from flask import Flask, session, request
from json import loads, dumps
from sys import path
path.insert(0, '../')

from plugins.config import Config
from plugins.email import Email
from plugins.database import DBHelper

class LeadsRouter:
	def __init__(self, app: Flask):
		self.app: Flask= app
		self.cfg: Config= Config()
		self.db: DBHelper= DBHelper()
		self.email: Email= Email()

	def setup(self):
		self.assign_ticket_placement()
		self.assign_newsletter_subscribe()
		self.assign_leads_management()
		self.assign_consult_ticket_placement()


	def assign_consult_ticket_placement(self):
		@self.app.route('/global/leads/consult', methods=["POST"])
		def consult_ticket_placement():
			body= loads(request.data)
			res= self.db.add_consult_ticket_placement(body)
			print(res)
			if res == -1 :
				return self.app.response_class(status= 401)

			if res:
				res= self.email.consult_ticket_placement_successfully(body["email"])

			if res:
				return self.app.response_class(status= 201)

			return self.app.response_class(status= 500)


	def assign_ticket_placement(self):
		@self.app.route('/global/leads/tickets/', methods=["POST"])
		def ticket_placement():
			body= loads(request.data)
			res= self.db.add_ticket_placement(body)
			if res:
				res= self.email.ticket_placement_successfully(body["email"])
			if res:
				return self.app.response_class(status= 201)

			return self.app.response_class(status= 500)

	def assign_newsletter_subscribe(self):
		@self.app.route('/global/leads/newsletter/', methods=["POST"])
		def newsletter_subscribe():
			body= loads(request.data)
			res= self.db.add_newsletter_subscription(body)
			if res:
				res= self.email.subscription_successfull(body["email"])

			if res:
				return self.app.response_class(status= 201)

			return self.app.response_class(status= 500)
	
	def assign_leads_management(self):
		@self.app.route('/global/leads/', methods=["GET", "POST"])
		def leads_management():
			pass


	