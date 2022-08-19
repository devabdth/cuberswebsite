from flask import Flask, render_template, url_for, request
import os
import json


class FormRouter:
    def __init__(self, app: Flask, config):
        self.app = app
        self.prefix = "forms"
        self.contact_info: dict = {
            'facebook': config.facebook, 
            'instagram': config.instagram,
            'linkedin': config.linkedin,
            'email': config.email,
            'phone': config.phone,
            'address': config.address,
        }       
        self.emailing_model = config.emailing
        self.database_helper = config.database_helper
        self.header_desc = config.header_desc
       
    def assign_routers(self):
        self.assign_application()
        self.assign_post_application()
        self.assign_api_router()
        self.assign_instructors_form()


    def assign_instructors_form(self):
        @self.app.route("/instructors/form/", methods=["GET"])
        @self.app.route("/join/", methods=["GET"])
        def instructors_form():
            return render_template(
                'instructorsForm/index.html',
                header_desc= self.header_desc,
                meta_info= self.contact_info
            )


    def assign_api_router(self):
        @self.app.route("/{}/fetch/".format(self.prefix), methods=["GET"])
        def api():
            self.database_helper.forms.load()
            params = dict(request.values)

            try:
                course_token: int = int(params["courseId"])
                forms_: list= []
                for form in list(self.database_helper.forms.forms_data.values()):
                    if form["courseId"] == course_token:
                        forms_.append(dict(form))


                return self.app.response_class(
                    status= 200,
                    response= json.dumps({"forms": forms_})
                )

            except: 
                return self.app.response_class(
                    status= 200,
                    response= json.dumps({"forms": list(self.database_helper.forms.forms_data.values())})
                )

               

    def assign_post_application(self):
        @self.app.route("/{}/post/".format(self.prefix), methods=["POST"])
        def create_application():
            try:
                data = request.data
                payload = json.loads(data)

                self.database_helper.forms.load()
                reservation_id = self.database_helper.forms.create_form(
                    payload)
                if reservation_id is None:
                    return self.app.response_class(status=403, response=json.dumps({"msg": "Duplicated Form"}))

                mail_params = {'main_concept': reservation_id}
                self.emailing_model.send_styled_email(subject='Thanks for chosing Cubers Academy', recievers=[
                                                      payload["email"]], params=mail_params)

                return self.app.response_class(status=201)
            except Exception as e:
                print("Creating Form: {}".format(e))
                return self.app.response_class(status=500, response=json.dumps({"msg": "This is Error Msg"}))

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
                images_url="http://127.0.0.1:3000/images", 
                header_desc= self.header_desc,
            )
