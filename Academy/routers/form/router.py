from flask import Flask, render_template, url_for, request
import os
import json


class FormRouter:
    def __init__(self, app: Flask, config, database_helper, contact_info: dict = {}):
        self.app = app
        self.prefix = "forms"
        self.database_helper = database_helper
        self.contact_info = contact_info

    def assign_routers(self):
        self.assign_application()
        self.assign_post_application()

    def assign_post_application(self):
        @self.app.route("/{}/post/".format(self.prefix), methods=["POST"])
        def create_application():
            try:
                data = request.data
                payload = json.loads(data)

                self.database_helper.forms.load()
                if not self.database_helper.forms.create_form(payload):
                    return self.app.response_class(status=500, response= json.dumps({"msg": "Duplicated Form"}))

                return self.app.response_class(status=201)
            except Exception as e:
                print("Creating Form: {}".format(e))
                return self.app.response_class(status=500, response= json.dumps({"msg": "This is Error Msg"}))

    def assign_application(self):
        @self.app.route("/courses/<course_id>/{}/".format(self.prefix), methods=["GET"])
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
                meta_info=self.contact_info,
                images_url="http://127.0.0.1:3000/images"
            )
