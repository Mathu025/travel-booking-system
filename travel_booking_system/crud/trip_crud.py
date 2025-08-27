from datetime import date
from database import SessionLocal
from models import Trip

def add_trip(destination, start_date, end_date, capacity):
    session = SessionLocal()
    trip = Trip(
        destination=destination,
        start_date=start_date,
        end_date=end_date,
        capacity=capacity
    )
    session.add(trip)
    session.commit()
    session.refresh(trip)
    session.close()
    return trip

def list_trips():
    session = SessionLocal()
    trips = session.query(Trip).all()
    session.close()
    return trips

def get_trip(trip_id):
    session = SessionLocal()
    trip = session.query(Trip).filter_by(id=trip_id).first()
    session.close()
    return trip

def delete_trip(trip_id):
    session = SessionLocal()
    trip = session.query(Trip).filter_by(id=trip_id).first()
    if trip:
        session.delete(trip)
        session.commit()
        result = True
    else:
        result = False
    session.close()
    return result