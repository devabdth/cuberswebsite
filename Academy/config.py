import os

# Database Helper
from db.helper import DatabaseHelper

# Email Model
from routers.operations.models.email import Emailing



class Config:
    def __init__(self):
        self.debug_mode_token = "DEBUG"
        self.production_mode_token = "PROD"

        self.port = os.environ.get("PORT") or 3000
        self.mode = os.environ.get("MODE") or self.debug_mode_token
        self.auth_key = os.environ.get("AUTH_KEY") or "1234567890"
        self.db_url = os.environ.get(
            "DB_URL") or "mongodb://localhost/cubersAcademy"

        self.email_model_email = os.environ.get(
            "EMAIL_MODEL_EMAIL") or "academy@cubersio.com"
        self.email_model_access_key = os.environ.get(
            "EMAIL_MODEL_ACCESS_KEY") or "Cubers@passwords:AcademyEmailPassword:25072001"
        self.header_desc = os.environ.get("HEADER_DESC") or """Cubers Academy is an Egyptian Company that is sub-branded from Cubers IO. We Cubers Academy, seeking to prepare youth aged from 17 ~ 27 years for the labor market by giving them: One-Day Workshops, Two-Days Workshops, Three-Days Workshops, Bootcamps, Courses, Diplomas. After our trainees finishes the programs they’ve chosen we take the highest ranked trainee and give internship in our main brand: Cubers IO."""
        self.header_keywords= os.environ.get("HEADER_KEYWORDS") or ""

        self.facebook= os.environ.get("FACEBOOK") or "https://facebook.com/cuberacd"
        self.linkedin= os.environ.get("LINKEDIN") or "https://linkedin.com/company/cubersacd"
        self.instagram= os.environ.get("INSTAGTAM") or "https://instagram.com/cubersacd"
        self.email= os.environ.get("CONTACT_EMAIL") or "academy@cubersio.com"
        self.phone= os.environ.get("CONTACT_PHONE") or "+20 112 916 4522"
        self.address= os.environ.get("CONTACT_ADDRESS") or ""

        # Initalize Emailing Operation Model
        self.emailing: Emailing = Emailing(
            email=self.email_model_email, 
            access_key=self.email_model_access_key
        )

        # Initialize Database Helper
        self.database_helper: DatabaseHelper = DatabaseHelper()


    @property
    def is_debug_mode(self) -> bool:
        return self.mode == self.debug_mode_token
