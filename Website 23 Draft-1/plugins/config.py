from os import environ

from dotenv import load_dotenv as env

class Config:
    def __init__(self):
        env()
        # App Information
        self.port = environ['PORT'] if 'PORT' in environ else 1010
        self.app_name = environ['APP_NAME'] if 'APP_NAME' in environ else "App_NAME"
        self.mode = environ['MODE'] if 'MODE' in environ else "DEBUG"
        self.host = environ['HOST'] if 'HOST' in environ else "localhost"
        self.auth_key = environ['AUTH_KEY'] if 'AUTH_KEY' in environ else ""
        self.base_url = environ["BASE_URL"] if "BASE_URL" in environ else "http://127.0.0.1:1010"
        self.copyright_msg = environ["COPYRIGHT"] if "COPYRIGHT" in environ else "Copyright"

        # Website Information
        self.header_desc = environ['HEADER_DESC'] if 'HEADER_DESC' in environ else ""
        self.header_keywords = environ['HEADER_KEYWORDS'] if 'HEADER_KEYWORDS' in environ else ""
        self.instagram_link = environ['INSTAGRAM'] if 'INSTAGRAM' in environ else None
        self.facebook_link = environ['FACEBOOK'] if 'FACEBOOK' in environ else None
        self.linkedin_link = environ['LINKEDIN'] if 'LINKEDIN' in environ else None
        self.tiktok_link = environ['TIKTOK'] if 'TIKTOK' in environ else None
        self.twitter_link = environ['TWITTER'] if 'TWITTER' in environ else None
        self.youtube_link = environ['YOUTEBE'] if 'YOUTEBE' in environ else None
