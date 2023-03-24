import os
import csv


class Leads:
	def __init__(self):
		self.data = self.load()

	def load(self):
		data = []
		with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'database/leads.csv'))) as f:
			reader = csv.reader(f)
			for row in reader:
				if row[0] != 'name':
					lead = {
		    			"name": row[0],
		    			"email": row[1],
		    			"phone": row[2],
		    			"position": row[3],
		    			"agentName": row[4],
		    			"category": int(row[5]),
		    			"address": row[6],

					}
					data.append(lead)
		return data

	def add(self, payload):
		try:
			line = '{},{},{},{},{},{},{},{}'.format(
				payload["name"],
			    payload["email"],
			    payload["phone"],
			    payload["position"],
			    payload["agentName"],
			    payload["category"],
			    payload["address"],
			    payload["agent"]
			)

			with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'database/leads.csv')), 'a') as f:
				f.write('\n{}'.format(line))

			return True

		except Exception as e:
			print(e)
			return False



