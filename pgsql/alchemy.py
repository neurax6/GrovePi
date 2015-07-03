from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import Column,Integer,String,Float

app = Flask(__name__)
app.config[]
db = SQLAlchemy(app)


Class Pin(db.Model):
    id= Column()



