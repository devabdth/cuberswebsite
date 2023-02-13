from flask import Flask, render_template, url_for, Response


def terms_routes(app: Flask, config):

    @app.route('/terms/')
    @app.route('/conditions/')
    @app.route('/contract/')
    @app.route('/trust/')
    def terms_index():
        return render_template('terms/index.html', terms=config.terms_content.ALL_TERMS.value, meta_info=config.meta_info)
