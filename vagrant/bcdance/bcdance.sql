CREATE DATABASE bcdance;
\c bcdance;

CREATE TABLE shows(
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE dancers(
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	fullname TEXT
);

CREATE TABLE pieces(
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

CREATE TABLE pieces_shows(
	piece_id INTEGER REFERENCES pieces (id),
	show_id INTEGER REFERENCES shows (id)
);