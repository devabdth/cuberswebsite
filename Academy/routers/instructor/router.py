from flask import Flask, render_template, url_for, request
import os
import json


class InstructorRouter:
    def __init__(self, app: Flask, config, database_helper, contact_info: dict = {}):
        self.app = app
        self.prefix = "instructor"
        self.database_helper = database_helper
        self.contact_info = contact_info

    def assign_routers(self):
        self.assign_instructor()
        self.assign_post_instructor()

    def assign_post_instructor(self):
        @self.app.route("/{}/post/".format(self.prefix), methods=["POST"])
        def create_instructor():
            data = request.data
            print(json.loads(data))
            print(dict(json.loads(data))["name"])

            return self.app.response_class(status=201)

    def assign_instructor(self):
        @self.app.route("/{}/<instructor_id>".format(self.prefix), methods=["GET"])
        def instructor_route(instructor_id: int):
            self.database_helper.instructors.load()
            self.database_helper.courses.load()
            data = self.database_helper.instructors.get_instructor_by_id(
                instructor_id)
            courses = self.database_helper.courses.get_courses_by_instructor_id(
                int(instructor_id))
            if len(courses) > 3:
                courses = courses[0:3]
            return render_template(
                "instructor/index.html",
                instructor=data["instructor"],
                instructor_id=data["instructor"]["id"],
                meta_info=self.contact_info,
                courses=courses,
                total_rate=sum(data["instructor"]["rates"]) /
                len(list(data["instructor"]["rates"])),
                images_url="http://127.0.0.1:3000/images"
            )
