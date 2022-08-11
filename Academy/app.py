from flask import Flask

from config import Config
# Database Helper
from db.helper import DatabaseHelper

# Routers
from routers.form.router import FormRouter
from routers.images.router import ImagesRouter


config: Config = Config()
app: Flask = Flask("CUBERS_ACADEMY_WEBSITE")

# Initialize Database Helper
helper: DatabaseHelper = DatabaseHelper()

# Routers Assignment
form_router: FormRouter = FormRouter(
    app=app, config=config, database_helper=helper)
form_router.assign_routers()
images_router: ImagesRouter = ImagesRouter(app=app, config=config)
images_router.assign_routers()

app.run(
    debug=config.is_debug_mode,
    port=config.port
)
