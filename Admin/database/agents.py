import os
import csv


class Agents:
	def __init__(self):
		self.data = self.load()

	def load(self):
		data = []
		with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'database/agents.csv'))) as f:
			reader = csv.reader(f)
			
			for row in reader:
				agent = {
	    			"id": row[0],
	    			"name": row[1],
	    			"email": row[2],
	    			"phone": row[3],
	    			"address": row[4],
	    			"position": row[5],
	    			"hiringType": row[6],
	    			"password": row[7],
				}
				data.append(agent)
		return data

	def get(self, _id):
		for agent in self.data:
			if agent['id'] == _id:
				return agent

		return None