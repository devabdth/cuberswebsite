from flask import Flask, render_template, url_for, Response


def about_routes(app: Flask, config):

    @app.route('/about/')
    @app.route('/whoWeAre/')
    @app.route('/brief/')
    def about_index():
        return render_template(
            'about/index.html',
            meta_info=config.meta_info,
            content={
                'story': config.about_content.STORY.value,
                'vision_pts': config.about_content.VISION.value,
            }
        )
