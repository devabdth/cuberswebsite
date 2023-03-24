from enum import Enum as Enum


class AboutContent(Enum):
    STORY: str = '''Cubers IO is an Egyptian company based in Cairo. We Cubers IO see that the biggest benefit is to take businesses to the next level which in the business can develop itself by our Software, Designs and Researches.\nWe’ve changed the way that our clients’ customers see the world by making services more easy as possible and we actually do this to satisfy our clients’ needs to expand vertically by making the cash flow more intelligent and horizontally  by making the virtual branch (Websites / Applications) available for the whole world.\n\n\nOur Experience has taught us that to provide any solutions we need creativity and lots if inspired thinking. Our experienced professionals along with the ‘let-us-do-it’ attitude of the fresh talents is constantly pushing the horizons.'''
    VISION: dict = {
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
                        reach up-to-date standards and become ready to provide any support you need.'''
        }
    }
