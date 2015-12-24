# [Swiss Pairings](https://github.com/erogers6264/fullstack-nanodegree-vm)

This Swiss Pairings program will help organize and pair players for a swiss style tournament, created by [Ethan Rogers](https://github.com/erogers6264).

To get started, check out below!

## Table of contents
* Documentation
* Bugs and feature requests
* Creators
* Copyright & license

## Documentation
* Clone the fullstack-nanodegree-vm repository
* Run vagrant up in the tournament directory and connect via ssh:
```
vagrant up
vagrant ssh
```
	* Run `psql` and import the `tournament.sql` file
```
\i tournament.sql`
\q
```
* Run the tests to see them pass!
```
python tournament_test.py
```
## Use
* You can use the program by opening a python shell and typing
```
from tournament import *
```
* All of the functions contained within the tournament module will be imported. See documentation within the tournament.py file. 

## Bugs and feature requests
Have a bug or a feature request? Please e-mail me at erogers6264@gmail.com

## Creators
Ethan Rogers, Udacity

## Copyright & license
This work is licensed under the Creative Commons Attribution 4.0 International
License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/.
