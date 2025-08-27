from datetime import date
from database import SessionLocal
from models import Booking, Traveler, Trip

def add_booking(traveler_id, trip_id):
    session = SessionLocal()

    traveler = session.query(Traveler).filter_by(id=traveler_id).first()
    trip = session.query(Trip).filter_by(id=trip_id).first()

    if not traveler or not trip:
        session.close()
        return None, "Traveler or Trip not found."

    booked_count = session.query(Booking).filter_by(trip_id=trip_id, status="Confirmed").count()
    if booked_count >= trip.capacity:
        session.close()
        return None, "Trip is full."
    
    booking = Booking(
        traveler_id=traveler_id,
        trip_id=trip_id,
        booking_date=date.today(),
        status="Confirmed"
    )
    session.add(booking)
    session.commit()
    session.close()
    return booking, "Booking confirmed"

def list_bookings():
    session = SessionLocal()
    bookings = session.query(Booking).all()
    session.close()
    return bookings
    
def get_traveler_bookings(traveler_id):
    session = SessionLocal()
    bookings = session.query(Booking).filter_by(traveler_id=traveler_id).all()
    session.close()
    return bookings

def get_trip_bookings(trip_id):
    session = SessionLocal()
    bookings = session.query(Booking).filter_by(trip_id=trip_id).all()
    session.close()
    return bookings

def cancel_booking(booking_id):
    session = SessionLocal()
    booking = session.query(Booking).filter_by(id=booking_id).first()
    if booking and booking.status != "Cancelled":
        booking.status = "Cancelled"
        session.commit()
        result = True
    else:
        result = False
    session.close()
    return result


