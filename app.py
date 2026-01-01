from flask import Flask
from flask_jwt_extended import JWTManager
from utils.db import init_db

init_db(app)
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'hiretrack-secret-key'
jwt = JWTManager(app)

@app.route('/')
def home():
    return {"message": "hiretrack is working!"}

if __name__ == '__main__':
    app.run(debug=True)