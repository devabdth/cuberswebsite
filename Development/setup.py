from flask import Flask

def setup(app: Flask) -> bool:
	try:
		from routers.home import HomeRouter as Home
		Home(app).setup()
		return True
	except Exception as e:
		print(e)
		return False