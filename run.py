import os
from app import app
from app.controllers import MainController

app.config['SECRET_KEY'] = os.urandom(32)

print("hellal")

if __name__ == "__main__":
    app.run()