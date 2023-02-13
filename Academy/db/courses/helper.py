import os
import json


class CoursesHelper:
    def __init__(self):

        base_path: str = os.path.join(os.path.dirname(__file__), "../dbs")
        self.courses_path = os.path.abspath(os.path.join(
            base_path, "{}.json".format("courses")))
        self.instructors_path = os.path.abspath(os.path.join(
            base_path, "{}.json".format("instructors")))
        self.spaces_path = os.path.abspath(os.path.join(
            base_path, "{}.json".format("spaces")))

        self.load()

    def load(self):
        with open(self.courses_path) as file:
            data = json.load(file)
            self.courses_data: dict = dict(data)
        with open(self.instructors_path) as file:
            data = json.load(file)
            self.instructors_data: dict = dict(data)
        with open(self.spaces_path) as file:
            data = json.load(file)
            self.spaces_data: dict = dict(data)

    def get_all_courses(self):
        courses_ = []
        for course in list(self.courses_data.values()):
            course["instructor"] = self.instructors_data["{}".format(
                course["instructorId"])]["name"]
            course["space_name"] = self.spaces_data["{}".format(
                course["space"])]["name"]
            courses_.append(course)
        return self.courses_data.values()

    def get_course_by_id(self, id: int) -> dict:
        data: dict = {}
        data["course"] = self.courses_data["{}".format(id)]
        data["instructor"] = self.instructors_data["{}".format(
            data["course"]["instructorId"])]
        data["space"] = self.spaces_data["{}".format(
            data["course"]["space"])]
        return data

    def get_courses_by_instructor_id(self, instructor_id: int) -> list:
        courses: list = []
        for course in self.courses_data.values():
            if course["instructorId"] == str(instructor_id):
                course["rate"] = sum(course["rates"]) / len(course["rates"])
                courses.append(course)

        return courses
