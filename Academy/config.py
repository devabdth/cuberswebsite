import os


class Config:
    def __init__(self):
        self.debug_mode_token = "DEBUG"
        self.production_mode_token = "PROD"

        self.port = os.environ.get("PORT") or 3000
        self.mode = os.environ.get("MODE") or self.debug_mode_token
        self.auth_key = os.environ.get("AUTH_KEY") or "1234567890"
        self.db_url = os.environ.get(
            "DB_URL") or "mongodb://localhost/cubersAcademy"

    def is_debug_mode(self) -> bool:
        return self.mode == self.debug_mode_token
