class Content:
	def __init__(self):
		self.load()


	def load(self):
		self.tabs: dict= {
			"en": {
				"home": "Home",
				"about": "About",
				"projects": "Projects",
				"contact": "Contact"
			}
		}

		self.actions: dict= {
			"en": {
				"getStarted": "Get Started"
			}
		}

		self.gbl_content: dict= {
			"en": {
				""
			}
		}