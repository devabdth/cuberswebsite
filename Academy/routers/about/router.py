from flask import Flask, render_template

class AboutRouter:
    def __init__(self, app: Flask, config):
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
        @self.app.route('/about/', methods=["GET"])
        @self.app.route('/whoWeAre/', methods=["GET"])
        @self.app.route('/profile/', methods=["GET"])
        @self.app.route('/brief/', methods=["GET"])
        def about():
            return render_template(
                'about/index.html',
                meta_info= self.contact_info,
                header_desc= self.header_desc
            )

