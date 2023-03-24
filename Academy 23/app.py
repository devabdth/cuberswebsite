from flask import Flask
from config import Config
from setup import init_app as setup


app: Flask= Flask("CUBACADEMY")
setup(app)


app.run(
    port= Config().port,
    debug= Config().is_debug_mode,
)
