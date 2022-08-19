from .form.router import FormRouter
from .images.router import ImagesRouter
from .instructor.router import InstructorRouter
from .courses.router import CoursesRouter
from .home.router import HomeRouter
from .operations.router import OperationsRouter
from .instructors.router import InstructorsRouter
from .about.router import AboutRouter

def setup(app, config) -> bool:
    try:

        HomeRouter(app=app, config=config).assign_routers()

        FormRouter(app=app, config=config).assign_routers()

        InstructorRouter(app=app, config=config).assign_routers()

        CoursesRouter(app=app, config=config).assign_routers()

        InstructorsRouter(app=app, config=config).assign_routers()

        ImagesRouter(app=app, config=config).assign_routers()

        OperationsRouter(app= app, config=config).assign_routers()

        AboutRouter(app= app, config= config).assign_routers()


    except Exception as e:
        print(str(e))
        return False

    return True
