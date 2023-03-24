from flask import Flask, render_template, url_for, Response


def home_routes(app: Flask, config):

    @app.route('/')
    @app.route('/home/')
    @app.route('/index/')
    def index():
        config.database_helper.projects.load()
        return render_template(
            'home/index.html',
            meta_info=config.meta_info,
            content={
                "websitesCard": config.home_content.WEBSITES_CARD.value,
                "applicationsCard": config.home_content.APPLICATIONS_CARD.value,
                "desktopCard": config.home_content.DESKTOP_CARD.value,
                "smmCard": config.home_content.SMM_CARD.value,
                "businessDevCard": config.home_content.BUSSINESS_DEV_CARD.value,
                "mediaProdCard": config.home_content.MEDIA_PROD_CARD.value,
                "terms_brief": config.home_content.TRUST_BETWEEN_US.value,
            },
            projects=(list(config.database_helper.projects.data.values()))[:3],
        )
