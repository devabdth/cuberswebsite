from flask import Flask, render_template, url_for, Response, send_file
import os

services: list = [
    {
        'title': "Social Media Marketing",
        'paragraph': "Lorem Ispum",
        'image': "entry.jpg",
        'technologies': [
            {
                'title': "Photoshop",
                'icon': "entry.jpg",
            }
        ],
    },
    {
        'title': "Social Media Marketing",
        'paragraph': "Lorem Ispum",
        'image': "entry.jpg",
        'technologies': [
            {
                'title': "Photoshop",
                'icon': "entry.jpg",
            }
        ],
    },
    {
        'title': "Social Media Marketing",
        'paragraph': "Lorem Ispum",
        'image': "entry.jpg",
        'technologies': [
            {
                'title': "Photoshop",
                'icon': "entry.jpg",
            }
        ],
    },
    {
        'title': "Social Media Marketing",
        'paragraph': "Lorem Ispum",
        'image': "entry.jpg",
        'technologies': [
            {
                'title': "Photoshop",
                'icon': "entry.jpg",
            }
        ],
    },



]

def services_routes(app: Flask, auth_key: str, contact_information: dict):

    @app.route('/services')
    @app.route('/technologies')
    def services_index():
        return render_template('services/index.html', services= services, meta_info= contact_information)

    @app.route('/services/image/<image>')
    def services_bgs(image: str):
        path_: str = os.path.join(os.path.dirname(__file__), 'assets\\{}'.format(image))
        print(os.path.exists(path_))
        if not os.path.exists(path_):
            return app.response_class(status=404)
        return send_file(path_)

    @app.route('/services/icon/<icon>')
    def services_icons(icon: str):
        path_: str = os.path.join(os.path.dirname(__file__), 'icons\\{}'.format(icons))
        print(os.path.exists(path_))
        if not os.path.exists(path_):
            return app.response_class(status=404)
        return send_file(path_)
