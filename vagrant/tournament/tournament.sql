-- Create the database
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connect to the database
\c tournament;

-- Create the tournaments table
CREATE TABLE tournaments(
	tournament_id SERIAL PRIMARY KEY,
	players INTEGER REFERENCES players (player_id),
	matches INTEGER REFERENCES matches (match_id),
	winner INTEGER REFERENCES players (player_id) DEFAULT NULL
);

-- Create the players table
CREATE TABLE players(
	player_id SERIAL PRIMARY KEY,
	name TEXT NOT NULL,
	wins INTEGER DEFAULT 0,
	losses INTEGER DEFAULT 0,
	tournament INTEGER REFERENCES tournaments (tournament_id)
);

-- Create the matches table
CREATE TABLE matches(
	match_id SERIAL PRIMARY KEY,
	winner INTEGER REFERENCES players (player_id),
	loser INTEGER REFERENCES players (player_id),
	tournament INTEGER REFERENCES tournaments (tournament_id)
);

-- Create a view of players ordered by wins
CREATE VIEW standings AS
	SELECT player_id, name, wins, (wins+losses) AS
	matches FROM players ORDER BY wins DESC;
