import os
from app import app
from app.controllers import MainController, TrainController, GuessController, ApiController

if __name__ == "__main__":
    app.run()