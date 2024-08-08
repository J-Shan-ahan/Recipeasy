from app import app, db
from app.models import Recipe
import os

def add_recipe(title, ingredients, image_filename, method, tags, cuisine):
    with app.app_context():
        new_recipe = Recipe(
            title=title,
            ingredients=ingredients,
            image_filename=image_filename,
            method=method,
            tags=tags,
            cuisine=cuisine
        )
        db.session.add(new_recipe)
        db.session.commit()
        print("Recipe added successfully!")

if __name__ == "__main__":

    add_recipe(
        title="Spaghetti Carbonara",
        ingredients="Spaghetti, Eggs, Parmesan cheese, Pancetta, Garlic, Black pepper",
        image_filename="carbonara.jpg",
        method="1. Cook spaghetti. 2. Cook pancetta. 3. Mix eggs and cheese. 4. Combine all ingredients.",
        tags="Italian, Pasta, Quick"
    )
