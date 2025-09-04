from database import SessionLocal, Base, engine
from models import Traveler, Trip, Booking
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

travelers = []
for t in travelers_data:
    traveler = Traveler(**t)
    session.add(traveler)
    travelers.append(traveler)

trips = []
for tr in trips_data:
    trip = Trip(**tr)
    session.add(trip)
    trips.append(trip)

session.commit()

bookings_data = [
    {"traveler_id": travelers[0].id, "trip_id": trips[0].id,"booking_date": date.today(), "status": "Confirmed"},
    {"traveler_id": travelers[1].id, "trip_id": trips[1].id,"booking_date": date.today(), "status": "Confirmed"},
    {"traveler_id": travelers[2].id, "trip_id": trips[2].id,"booking_date": date.today(), "status": "Confirmed"},
]

for b in bookings_data:
    booking = Booking(**b)
    session.add(booking)

session.commit()
session.close()

print("Seed data added successfully!") 