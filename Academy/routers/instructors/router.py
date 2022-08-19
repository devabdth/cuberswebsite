from flask import Flask, render_template, request


class InstructorsRouter:
    def __init__(self, app: Flask, config):
        self.app = app
        self.prefix = "instructors"
        self.contact_info: dict = {
            'facebook': config.facebook, 
            'instagram': config.instagram,
            'linkedin': config.linkedin,
            'email': config.email,
            'phone': config.phone,
            'address': config.address,
        }       
        self.database_helper= config.database_helper
        self.emailing_model = config.emailing
        self.header_desc= config.header_desc

    def assign_routers(self):
        self.assign_all_instructors()

    def search(self, instructor: str):
        self.database_helper.instructors.load()
        instructors = self.database_helper.instructors.get_all_instructors()

        instructors_ = []
        for instructor__ in list(instructors):
            if (instructor__["name"]).lower().find(instructor.lower()) != -1:
                instructors_.append(dict(instructor__))
        return instructors_

    def assign_all_instructors(self):

        @self.app.route("/{}/".format(self.prefix), methods=["GET"])
        def instructors():
            self.database_helper.instructors.load()
            params = dict(request.values)

            if "instructor" in params.keys():
                instructor_token = params["instructor"]
            else:
                instructor_token = ""

            instructorss = list(self.database_helper.courses.get_all_courses())
            instructors = self.search(
                instructor=instructor_token,
            )
            def modify_cats(cats: list):
                cats_: str = ""
                for cat in cats:
                    if cat == cats[-1]:
                        cats_ = "{} | {}".format(cats_, cat)
                        return
                    cats_ = "{} | {} |".format(cats_, cat)

                return cats_
                

            def calculate_rate(rates: list):
                if len(rates) == 0:
                    return 0

                return sum(rates) / len(rates)

            return render_template(
                "instructors/index.html",
                meta_info=self.contact_info,
                instructor=instructor_token,
                instructors= instructors,
                calculate_rate=calculate_rate,
                modify_cats= modify_cats,
                images_url="http://127.0.0.1:3000/images", 
                header_desc= self.header_desc

            )
