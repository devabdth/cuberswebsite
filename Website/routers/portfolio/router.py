from flask import Flask, render_template, url_for, Response, send_file
import os

projects: dict = {
        "0": {
            'title': "Title",
            'type': "Website",
            "short_brief": "Short Brief",
            "paragraph": "Lorem Ispum",
            "id": "0",
            "content": [
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },

                {
                    "cover": None,
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },

            ],
 
        },
        "1": {
            'title': "Title",
            'type': "Website",
            "short_brief": "Short Brief",
            "paragraph": "Lorem Ispum",
            "id": "1",
            "content": [
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },

                {
                    "cover": None,
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
            ],
    
        },
        "2": {
            'title': "Title",
            'type': "Website",
            "short_brief": "Short Brief",
            "paragraph": "Lorem Ispum",
            "id": "2",
            "content": [
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },

                {
                    "cover": None,
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
            ],
        },
        "3": {
            'title': "Title",
            'type': "Website",
            "short_brief": "Short Brief",
            "paragraph": "Lorem Ispum",
            "id": "3",
            "content": [
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },

                {
                    "cover": None,
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
            ],
        },
        "4": {
            'title': "Title",
            'type': "Website",
            "short_brief": "Short Brief",
            "paragraph": "Lorem Ispum",
            "id": "4",
            "content": [
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },

                {
                    "cover": None,
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
            ],
        },
        "5": {
            'title': "Title",
            'type': "Website",
            "short_brief": "Short Brief",
            "paragraph": "Lorem Ispum",
            "id": "5",
            "content": [
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },

                {
                    "cover": None,
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
                {
                    "cover": "0.png",
                    "text": '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin at pulvinar enim. Phasellus tempor non purus ut faucibus. In et magna vel arcu efficitur euismod eu blandit velit. Quisque id mi eros. Maecenas eget nisl iaculis nulla mollis aliquet. Suspendisse consectetur rutrum turpis. Sed cursus eleifend lorem commodo consequat. Nullam convallis euismod massa, vel congue augue faucibus at. Nullam felis ante, convallis sed libero at, scelerisque gravida felis. Vestibulum accumsan elit in aliquet tempor. Praesent tempor scelerisque quam eget finibus. Aliquam quis sem metus. Cras non nunc aliquet, vulputate nisi in, semper nibh.'''

                },
            ],
        },

}

def portfolio_routes(app: Flask, auth_key: str, contact_information: dict, url: str):

    @app.route('/projects')
    @app.route('/works')
    @app.route('/portfolio')
    @app.route('/gallery')
    def projects_index():
        return render_template('portfolio/index.html', projects= projects, meta_info= contact_information, url=url)

    @app.route('/project/<id>')
    @app.route('/portfolio/projectId=<id>')
    @app.route('/portfolio/<id>')
    @app.route('/works/<id>')
    @app.route('/gallery/<id>')
    def single_project_index(id: str):
        return render_template('portfolio/single_project/index.html', project=projects[id], meta_info= contact_information, url= url)

    @app.route('/projects/covers/<id>')
    def project_cover(id: str):
      print(id)
      path_: str = os.path.join(os.path.dirname(__file__), 'covers\\{}.png'.format(id))
      print(os.path.exists(path_))
      if not os.path.exists(path_):
        return app.response_class(status=404)
      return send_file(path_)
  
    @app.route('/projects/assets/<file>')
    def project_asset(file: str):
      print(id)
      path_: str = os.path.join(os.path.dirname(__file__), 'assets\\{}'.format(file))
      print(os.path.exists(path_))
      if not os.path.exists(path_):
        return app.response_class(status=404)
      return send_file(path_)
