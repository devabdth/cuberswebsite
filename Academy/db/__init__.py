import os

base_path: str = os.path.join(os.path.dirname(__file__), "dbs")
if not os.path.exists(base_path):
    os.mkdir(base_path)


dbs: list = ["courses", "instructors", "forms", "spaces"]
for db in dbs:
    path_ = os.path.abspath(os.path.join(base_path, "{}.json".format(db)))
    if not os.path.exists(path_):
        with open(path_, 'a'):
            os.utime(path_, None)
