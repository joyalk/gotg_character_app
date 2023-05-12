import psycopg2
import psycopg2.extras

DB_URL = 'dbname=guradians_of_the_galaxy_characters_db'

def sql(query, parameters=[]):
    connection = psycopg2.connect(DB_URL)
    cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute(query, parameters)
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    return results