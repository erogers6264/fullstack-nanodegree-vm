from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from dblayout import Base, Shelter, Puppy
import datetime
from datetime import timedelta

engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()

sixMonths = timedelta(days=180)
print(session.query(Puppy).all())
lessThan6Months = session.query(Puppy).filter(timedelta(\
								Puppy.dateOfBirth) <= sixMonths)
for i in lessThan6Months:
	print i.name, i.dateOfBirth