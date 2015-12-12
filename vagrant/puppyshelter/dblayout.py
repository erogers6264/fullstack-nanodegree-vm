#
# Layout the the database tables using sqlalchemy orm
#

# Import everything we'll need
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
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
	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	address = Column(String(250))
	city = Column(String(80))
	state = Column(String)
	zipCode = Column(Integer)
	website = Column(String) 


class Puppy(Base):
	"""What a cute class of objects!"""
	__tablename__ = 'puppy'
	id = Column(Integer, primary_key = True)
	name = Column(String(250), nullable = False)
	gender = Column(String(6), nullable = False)
	dateOfBirth = Column(Date)
	picture = Column(String)
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)
	weight = Column(Numeric(10))


# Engine
engine = create_engine('sqlite:///puppyshelter.db')

# Map the classes by creating corresponding tables
# binding to engine
Base.metadata.create_all(engine)
