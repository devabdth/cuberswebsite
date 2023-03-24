from flask import Flask, render_template, url_for, Response, send_file
import os

def tracking_routes(app: Flask, config):
    @app.route('/project/<id>/milestones')
    @app.route('/tracking/<id>/')
    def single_project_tracking_index(id: str):
        config.database_helper.projects.load()
        return render_template('tracking/index.html', header_desc=config.header_desc, meta_info=config.meta_info, url=config.url)

    @app.route('/tracking/')
    def tracking_project_form():
        return render_template('tracking/form.html', header_desc=config.header_desc, meta_info=config.meta_info, url=config.url)

