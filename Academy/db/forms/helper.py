import os
import json


class FormsHelper:
    def __init__(self):

        base_path: str = os.path.join(os.path.dirname(__file__), "../dbs")
        self.forms_path = os.path.abspath(os.path.join(
            base_path, "{}.json".format("forms")))

    def load(self):
        with open(self.forms_path) as file:
            data = json.load(file)
            self.forms_data: dict = dict(data)

    def save(self):
        with open(self.forms_path, 'w') as file:
            json.dump(self.forms_data, file)

    def get_all_forms(self):
        self.load()
        forms_: list = []
        for form in list(self.forms_data.values()):
            forms_.append(form)

        return forms_

    def validate_unique_form(self, email, course_id):
        if len(self.get_all_forms()) == 0:
            return True

        for form in self.get_all_forms():
            if form["courseId"] == course_id and form["email"] == email:
                return False

        return True

    def create_form(self, payload):
        try:
            if not self.validate_unique_form(payload["email"], payload["courseId"]):
                return None
            if len(list(self.forms_data.keys())) == 0:
                id: int = 0
            else:
                id: int = int(list(self.forms_data.keys())[-1]) + 1
        except Exception as e:
            print("Error: {}".format(e))


        self.forms_data["{}".format(id)] = dict(payload)
        self.save()
        return id
