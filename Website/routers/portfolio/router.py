from flask import Flask, render_template, url_for, Response, send_file
import os


def portfolio_routes(app: Flask, config):

    @ app.route('/projects/')
    @ app.route('/works/')
    @ app.route('/portfolio/')
    @ app.route('/gallery/')
    def projects_index():
        config.database_helper.projects.load()
        return render_template('portfolio/index.html', header_desc=config.header_desc, projects=config.database_helper.projects.data, meta_info=config.meta_info, url="../")

    @ app.route('/project/<id>/')
    @ app.route('/portfolio/projectId=<id>/')
    @ app.route('/portfolio/<id>/')
    @ app.route('/works/<id>/')
    @ app.route('/gallery/<id>/')
    def single_project_index(id: str):
        config.database_helper.projects.load()
        return render_template('portfolio/single_project/index.html', header_desc=config.header_desc, project=config.database_helper.projects.get_project_by_id(id), meta_info=config.meta_info, url="https://cubersio.com")

    @ app.route('/projects/covers/<id>/')
    def project_cover(id: str):
        print(id)
        path_: str = os.path.join(os.path.dirname(
            __file__), './covers/{}.png'.format(id))
        print(os.path.exists(path_))
        if not os.path.exists(path_):
            return app.response_class(status=404)
        return send_file(path_)

    @ app.route('/projects/assets/<file>/')
    def project_asset(file: str):
        print(id)
        path_: str = os.path.join(os.path.dirname(
            __file__), './assets/{}'.format(file))
        print(os.path.exists(path_))
        if not os.path.exists(path_):
            return app.response_class(status=404)
        return send_file(path_)
