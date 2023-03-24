import os
import json


class ProjectsHelper:
    def __init__(self):
        self.base_bath: str = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 'dbs/projects.json'))

    def load(self):
        with open(self.base_bath, encoding='utf-8') as f:
            self.data = dict(json.loads(f.read()))

    def save(self):
        with open(self.base_bath, 'w+') as f:
            json.dump(self.data, f)
            f.close()

    def get_project_by_id(self, id: int) -> dict:
        self.load()
        try:
            project_ = self.data["{}".format(id)]
            return project_

        except Exception as e:
            print(e)
            return None
