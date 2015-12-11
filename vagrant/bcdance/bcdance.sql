-- Create our database
DROP DATABASE IF EXISTS bcdance;
CREATE DATABASE bcdance;

--Connect to this said database
\c bcdance;

-- Create our tables

DROP TABLE IF EXISTS shows;
CREATE TABLE shows(
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

DROP TABLE IF EXISTS dancers;
CREATE TABLE dancers(
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	fullname TEXT
);

DROP TABLE IF EXISTS pieces;
CREATE TABLE pieces(
	id SERIAL PRIMARY KEY,
	name TEXT NOT NULL
);

-- With some linking tables for many to many relationships
-- Can we query this in interesting ways using joins?
DROP TABLE IF EXISTS dancers_pieces;
CREATE TABLE dancers_pieces(
	dancer_id INTEGER REFERENCES dancers (id),
	piece_id INTEGER REFERENCES pieces (id)
);

DROP TABLE IF EXISTS pieces_shows;
CREATE TABLE pieces_shows(
	piece_id INTEGER REFERENCES pieces (id),
	show_id INTEGER REFERENCES shows (id)
);

DROP TABLE IF EXISTS dancers_shows;
CREATE TABLE dancers_shows(
	dancer_id INTEGER REFERENCES dancers (id),
	show_id INTEGER REFERENCES shows (id)
);