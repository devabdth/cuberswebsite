from flask import Flask, render_template, url_for, Response


def home_routes(app: Flask, auth_key: str, contact_information: dict, content: dict, projects: dict):

    @app.route('/')
    @app.route('/home')
    @app.route('/index')
    def index():
        return render_template('home/index.html', meta_info= contact_information, content= content, projects= projects)
