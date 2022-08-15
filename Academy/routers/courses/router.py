from flask import Flask, render_template, request
import pandas as pd


class CoursesRouter:
    def __init__(self, app: Flask, config, database_helper, contact_info: dict = {}):
        self.app = app
        self.prefix = "courses"
        self.database_helper = database_helper
        self.contact_info = contact_info

    def assign_routers(self):
        self.assign_all_courses()

    def search(self, course: str, instructor: str):
        self.database_helper.courses.load()
        courses = self.database_helper.courses.get_all_courses()

        courses_ = []
        for course__ in list(courses):
            if (course__["name"]).lower().find(course.lower()) != -1 and course__["instructor"].lower().find(instructor.lower()) != -1:
                courses_.append(dict(course__))
        return courses_

    def assign_all_courses(self):

        @self.app.route("/{}/".format(self.prefix), methods=["GET"])
        def course():
            self.database_helper.courses.load()
            params = dict(request.values)

            if "course" in params.keys():
                course_token = params["course"]
            else:
                course_token = ""

            if "instructor" in params.keys():
                instructor_token = params["instructor"]
            else:
                instructor_token = ""


            courses = list(self.database_helper.courses.get_all_courses())
            courses = [courses[0] for _ in range(0, 31)]
            courses = self.search(
                course=course_token,
                instructor=instructor_token,
            )
            print(courses)

            def calculate_rate(rates: list):
                if len(rates) == 0:
                    return 0

                return sum(rates) / len(rates)
            return render_template(
                "courses/index.html",
                meta_info=self.contact_info,
                course=course_token,
                instructor=instructor_token,
                courses=courses,
                calculate_rate=calculate_rate,
                images_url="http://127.0.0.1:3000/images"

            )
