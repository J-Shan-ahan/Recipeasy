from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(100), nullable=False)
    method = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(100), nullable=False)
    cuisine = db.Column(db.String(100))  