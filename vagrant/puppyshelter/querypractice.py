
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from dblayout import Base, Shelter, Puppy
import datetime
from datetime import timedelta

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()


# Show all puppies
def showPuppies():
	print(session.query(Puppy).all())

# Show all puppiers less than 6 months old ordered by the 
# yougest first
def lessSixMonths():
	today = datetime.date.today()
	sixMonths = timedelta(days=180)
	sixMonthsAgo = today - sixMonths

	lessThan6Months = session.query(Puppy).filter(sixMonthsAgo < Puppy.dateOfBirth)\
					  .order_by(Puppy.dateOfBirth.desc())
	for i in lessThan6Months:
	 	print i.name, i.dateOfBirth

# Show puppies by ascending weight
def weightAscending():
	weightAscending = session.query(Puppy).order_by(Puppy.weight)
	for i in weightAscending:
		print i.name, i.weight

# Show all puppies grouped by the shelter they are staying in
def byShelter():
	byShelter = session.query(Puppy).join("shelter").order_by(Shelter.name)
	for pup in byShelter:
		print pup.name, pup.shelter.name
