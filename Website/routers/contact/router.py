from flask import Flask, render_template, url_for, Response


def contact_routes(app: Flask, auth_key: str, contact_information: dict):

    @app.route('/contact')
    @app.route('/getInTouch')
    @app.route('/relation')
    @app.route('/findUs')
    def contact_index():
        return render_template('contact/index.html', meta_info= contact_information)
