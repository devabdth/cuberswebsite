from flask import Flask, render_template, url_for, request
import os
import json


class FormRouter:
    def __init__(self, app: Flask, config, database_helper):
        self.app = app
        self.prefix = "forms"
        self.database_helper = database_helper

    def assign_routers(self):
        self.assign_application()
        self.assign_post_application()

    def assign_post_application(self):
        @self.app.route("/{}/post/".format(self.prefix), methods=["POST"])
        def create_application():
            data = request.data
            print(json.loads(data))
            print(dict(json.loads(data))["name"])

            return self.app.response_class(status=201)

    def assign_application(self):
        @self.app.route("/<course_id>/{}/".format(self.prefix), methods=["GET"])
        def application_route(course_id: int):
            self.database_helper.courses.load()
            data = self.database_helper.courses.get_course_by_id(
                course_id)
            return render_template(
                "form/index.html",
                course=data["course"],
                course_id=data["course"]["id"],
                instructor=data["instructor"],
                instructor_id=data["instructor"]["id"],
                space=data["space"],
                space_id=data["space"]["id"],
                images_url="http://127.0.0.1:3000/images"
            )
