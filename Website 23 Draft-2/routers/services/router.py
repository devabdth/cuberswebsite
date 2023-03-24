from flask import Flask, render_template, url_for, Response, send_file
import os


def services_routes(app: Flask, config):

    @app.route('/services')
    @app.route('/technologies')
    def services_index():
        return render_template(
            'services/index.html',
            services=config.services_content.ALL.value,
            meta_info=config.meta_info,
            header_desc=config.header_desc,
            keywords=config.keywords
        )

    @app.route('/services/image/<image>')
    def services_bgs(image: str):
        path_: str = os.path.join(os.path.dirname(
            __file__), 'assets\\{}'.format(image))
        print((path_))
        if not os.path.exists(path_):
            return app.response_class(status=404)
        return send_file(path_)

    @app.route('/services/icon/<icon>')
    def services_icons(icon: str):
        path_: str = os.path.join(os.path.dirname(
            __file__), 'icons\\{}'.format(icons))
        print(os.path.exists(path_))
        if not os.path.exists(path_):
            return app.response_class(status=404)
        return send_file(path_)
