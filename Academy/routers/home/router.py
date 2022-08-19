from flask import Flask, render_template


class HomeRouter:
    def __init__(
        self, app: Flask, config):
        self.app = app
        self.config = config
        self.contact_info: dict = {
            'facebook': config.facebook, 
            'instagram': config.instagram,
            'linkedin': config.linkedin,
            'email': config.email,
            'phone': config.phone,
            'address': config.address,
        }       
        self.emailing_model = config.emailing
        self.header_desc = config.header_desc
        self.database_helper = config.database_helper

    def assign_routers(self):
        @self.app.route("/", methods=["GET"])
        @self.app.route("/home/", methods=["GET"])
        @self.app.route("/index/", methods=["GET"])
        @self.app.route("/main/", methods=["GET"])
        @self.app.route("/landingPage/", methods=["GET"])
        def index():
            self.database_helper.courses.load()
            self.database_helper.instructors.load()
            courses = list(
                self.database_helper.courses.courses_data.values())[-4: -1]
            instructors: list = list(
                self.database_helper.instructors.instructors_data.values())[-4: -1]
            print(instructors)

            def calculate_rate(rates: list):
                if len(rates) == 0:
                    return 0

                return sum(rates) / len(rates)

            def modify_cats(cats: list):
                cats_: str = ""
                for cat in cats:
                    if cat == cats[-1]:
                        cats_ = "{} | {}".format(cats_, cat)
                        return
                    cats_ = "{} | {} |".format(cats_, cat)

                return cats_
                
            return render_template(
                "home/index.html",
                meta_info=self.contact_info,
                images_url="http://127.0.0.1:3000/images",
                header_desc=self.header_desc,
                courses=courses,
                instructors=instructors,
                calculate_rate=calculate_rate,
                modify_cats= modify_cats,
            )
