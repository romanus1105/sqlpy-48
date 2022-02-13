import sqlalchemy
from pprint import pprint
from getpass import getpass

engine = sqlalchemy.create_engine(f'postgresql://{input("Enter username: ")}:{getpass("Enter password: ")}@{input("Enter host to connect")}:{input("Enter port your DB is listening to: ")}/{input("Enter DB name: ")}')
connection = engine.connect()
pprint(connection.execute('''
SELECT name, released FROM albums
WHERE released = 2018;
''').fetchall())
pprint(connection.execute('''
SELECT name, length FROM songs
ORDER BY length DESC
LIMIT 1;
''').fetchone())
pprint(connection.execute('''
SELECT name, length FROM songs
WHERE length >= 210;
''').fetchall())
pprint(connection.execute('''
SELECT name FROM collections
WHERE released BETWEEN 2018 AND 2020;
''').fetchall())
pprint(connection.execute('''
SELECT name FROM musicians
WHERE name NOT LIKE '%% %%';
''').fetchall())
pprint(connection.execute('''
SELECT name FROM songs
WHERE name iLIKE '%%my%%' OR name iLIKE '%%мой%%';
''').fetchall())
