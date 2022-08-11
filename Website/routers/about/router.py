from flask import Flask, render_template, url_for, Response


def about_routes(app: Flask, auth_key: str, contact_information: dict, content: dict):

    @app.route('/about')
    @app.route('/whoWeAre')
    @app.route('/brief')
    def about_index():
        return render_template('about/index.html', meta_info= contact_information, content= content)
