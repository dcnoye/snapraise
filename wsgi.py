#boilerplate for development, can be jettisoned
import sys
import site

from app import create_app

app = create_app({})

if __name__ == "__main__":
    app.run()
