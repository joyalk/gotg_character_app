from db.db import sql

def all_characters():
    return sql('SELECT * FROM characters')

def create_character(name, image_url, weapons, species, catchphrase, abilities):
    sql('INSERT INTO characters(name, image_url, weapons, species, catchphrase, abilities) VALUES(%s, %s, %s, %s, %s, %s) RETURNING *', [name, image_url, weapons, species, catchphrase, abilities])

def get_character(id):
    characters = sql("SELECT * FROM characters WHERE id = %s", [id])
    return characters[0]

def update_character(name, image_url, weapons, species, catchphrase, abilities):
    sql('UPDATE characters SET name=%s, image_url=%s, weapons=%s, species=%s, catchphrase=%s, abilities=%s WHERE id=%s RETURNING *', [name, image_url, weapons, species, catchphrase, abilities, id])

def delete_food (id):
    sql('DELETE FROM characters WHERE id=%s RETURNING *', [id])