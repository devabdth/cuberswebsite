from flask import Flask, session, redirect, request

from sys import path
path.insert(0, '../')


class ConfigRouter:
    def __init__(self, app: Flask):
        self.app: Flask = app

    def setup(self):
        self.assign_configurations()

    def assign_configurations(self):
        @self.app.route('/config/', methods=["PATCH"])
        def configurations():
            params = dict(request.values)
            for item in params.items():
                session[item[0]] = item[1]

            return self.app.response_class(status=200)
