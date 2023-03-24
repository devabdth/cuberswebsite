from content.about_content import AboutContent
from content.home_content import HomeContent
from content.terms_content import TermsContent
from content.services_content import ServicesContent
import os

from db import DatabaseHelper


class Config:

    def __init__(self):
        self.home_content = HomeContent
        self.about_content = AboutContent
        self.terms_content = TermsContent
        self.services_content = ServicesContent

        self.debug_mode_token = "DEBUG"
        self.production_mode_token = "PROD"

        self.port = os.environ.get("PORT") or 3000
        self.mode = os.environ.get("MODE") or self.debug_mode_token
        self.auth_key = os.environ.get("AUTH_KEY") or "1234567890"
        self.db_url = os.environ.get(
            "DB_URL") or "mongodb://localhost/cubersWebsite"

        self.email_model_email = os.environ.get(
            "EMAIL_MODEL_EMAIL") or "info@cubersio.com"
        self.email_model_access_key = os.environ.get(
            "EMAIL_MODEL_ACCESS_KEY") or "Cubers@passwords:WebsiteEmailPassword:25072001"
        self.header_desc = os.environ.get("HEADER_DESC") or """Cubers Website is an Egyptian Company that is sub-branded from Cubers IO. We Cubers Website, seeking to prepare youth aged from 17 ~ 27 years for the labor market by giving them: One-Day Workshops, Two-Days Workshops, Three-Days Workshops, Bootcamps, Courses, Diplomas. After our trainees finishes the programs they’ve chosen we take the highest ranked trainee and give internship in our main brand: Cubers IO."""
        self.keywords = os.environ.get("KEYWORDS") or ""
        self.header_keywords = os.environ.get("HEADER_KEYWORDS") or ""

        self.facebook = os.environ.get(
            "FACEBOOK") or "https://facebook.com/cubersio"
        self.linkedin = os.environ.get(
            "LINKEDIN") or "https://linkedin.com/company/cubersio"
        self.instagram = os.environ.get(
            "INSTAGTAM") or "https://instagram.com/cubersio"
        self.email = os.environ.get("CONTACT_EMAIL") or "info@cubersio.com"
        self.phone = os.environ.get("CONTACT_PHONE") or "+20 112 916 4522"
        self.address = os.environ.get("CONTACT_ADDRESS") or ""

        self.url = os.environ.get(
            "URL") or "www.cubersio.com"

        # Initalize Emailing Operation Model
        # self.emailing: Emailing = Emailing(
        #     email=self.email_model_email,
        #     access_key=self.email_model_access_key
        # )

        # Initialize Database Helper
        self.database_helper: DatabaseHelper = DatabaseHelper()

    @property
    def is_debug_mode(self) -> bool:
        return self.mode == self.debug_mode_token

    @property
    def meta_info(self) -> dict:
        return{
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "facebook": self.facebook,
            "linkedin": self.linkedin,
            "instagram": self.instagram,
        }
