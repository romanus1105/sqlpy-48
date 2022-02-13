create table if not exists genres(
	id serial primary key,
	name varchar(50) not null unique
);
create table if not exists musicians(
	id serial primary key,
	name varchar(50) not null unique
);
create table if not exists genremusician(
    musician_id integer not null references musicians(id),
    genre_id integer not null references genres(id),
    constraint gm_pk primary key (musician_id, genre_id)
);
create table if not exists albums(
	id serial primary key,
	name varchar(100) not null,
	released integer not null
);
create table if not exists musicianalbum(
    id serial primary key,
    album_id integer not null references albums(id),
    musician_id integer not null references musicians(id)
);
create table if not exists songs(
	id serial primary key,
	name varchar(100) not null,
	length integer not null,
	album_id integer references albums(id)
);
create table if not exists collections(
    id serial primary key,
    name varchar(100) not null,
    released integer not null
);
create table if not exists collectionsong(
    song_id integer not null references songs(id),
    collection_id integer not null references collections(id),
    constraint cs_pk primary key (song_id, collection_id)
);
