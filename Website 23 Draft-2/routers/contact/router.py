from flask import Flask, render_template, url_for, Response


def contact_routes(app: Flask, config):

    @app.route('/contact/')
    @app.route('/getInTouch/')
    @app.route('/relation/')
    @app.route('/findUs/')
    def contact_index():
        return render_template('contact/index.html', meta_info=config.meta_info)
