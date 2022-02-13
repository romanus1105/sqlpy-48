import sqlalchemy
from getpass import getpass

engine = sqlalchemy.create_engine(f'postgresql://{input("Enter username: ")}:{getpass("Enter password: ")}@{input("Enter host to connect")}:{input("Enter port your DB is listening to: ")}/{input("Enter DB name: ")}')
connection = engine.connect()
connection.execute('''
INSERT INTO genres
VALUES(1, 'Rock'), (2, 'Pop'), (3, 'Rap'), (4, 'Jazz'), (5, 'Electronic');
''')
connection.execute('''
INSERT INTO musicians
VALUES(1, 'Eric Clapton'), 
(2, 'Tom Jones'), 
(3, '50 Cent'), 
(4, 'Louis Armstrong'), 
(5, 'Armin van Buuren'),
(6, 'Jimi Hendrix'),
(7, 'Frank Sinatra'),
(8, 'Eminem');
''')
connection.execute('''
INSERT INTO genremusician
VALUES(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 1), (7, 2), (8, 3);
''')
connection.execute('''
INSERT INTO albums
VALUES(1, 'No Reason to Cry', 1976),
(2, 'Green, Green Grass of Home', 1967),
(3, 'The Massacre', 2005),
(4, 'Hello Dolly!', 1964),
(5, 'Balance', 2018),
(6, 'Are You Experienced', 1967),
(7, 'My Way', 1969),
(8, 'Encore', 2004);
''')
connection.execute('''
INSERT INTO musicianalbum
VALUES(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), 
(5, 5, 5), (6, 6, 6), (7, 7, 7), (8, 8, 8);
''')
connection.execute('''
INSERT INTO songs
VALUES(1, 'Carnival', 224, 1), (2, 'Double Trouble', 263, 1),
(3, 'Green, Green Grass of Home', 144, 2), (4, 'He will Have to Go', 140, 2),
(5, 'In My Hood', 231, 3), (6, 'This is 50', 184, 3),
(7, 'It is been a long, long time', 162, 4), (8, 'Hey, look ober me!', 154, 4),
(9, 'Wild Wild Son', 213, 5), (10, 'Blah Blah Blah', 183, 5),
(11, 'Remember', 163, 6), (12, 'Fire', 150, 6),
(13, 'My way', 275, 7), (14, 'All My Tomorrows', 275, 7),
(15, 'Puke', 248, 8), (16, 'Big Weenie', 277, 8);
''')
connection.execute('''
INSERT INTO collections
VALUES(1, 'The Best 60s', 1999),
(2, 'Romantic Collection', 1985), 
(3, 'Cripz Niggas', 2020), 
(4, 'The Jazz Founding Fathers', 1979),
(5, '2018 London Rave', 2018),
(6, 'Rock Classics', 1997),
(7, 'The Sopranos: Music from the HBO Original Series', 2012),
(8, 'Tracks We Grown On', 2016);
''')
connection.execute('''
INSERT INTO collectionsong
VALUES(1, 1), (2, 1), (3, 2), (4,2), (5, 3), (6, 3), (7, 4), (8, 4),
(9, 5), (10, 5), (11, 6), (12, 6), (13, 7), (14, 7), (15, 8), (16, 8);
''')