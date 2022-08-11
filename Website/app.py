from flask import Flask
from routers.home.router import home_routes
from routers.about.router import about_routes
from routers.terms.router  import terms_routes
from routers.services.router  import services_routes
from routers.contact.router  import contact_routes
from routers.portfolio.router import portfolio_routes
import os

def projects():
    from routers.portfolio.router import projects
    return list(projects.values())[:3]

config: dict = {
        "PORT": os.environ.get("PORT") or 3000,
        "DB_URL": os.environ.get("DB_URL") or "mongodb://localhost/cubers",
        "API_REQS_AUTH": os.environ.get("API_REQS_AUTH") or "123456789"
        }

contact_information: dict = {
    "phone": os.environ.get('PHONE') or '+201129164522',
    "address": os.environ.get('ADDRESS') or '20 Unknown st. | Unknown - Unknown',
    "map": os.environ.get('MAP') or "https://www.google.com/maps/place/30%C2%B001'13.3%22N+31%C2%B009'57.8%22E/@30.02036,31.1638643,746m/data=!3m2!1e3!4b1!4m6!3m5!1s0x0:0xc0d633d0d76b42ea!7e2!8m2!3d30.0203596!4d31.1660532",
}

home_content: dict = {
    
    "websitesCard": "Websites Card shot info",
    "applicationsCard": "Websites Card shot info",
    "desktopCard": "Websites Card shot info",
    "smmCard": "Websites Card shot info",
    "businessDevCard": "Websites Card shot info",
    "mediaProdCard": "Websites Card shot info",
    "terms_brief": "This is Terms Brief",
}

about_content: dict = {
    "story": '''
Cubers IO is an Egyptian company based in Cairo. We Cubers IO see that the biggest benefit is to take businesses to the next level which in the business can develop itself by our Software, Designs and Researches.///We’ve changed the way that our clients’ customers see the world by making services more easy as possible and we actually do this to satisfy our clients’ needs to expand vertically by making the cash flow more intelligent and horizontally  by making the virtual branch (Websites / Applications) available for the whole world.///Our Experience has taught us that to provide any solutions we need creativity and lots if inspired thinking. Our experienced professionals along with the ‘let-us-do-it’ attitude of the fresh talents is constantly pushing the horizons.''',
    "vision_pts": {
        "vision_pt_one": {
            "title": "I. We're your 'Brain'",
            "content": '''We aim to select the best way to your company and this is done
                        from a full “Case Study” that provides you the needed information about your competitors,
                        features, problems and solutions. <br>
                        Also we determine the technologies that will be used in next phases so finally we reach the most
                        perfect plan.''',
        },
    "vision_pt_two": {
            "title": "II. Experts for Masterpieces",
            "content": '''It is not easy to transform a simple idea to a unique software
                        project so we work practically on every single element selected in the plan from the scratch to
                        the deployed phase process.''',
        },
    "vision_pt_three": {
            "title": "III. We'll always got your back",
            "content": '''Your project is successfully published! <br>
                        After publishing your business, we still with you to test, make observations and improvements to
                        reach up-to-date standards and become ready to provide any support you need.''',
        },
    }
}

app: Flask = Flask(__name__)

home_routes(
        app= app,
        auth_key= config["API_REQS_AUTH"],
        contact_information= contact_information,
        content= home_content,
        projects= projects(),
)

about_routes(
        app= app, 
        auth_key= config["API_REQS_AUTH"],
        contact_information= contact_information,
        content= about_content,
)

terms_routes(
        app= app, 
        auth_key= config["API_REQS_AUTH"],
        contact_information= contact_information,
)

services_routes(
        app= app, 
        auth_key= config["API_REQS_AUTH"],
        contact_information= contact_information,
)

contact_routes(
        app= app, 
        auth_key= config["API_REQS_AUTH"],
        contact_information= contact_information,
)

portfolio_routes(
        app= app, 
        auth_key= config["API_REQS_AUTH"],
        contact_information= contact_information,
        url="http://127.0.0.1:3000",
)


if __name__ == '__main__':
    app.run(
            port= config["PORT"],
            debug= True,
            )
