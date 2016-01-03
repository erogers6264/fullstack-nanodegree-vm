-- Create the database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connect to the database
\c tournament;

-- Create the players table
CREATE TABLE players(
	player_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	wins INTEGER DEFAULT 0,
	losses INTEGER DEFAULT 0,
	has_bye	BOOLEAN DEFAULT FALSE
);

-- Create the matches table
CREATE TABLE matches(
	match_id SERIAL PRIMARY KEY,
	winner INTEGER REFERENCES players (player_id),
	loser INTEGER REFERENCES players (player_id),
);

-- Create a view of players ordered by wins
CREATE VIEW standings AS
	SELECT player_id, name, wins, (wins+losses), has_bye AS
	matches FROM players ORDER BY wins DESC;
