from pprint import pprint
import psycopg2

CONNECTION_PARAMETERS = {
    'dbname': 'petrack',
    'user': 'vet_app',
    'password': 'password',
    'host': 'localhost'
}

with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT id, first_name, last_name, email
            FROM owners
            ORDER BY last_name
        """)
        print('owners')
        pprint(cursor.fetchall())
        