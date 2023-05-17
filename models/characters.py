from db.db import sql

def all_characters():
    return sql('SELECT * FROM characters')

def create_character(name, image_url, weapons, species, catchphrase, abilities):
    sql('INSERT INTO characters(name, image_url, weapons, species, catchphrase, abilities) VALUES(%s, %s, %s, %s, %s, %s) RETURNING *', [name, image_url, weapons, species, catchphrase, abilities])

def get_character(id):
    characters = sql("SELECT * FROM characters WHERE id = %s", [id])
    return characters[0]

def update_character(id, name, image_url, weapons, species, catchphrase, abilities):
    sql('UPDATE characters SET name=%s, image_url=%s, weapons=%s, species=%s, catchphrase=%s, abilities=%s WHERE id=%s RETURNING *', [name, image_url, weapons, species, catchphrase, abilities, id])

def add_comment_character(id, comment):
    sql('INSERT INTO comments(character_id, comment) VALUES(%s, %s) RETURNING *', [id, comment])

def get_comments(character_id):
    comments = sql("SELECT * FROM comments WHERE character_id = %s", [character_id])
    return comments

def delete_character(id):
    sql('DELETE FROM characters WHERE id=%s RETURNING *', [id])

def get_all_comments():
    comments = sql('SELECT * FROM comments')
    return comments