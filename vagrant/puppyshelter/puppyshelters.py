#
# This module provides functions to work with the database
#
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dblayout import Base, Shelter, Puppy, Adopter, Profile 

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Create a function to check a puppy into a shelter, if the shelter is at
# capacity, prompt the user to try a different shelter. If you’re feeling
# extra ambitious write an algorithm that will find another shelter in the
# same area or with a higher vacancy. If all shelters are full, prompt the
# user that a new shelter needs to be opened.

# Feeling Extra Udacious?
# Write a load-balancing algorithm that can transfer puppies evenly throughout
# all the shelters in the database.

def registerPuppy(name, gender, dateOfBirth, picture,
				  shelter_id, shelter, weight, profile, adopters):
	pup = Puppy(self.name = name,
				self.gender = gender,
				self.dateOfBirth = dateOfBirth, 
				self.picture = picture, 
				self.weight = weight)


def balancePuppies():
	pass