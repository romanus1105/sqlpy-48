import sqlalchemy
from pprint import pprint
from getpass import getpass

engine = sqlalchemy.create_engine(f'postgresql://{input("Enter username: ")}:{getpass("Enter password: ")}@{input("Enter host to connect")}:{input("Enter port your DB is listening to: ")}/{input("Enter DB name: ")}')
connection = engine.connect()

pprint(connection.execute('''
SELECT name, COUNT(musician_id) FROM genres
JOIN genremusician ON genres.id = genremusician.genre_id
GROUP BY name;
''').fetchall())

pprint(connection.execute('''
SELECT name FROM songs
WHERE album_id = (SELECT id FROM albums
WHERE released = 2020 OR released = 2019);
''').fetchall())

pprint(connection.execute('''
SELECT albums.name, AVG(length) FROM songs
JOIN albums ON songs.album_id = albums.id
GROUP BY albums.name;
''').fetchall())

pprint(connection.execute('''
SELECT musicians.name FROM musicians
JOIN musicianalbum ON musicians.id = musicianalbum.musician_id
JOIN albums ON musicianalbum.album_id = albums.id
WHERE released != 2020;
''').fetchall())

pprint(connection.execute('''
SELECT DISTINCT collections.name, musicians.name FROM collections
JOIN collectionsong ON collectionsong.collection_id = collections.id
JOIN songs ON collectionsong.song_id = songs.id
JOIN albums ON songs.album_id = albums.id
JOIN musicianalbum ON musicianalbum.album_id = albums.id
JOIN musicians ON musicians.id = musicianalbum.musician_id
WHERE musicians.name = 'Eminem';
''').fetchall())

pprint(connection.execute('''
SELECT musicians.name, albums.name, COUNT(genre_id) FROM musicians
JOIN genremusician ON musicians.id = genremusician.musician_id
JOIN musicianalbum ON musicians.id = genremusician.musician_id
JOIN albums ON musicianalbum.album_id = albums.id
GROUP BY musicians.name, albums.name
HAVING COUNT(genre_id)>1;
''').fetchall())

pprint(connection.execute('''
SELECT songs.name FROM songs
LEFT JOIN collectionsong ON songs.id = collectionsong.song_id
WHERE collectionsong.song_id IS NULL;
''').fetchall())

pprint(connection.execute('''
SELECT musicians.name FROM songs
JOIN musicianalbum ON songs.album_id = musicianalbum.album_id
JOIN musicians ON musicians.id = musicianalbum.musician_id
WHERE length = (SELECT MIN(length) FROM songs);
''').fetchall())

pprint(connection.execute('''
WITH new_table AS (SELECT albums.name, COUNT(songs.id) AS cnt
FROM songs
JOIN albums ON songs.album_id = albums.id
GROUP BY albums.name)
SELECT name, cnt FROM new_table
WHERE cnt = (SELECT MIN(cnt) FROM new_table);
''').fetchall())
