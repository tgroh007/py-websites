from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1QAZ@wsx3EDC$rfv'

    
    return app
