from app import app, db
from app.models import Recipe

def add_recipe(title, ingredients, image_filename, method, tags, cuisine):
    with app.app_context():
        new_recipe = Recipe(
            title=title,
            ingredients=ingredients,
            image_filename=image_filename,
            method=method,
            tags=tags,
            cuisine=cuisine  # Include cuisine
        )

        db.session.add(new_recipe)
        db.session.commit()
        print(f"Recipe '{title}' added successfully!")

def populate_db():
    recipes = [
        {
            "title": "Spaghetti Carbonara",
            "ingredients": "Spaghetti, Eggs, Parmesan cheese, Pancetta, Garlic, Black pepper",
            "image_filename": "1.jpg",
            "method": "1. Cook spaghetti. 2. Cook pancetta. 3. Mix eggs and cheese. 4. Combine all ingredients.",
            "tags": "Italian Pasta Quick",
            "cuisine": "Italian"  # Add cuisine
        },
        {
            "title": "Margherita Pizza",
            "ingredients": "Pizza dough, Tomato sauce, Mozzarella cheese, Basil, Olive oil",
            "image_filename": "2.jpg",
            "method": "1. Spread sauce on dough. 2. Add cheese and basil. 3. Bake in oven.",
            "tags": "Italian Pizza Vegetarian",
            "cuisine": "Italian"  # Add cuisine
        },
        {
            "title": "Chicken Alfredo",
            "ingredients": "Fettuccine, Chicken breast, Alfredo sauce, Parmesan cheese, Garlic",
            "image_filename": "3.jpg",
            "method": "1. Cook fettuccine. 2. Cook chicken. 3. Combine with Alfredo sauce.",
            "tags": "Italian Chicken Creamy",
            "cuisine": "Italian"  # Add cuisine
        },
        {
            "title": "Chocolate Cake",
            "ingredients": "Flour, Cocoa powder, Sugar, Eggs, Butter, Baking powder",
            "image_filename": "4.jpg",
            "method": "1. Mix dry ingredients. 2. Add wet ingredients. 3. Bake in oven.",
            "tags": "Dessert Chocolate Sweet",
            "cuisine": "Dessert"  # Add cuisine
        },
        {
            "title": "Caesar Salad",
            "ingredients": "Romaine lettuce, Caesar dressing, Croutons, Parmesan cheese",
            "image_filename": "5.jpg",
            "method": "1. Toss lettuce with dressing. 2. Add croutons and cheese.",
            "tags": "Salad Vegetarian Quick",
            "cuisine": "Salad"  # Add cuisine
        },
        {
            "title": "Beef Tacos",
            "ingredients": "Ground beef, Taco seasoning, Tortillas, Lettuce, Cheese, Salsa",
            "image_filename": "6.jpg",
            "method": "1. Cook beef with seasoning. 2. Assemble tacos with toppings.",
            "tags": "Mexican Beef Quick",
            "cuisine": "Mexican"  # Add cuisine
        },
        {
            "title": "Tomato Soup",
            "ingredients": "Tomatoes, Onion, Garlic, Vegetable broth, Cream",
            "image_filename": "7.jpg",
            "method": "1. Cook tomatoes and onions. 2. Blend with broth and cream.",
            "tags": "Soup Vegetarian Comfort",
            "cuisine": "Soup"  # Add cuisine
        },
        {
            "title": "Chicken Stir-Fry",
            "ingredients": "Chicken breast, Mixed vegetables, Soy sauce, Garlic, Ginger",
            "image_filename": "8.jpg",
            "method": "1. Stir-fry chicken and vegetables. 2. Add sauce and cook.",
            "tags": "Asian Chicken Quick",
            "cuisine": "Asian"  # Add cuisine
        },
        {
            "title": "Greek Salad",
            "ingredients": "Cucumber, Tomatoes, Feta cheese, Olives, Red onion, Olive oil",
            "image_filename": "9.jpg",
            "method": "1. Combine all ingredients in a bowl.",
            "tags": "Salad Vegetarian Mediterranean",
            "cuisine": "Mediterranean"  # Add cuisine
        },
        {
            "title": "Berry Smoothie",
            "ingredients": "Mixed berries, Yogurt, Honey, Ice",
            "image_filename": "10.jpg",
            "method": "1. Blend all ingredients until smooth.",
            "tags": "Drink Smoothie Healthy",
            "cuisine": "Drink"  # Add cuisine
        }
    ]

    with app.app_context():
        for recipe in recipes:
            add_recipe(
                title=recipe["title"],
                ingredients=recipe["ingredients"],
                image_filename=recipe["image_filename"],
                method=recipe["method"],
                tags=recipe["tags"],
                cuisine=recipe["cuisine"]  
            )

if __name__ == "__main__":
    populate_db()
