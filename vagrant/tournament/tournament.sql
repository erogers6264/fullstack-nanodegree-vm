-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create the database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connect to the database
\c tournament;

-- Create the players table
DROP TABLE IF EXISTS players;
CREATE TABLE players(
	player_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	wins INTEGER DEFAULT 0,
	losses INTEGER DEFAULT 0
);

-- Create the matches table
DROP TABLE IF EXISTS matches;
CREATE TABLE matches(
	match_id SERIAL PRIMARY KEY,
	winner INTEGER REFERENCES players (player_id),
	loser INTEGER REFERENCES players (player_id),
	UNIQUE (winner, loser)
);

-- Create a view of players ordered by wins
CREATE VIEW standings AS
	SELECT player_id, name, wins, (wins+losses) AS
	matches FROM players ORDER BY wins DESC;

CREATE VIEW unique_matches AS
	SELECT player_id
