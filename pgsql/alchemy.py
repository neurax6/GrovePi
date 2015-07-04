from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import Column,Integer,String,Float

app = Flask(__name__)
app.config[]
db = SQLAlchemy(app)


Class Pin(db.Model):
    id = Column(InterruptedError,primary_key=True)
    temp = Column(Float,unique=False)
    hum = Column(Float,unique=False)
    date = Column(String,unique=False)

db.create_all()

@app.route('/')




