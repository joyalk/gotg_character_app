from flask import render_template, request, redirect
from models.characters import all_characters, get_character, create_character, update_character, delete_character, add_comment_character, get_comments, get_all_comments
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

def comments(id):
    character = get_character(id)
    comments = get_comments(id)
    return render_template('characters/comment.html', character=character, comments=comments)
    
def add_comment(id):    
    comment = request.form.get('comment', '')
    add_comment_character(id, comment)
    return redirect('/')

def display_comments():
    all_comments = get_all_comments()

    character_comment_map = {}

    for item in all_comments:
        character_id = item['character_id']
        comment = item['comment']
        character_name = get_character(character_id)['name']

        if str(character_name) not in character_comment_map:
            character_comment_map[str(character_name)] = []
        
        character_comment_map[str(character_name)].append(comment)
    return render_template('characters/comments_section.html',character_comment_map=character_comment_map)