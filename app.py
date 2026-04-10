from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setup Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
db = SQLAlchemy(app)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)