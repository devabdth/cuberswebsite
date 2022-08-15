import os
import json
import pandas as pd

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
        forms_: list = []
        for form in list(self.forms_data.values()):
            forms_.append(form)

        return forms_
    
    def validate_unique_form(self, email, course_id):
        if len(self.get_all_forms()) == 0:
            return True
        df = pd.DataFrame(self.get_all_forms())
        df = df.loc[df["courseId"] == course_id]
        df = df.loc[df["email"] == email]
        print(df)
        return len(df) == 0


    def create_form(self, payload):
        if not self.validate_unique_form(payload["email"], payload["courseId"]):
            return False
        if len(list(self.forms_data.keys())) == 0:
            id: int = 0
        else: 
            print(type(list(self.forms_data.keys())[-1]))
            id: int= int(list(self.forms_data.keys())[-1]) + 1
        
        self.forms_data["{}".format(id)] = dict(payload)
        self.save()
        return True

