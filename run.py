import os
from app import app
from flask_wtf.csrf import CSRFProtect
from app.controllers import MainController, TrainController, GuessController, ApiController

app.config['SECRET_KEY'] = os.urandom(32)
csrf = CSRFProtect(app)

if __name__ == "__main__":
    app.run()