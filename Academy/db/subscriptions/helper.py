import os
import json


class SubscriptionsHelper:
    def __init__(self):

        base_path: str = os.path.join(os.path.dirname(__file__), "../dbs")
        self.subscriptions_path = os.path.abspath(os.path.join(
            base_path, "{}.json".format("subscriptions")))

        self.load()

    def load(self):
        with open(self.subscriptions_path) as file:
            data = json.load(file)
            self.subscriptions_data: dict = dict(data)

    def save(self):
        with open(self.subscriptions_path, 'w') as f:
            json.dump(self.subscriptions_data, f)
            f.close()
