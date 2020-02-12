import os
from app import app
from app.controllers import MainController, TrainController, GuessController, ApiController

app.config['SECRET_KEY'] = os.urandom(32)

if __name__ == "__main__":
    app.run()