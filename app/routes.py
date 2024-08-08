from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from app import app, db
from app.models import Recipe
from sqlalchemy.sql import func
from sqlalchemy.exc import OperationalError, PendingRollbackError

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def get_tags():
    all_tags = db.session.query(Recipe.tags).all()
    tags_list = []
    
    for tags in all_tags:
        if tags[0]:
            split_tags = tags[0].split()
            tags_list.extend(split_tags)
    
    unique_tags = list(set(tags_list))
    return unique_tags


@app.route('/')
def index():
    recipe = Recipe.query.order_by(func.random()).first()
    cuisines = db.session.query(Recipe.cuisine).distinct().all()
    cuisines = [cuisine[0] for cuisine in cuisines if cuisine[0]]
    tags = get_tags()
    return render_template('index.html', recipe=recipe, cuisines=cuisines, tags=tags)

@app.route('/category/<string:cuisine>')
def category(cuisine):
    recipes = Recipe.query.filter_by(cuisine=cuisine).all()
    cuisines = db.session.query(Recipe.cuisine).distinct().all()
    cuisines = [cuisine[0] for cuisine in cuisines if cuisine[0]]
    tags = get_tags()
    return render_template('category.html', category=cuisine, recipes=recipes, cuisines=cuisines, tags=tags)

@app.route('/recipe/<int:recipe_id>')
def recipe_detail(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    cuisines = db.session.query(Recipe.cuisine).distinct().all()
    cuisines = [cuisine[0] for cuisine in cuisines if cuisine[0]]
    tags = get_tags()
    return render_template('recipe_detail.html', recipe=recipe, cuisines=cuisines, tags=tags)

@app.route('/search')
def search_results():
    query = request.args.get('q')
    if query:
        recipes = Recipe.query.filter(
            (Recipe.title.ilike(f'%{query}%')) |
            (Recipe.ingredients.ilike(f'%{query}%')) |
            (Recipe.tags.ilike(f'%{query}%')) |
            (Recipe.cuisine.ilike(f'%{query}%'))
        ).all()
    else:
        recipes = []

    cuisines = db.session.query(Recipe.cuisine).distinct().all()
    cuisines = [cuisine[0] for cuisine in cuisines if cuisine[0]]
    tags = get_tags()
    return render_template('search_results.html', recipes=recipes, cuisines=cuisines, tags=tags)

@app.route('/add_recipe', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        method = request.form['method']
        tags = request.form['tags'].split()
        cuisine = request.form['cuisine']

        if 'image' not in request.files:
            flash('No image file part')
            return redirect(request.url)
        
        file = request.files['image']
        if file.filename == '':
            flash('No selected image file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            temp_file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            os.makedirs(os.path.dirname(temp_file_path), exist_ok=True)
            file.save(temp_file_path)

            new_recipe = Recipe(
                title=title,
                ingredients=ingredients,
                image_filename='temp.jpg',
                method=method,
                tags=', '.join(tags),
                cuisine=cuisine
            )
            db.session.add(new_recipe)
            try:
                db.session.commit()
            except (OperationalError, PendingRollbackError) as e:
                db.session.rollback()
                flash(f'An error occurred while adding the recipe: {str(e)}')
                print(f"Exception: {e}")
                return redirect(request.url)

            recipe_id = new_recipe.id
            new_filename = f"{recipe_id}.jpg"
            new_file_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)

            os.rename(temp_file_path, new_file_path)
            new_recipe.image_filename = new_filename
            try:
                db.session.commit()
            except (OperationalError, PendingRollbackError) as e:
                db.session.rollback()
                flash(f'An error occurred while updating the image filename: {str(e)}')
                print(f"Exception: {e}")
                return redirect(request.url)

            flash('Recipe added successfully!')
            return redirect(url_for('index'))

    tags = get_tags()
    return render_template('add_recipe.html', tags=tags)
