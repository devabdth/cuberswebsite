import os
import json


class InstructorsHelper:
    def __init__(self):

        base_path: str = os.path.join(os.path.dirname(__file__), "../dbs")
        self.instructors_path = os.path.abspath(os.path.join(
            base_path, "{}.json".format("instructors")))

        self.load()

    def load(self):
        with open(self.instructors_path) as file:
            data = json.load(file)
            self.instructors_data: dict = dict(data)

    def get_all_instructors(self):
        return list(self.instructors_data.values())



    def get_instructor_by_id(self, id: int) -> dict:
        data: dict = {}
        data["instructor"] = self.instructors_data["{}".format(id)]
        return data
