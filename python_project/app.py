##########################################
################# Import Libraries #######
########################################## 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)

from routes import *



if __name__ == '__main__':
    app.run(debug=True)