#!/usr/bin/env python
#
# bcdance.py -- implementation of show management
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=bcdance")