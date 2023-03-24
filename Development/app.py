from flask import Flask
import os
from setup import setup

app: Flask= Flask(
	"DEVELOPMENT_PORTFOLIO",
	template_folder= os.path.join(os.path.dirname(__file__), "templates/"),
	static_folder= os.path.join(os.path.dirname(__file__), "templates/")
)

setup(app)


app.run(
	debug= True,
	port= 9999
)