from flask import Flask
from config import Config


# Database Helper
from db.helper import DatabaseHelper

# Routers
from routers.form.router import FormRouter
from routers.images.router import ImagesRouter
from routers.instructor.router import InstructorRouter
from routers.courses.router import CoursesRouter


contact_info: dict = {
    'facebook': "https://facebook.com/cubersacd",
    'instagram': "https://instagram.com/cuberacd",
    'linkedin': "https://linkedin.com/cuberacd",
    'email': "academy@cubersio.cm",
    'phone': "+20 112 916 4522",
    'address': "",
}

config: Config = Config()
app: Flask = Flask("CUBERS_ACADEMY_WEBSITE")

# Initialize Database Helper
helper: DatabaseHelper = DatabaseHelper()

# Routers Assignment
form_router: FormRouter = FormRouter(
    app=app, config=config, database_helper=helper, contact_info=contact_info)
form_router.assign_routers()
isntructor_router: InstructorRouter = InstructorRouter(
    app=app, config=config, database_helper=helper, contact_info=contact_info)
isntructor_router.assign_routers()
courses_router: CoursesRouter = CoursesRouter(
    app=app, config=config, database_helper=helper, contact_info=contact_info)
courses_router.assign_routers()

images_router: ImagesRouter = ImagesRouter(app=app, config=config)
images_router.assign_routers()


def runner():
    app.run()