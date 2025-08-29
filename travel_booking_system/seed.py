from database import SessionLocal, Base, engine
from models import Traveler, Trip
from datetime import date

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

travelers_data = [
    {"name": "Alice", "email":"alice72@gmail.com", "phone": "67543", "passport_number": "P1256788"},
    {"name": "John", "email": "john970@gmail.com", "phone": "345890", "passport_number": "P26780297"},
    {"name": "Doe", "email": "doe123@gmail.com", "phone": "4562309", "passport_number": "P09754637"}
]

trips_data = [
    {"destination": "Paris", "start_date": date(2025, 9, 8), "end_date": date(2025, 10, 10), "capacity": 25},
    {"destination": "Dubai", "start_date": date(2025, 10, 10), "end_date": date(2025, 11, 18), "capacity": 15},
    {"destination": "Egypt", "start_date": date(2025, 11, 20), "end_date": date(2025, 12, 20), "capacity": 30}
]

session = SessionLocal()

for t in travelers_data:
    traveler = Traveler(**t)
    session.add(traveler)

for tr in trips_data:
    trip = Trip(**tr)
    session.add(trip)

session.commit()
session.close()

print("Seed data added successfully!")