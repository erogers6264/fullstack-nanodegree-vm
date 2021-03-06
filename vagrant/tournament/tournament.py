#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM matches *")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("DELETE FROM players *")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("SELECT COUNT(*) FROM players;")
    count = c.fetchone()
    db.close()
    return int(count[0])


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s);", (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins,
                                                matches, has_bye):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
        has_bye: whether the player as been assigned a bye in this tournament
    """
    db = connect()
    c = db.cursor()

    c.execute("""SELECT * FROM standings""")
    standings = c.fetchall()

    db.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s)",
              (winner, loser,))
    c.execute("""UPDATE players
                 SET wins=wins + 1
                 WHERE player_id=%s; """, (winner,))
    c.execute("""UPDATE players
                 SET losses=losses + 1
                 WHERE player_id=%s; """, (loser,))
    db.commit()
    db.close()


def hasBye(player):
    """Determines if the player has a bye. Returns a boolean
    indicating the result.
    Args:
        player: the id number of the player in question
    """
    db = connect()
    c = db.cursor()
    c.execute("SELECT has_bye FROM players WHERE player_id=%s", (player,))
    bye = c.fetchone()
    db.close()
    return bye[0]


def assignBye(player):
    db = connect()
    c = db.cursor()
    c.execute("""UPDATE players
                 SET has_bye=TRUE, wins=wins+1
                 WHERE player_id=%s""", (player,))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()

    # Organize the player ids and names into a list of tuples
    idnamepairs = [(row[0], row[1]) for row in standings]
    pairs = []
    even = (len(idnamepairs) % 2) == 0  # Determine whether even

    if even:
        i = 0
        while i < len(idnamepairs):
            pair = idnamepairs[i] + idnamepairs[i+1]
            pairs.append(pair)
            i += 2
    else:
        # Iterate and assign a bye to the first player without one
        for player in idnamepairs:
            if hasBye(player[0]) == False:
                assignBye(player[0])
                # Grab the byed player then break to proceed to pairing
                byed = idnamepairs.pop(idnamepairs.index(player))
                break
        # Pair the remaining number of players (now even)
        i = 0
        while i < len(idnamepairs):
            pair = idnamepairs[i] + idnamepairs[i+1]
            pairs.append(pair)
            i += 2
        # Append the byed player to the end of the pairing list
        pairs.append(byed)
    return pairs
