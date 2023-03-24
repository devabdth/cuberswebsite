from dotenv import load_dotenv
from os import environ

class Config:
    def __init__(self):
        load_dotenv()

        self.port= environ["PORT"] if "PORT" in environ else 5000
        
        self.mode= environ["MODE"] if "MODE" in environ else 0
        self.is_debug_mode= self.mode == 0

        self.base_url= environ["BASE_URL"] if "BASE_URL" in environ else "http://127.0.0.1:{}".format(self.port)
        self.db_url= environ["DB_URL"] if "DB_URL" in environ else "mongodb://localhost/cubacademy"

        self.facebook= environ["FACEBOOK"] if "FACEBOOK" in environ else ""
        self.instragram= environ["INSTAGRAM"] if "INSTRAGRAM" in environ else ""
        self.facebook= environ["LINKEDIN"] if "LINKEDIN" in environ else ""

