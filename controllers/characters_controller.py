from flask import render_template, request, redirect
from models.characters import all_characters, get_character, create_character, update_character, delete_character
from services.sessions_info import current_user

def index():
    characters = all_characters()
    return render_template('characters/index.html', characters=characters, current_user=current_user)

def new():
    return render_template('characters/new.html')
    
def create():
    name = request.form.get('name')
    image_url = request.form.get('image_url')
    weapons = request.form.get('weapons')
    species = request.form.get('species')
    catchphrase = request.form.get('catchphrase')
    abilities = request.form.get('abilities')
    create_character(name, image_url, weapons, species, catchphrase, abilities)
    return redirect('/')

def edit(id):
    character = get_character(id)
    return render_template('characters/edit.html', character=character)

def update(id):
    name = request.form.get('name')
    image_url = request.form.get('image_url')
    weapons = request.form.get('weapons')
    species = request.form.get('species')
    catchphrase = request.form.get('catchphrase')
    abilities = request.form.get('abilities')
    update_character(id, name, image_url, weapons, species, catchphrase, abilities)
    return redirect('/')

def delete(id):
    delete_character(id)
    return redirect('/')