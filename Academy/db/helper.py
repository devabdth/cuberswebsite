from db.courses.helper import CoursesHelper
from db.forms.helper import FormsHelper
from db.instructors.helper import InstructorsHelper
from db.spaces.helper import SpacesHelper


class DatabaseHelper:
    def __init__(self):
        self.courses: CoursesHelper = CoursesHelper()
        self.instructors: InstructorsHelper = InstructorsHelper()
        self.spaces: SpacesHelper = SpacesHelper()
        self.froms: FormsHelper = FormsHelper()
