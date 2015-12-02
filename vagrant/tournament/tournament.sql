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
DROP VIEW IF EXISTS standings;
CREATE VIEW standings AS
	SELECT player_id, name, wins, (wins+losses) AS
	matches FROM players ORDER BY wins DESC;
