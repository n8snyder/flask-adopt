"""Seed file to make sample data for Users db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add Users
whiskey = Pet(name='Whiskey', 
                species="dog", 
                photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTi-tSMJdDZLMq1-bjfgHHN1KKh7XY5ubMjYQ_YsPK30Fx0ONJzs-fO78_iUKIJfpnMl3U&usqp=CAU", 
                age = "young",
                notes = "",
                available = True)
bowser = Pet(name='bowser', 
                species="dragon", 
                photo_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTi-tSMJdDZLMq1-bjfgHHN1KKh7XY5ubMjYQ_YsPK30Fx0ONJzs-fO78_iUKIJfpnMl3U&usqp=CAU", 
                age = "adult",
                notes = "",
                available = False)


# Add new objects to session, so they'll persist
db.session.add(whiskey)
db.session.add(bowser)

# Commit--otherwise, this never gets saved!
db.session.commit()