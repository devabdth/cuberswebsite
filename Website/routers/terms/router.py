from flask import Flask, render_template, url_for, Response

terms: list = [
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },
        {
            'title': "Title",
            "paragraph": "Lorem Ispum",
        },

]

def terms_routes(app: Flask, auth_key: str, contact_information: dict):

    @app.route('/terms')
    @app.route('/conditions')
    @app.route('/contract')
    @app.route('/trust')
    def terms_index():
        return render_template('terms/index.html', terms= terms, meta_info= contact_information)
