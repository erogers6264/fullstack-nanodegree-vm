#
# Layout the the database tables using sqlalchemy orm
#

# Import everything we'll need
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

# Return a new, magical base class from which
# all mapped classes should inherit
Base = declarative_base()

# Time to write the classes which will be mapped
class Shelter(Base):
	"""Dogooders in this world"""

	__tablename__ = 'shelter'

	name = Column(String(80), nullable = False)
	address = Column(String)
	city = Column(String)
	state = Column(String)
	zipCode = Column(Integer)
	website = Column(String) 
	id = Column(Integer, primary_key = True)
	puppy = relationship("Puppy", backref="shelter")

	# def __init__(self, name, address, city, 
	# 			 state, zipCode, website, id):
	# 	self.name = name
	# 	self.address = address
	# 	self.city = city
	# 	self.state = state
	# 	self.zipCode = zipCode
	# 	self.website = website
	# 	self.id = id

	# def __repr__(self):
	# 	return """<Shelter('%s','%s', '%s', '%s',
	# 		 			   '%s', '%s', '%s')>""" % 
	# 					  (self.name,
	# 					   self.address, self.city,
	# 					   self.state, self.zipCode,
	# 					   self.website, self.id)


class Puppy(Base):
	"""What a cute class of objects!"""

	__tablename__ = 'puppy'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	dateOfBirth = Column(String) # Maybe look up a date data type
	gender = Column(String)
	weight = Column(Integer)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))

	# def __init__(self, name, dateOfBirth, gender, 
	# 			 weight, shelter_id, shelter):
	# 	super(Puppy, self).__init__()
	# 	self.arg = arg
	# 	self.name = name
	# 	self.dateOfBirth = dateOfBirth
	# 	self.gender = gender
	# 	self.weight = weight
	# 	self.shelter_id = shelter_id
	# 	self.shelter = shelter

	# def __repr__(self):
	# 	return """<Puppy('%s','%s', '%s', '%s',
	# 		 			 '%s', '%s', '%s')""" %
	# 					(self.arg, self.name, self.dateOfBirth, self.gender,
	# 					 self.weight, self.shelter_id, self.shelter)


# Engine
engine = create_engine('sqlite:///puppies.db')

# Map the classes by creating corresponding tables
# binding to engine
Base.metadata.create_all(engine)