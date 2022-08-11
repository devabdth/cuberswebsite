from flask import Flask, send_file, send_from_directory
import os


class ImagesRouter:
    def __init__(self, app: Flask, config):
        self.app = app
        self.prefix = "images"

    def assign_routers(self):
        self.send_course_image_router()
        self.send_space_image_router()

    def send_course_image_router(self):
        @self.app.route("/courses/{}/<course_id>/".format(self.prefix), methods=["GET"])
        def send_course_image(course_id):
            return send_file("./images/courses/{}.jpg".format(course_id))

    def send_space_image_router(self):
        @self.app.route("/spaces/{}/<course_id>/".format(self.prefix), methods=["GET"])
        def send_space_image(course_id):
            return send_file("./images/spaces/{}.jpg".format(course_id))
