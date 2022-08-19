from db.courses.helper import CoursesHelper
from db.forms.helper import FormsHelper
from db.instructors.helper import InstructorsHelper
from db.spaces.helper import SpacesHelper
from db.subscriptions.helper import SubscriptionsHelper


class DatabaseHelper:
    def __init__(self):
        self.courses: CoursesHelper = CoursesHelper()
        self.instructors: InstructorsHelper = InstructorsHelper()
        self.spaces: SpacesHelper = SpacesHelper()
        self.forms: FormsHelper = FormsHelper()
        self.subscriptions: SubscriptionsHelper = SubscriptionsHelper()
