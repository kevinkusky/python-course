from pprint import pprint
import psycopg2

CONNECTION_PARAMETERS = {
    'dbname': 'petrack',
    'user': 'vet_app',
    'password': 'password',
    'host': 'localhost'
}

# ** - double splat - spread into key:value pairs
# with to close connection after
with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
    with conn.cursor() as cursor:
        # executes with SQL querery 
        cursor.execute("""
            SELECT id, first_name, last_name, email
            FROM owners
            ORDER BY last_name
        """)
        print('owners')
        # pprint(cursor.fetchall())
        # := - whilerus opporator - assignment as part of condition
        while row := cursor.fetchone():
            pprint(row)

        # Querery with search parameter
        # %(nameOfEntry)s - placeholder for search related queries
        cursor.execute("""
            SELECT id, first_name, last_name, email
            FROM owners
            WHERE last_name like %(filter)s
            ORDER BY last_name
        """, {'filter': 'M%'})
        print("\nowners M%")
        while row := cursor.fetchone():
            pprint(row)

        # InsertQuerery with 'user entered' data
        cursor.execute("""
            INSERT INTO owners(first_name, last_name, email)
            VALUES (%(first_name)s, %(last_name)s, %(email)s)
        """, {
            'first_name': 'Carol',
            'last_name': 'Pepesylvia',
            'email': 'charlieday@kittenmittens.org',
        })
        # Secondary querery to print new entry
        cursor.execute("""
            SELECT id, first_name, last_name, email
            FROM owners
            ORDER BY last_name
        """)
        print('\nowners after insert')
        while row := cursor.fetchone():
            pprint(row)

        # Join Querery with keys from 2 data tables 
        cursor.execute("""
            SELECT p.id, p.name, pt.type, p.age, p.has_microchip
            FROM pets p
            JOIN pet_types pt ON (p.pet_type_id = pt.id)
            ORDER BY name
        """)
        print('\nowners after insert')
        while row := cursor.fetchone():
            pprint(row)
