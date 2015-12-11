#
# Layout the the database tables using sqlalchemy orm
#

# Import everything we'll need
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
	"""docstring for Shelter"""
	__tablename__ = 'shelter'
	name = Column(String(80), nullable = False)
	address = Column(String)
	city = Column(String)
	state = Column(String)
	zipCode = Column(Integer)
	website = Column(String) 
	id = Column(Integer, primary_key = True)

	def __init__(self, name, address, city, 
				 state, zipCode, website, id):
		self.name = name
		self.address = address
		self.city = city
		self.state = state
		self.zipCode = zipCode
		self.website = website
		self.id = id

	def __repr__(self):
		return "<User('%s','%s', '%s')>" % (self.name, self.address, self.city,
											self.state, self.zipCode,
											self.website, self.id)


class Puppy(Base):
	"""docstring for Puppy"""

	__tablename__ = 'puppy'

	name = Column(String(80), nullable = False)
	dateOfBirth = Column() # Maybe look up a date data type
	gender = Column()
	weight = Column()
	shelter_id = Column()

	def __init__(self, arg):
		super(Puppy, self).__init__()
		self.arg = arg

	def __repr__(self):
		pass


# Engine
engine = create_engine('sqlite:///puppies.db')