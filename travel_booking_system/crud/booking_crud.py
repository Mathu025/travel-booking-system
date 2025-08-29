from datetime import date
from database import SessionLocal
from models import Booking, Traveler, Trip
import click

def add_booking():
    session = SessionLocal()

    travelers = session.query(Traveler).all()
    click.secho("Travelers:", fg="cyan")
    for t in travelers:
        click.echo(f"{t.id}. {t.name} ({t.email})")
    traveler_id = click.prompt("Enter traveler ID", type=int)
    traveler = session.query(Traveler).filter_by(id=traveler_id).first()
    if not traveler:
        click.secho(f"Traveler not found!", fg="red")
        session.close()
        return
        

    trips = session.query(Trip).all()
    click.secho("Trips:", fg="cyan")
    for tr in trips:
        click.echo(f"{tr.id}.{tr.destination} ({tr.start_date}-{tr.end_date}, Capacity: {tr.capacity})")
    trip_id = click.prompt("Enter trip ID", type=int)
    trip = session.query(Trip).filter_by(id=trip_id).first()
    if not trip:
        click.secho(f"Trip npt found!", fg="red")
        session.close()
        return


    traveler = session.query(Traveler).filter_by(id=traveler_id).first()
    trip = session.query(Trip).filter_by(id=trip_id).first()

    
    booking = Booking(
        traveler_id=traveler_id,
        trip_id=trip_id,
        booking_date=date.today(),
        status="Confirmed"
    )
    session.add(booking)
    session.commit()
    click.secho(f"Booking confirmed: {traveler.name}-{trip.destination}\n", fg="green")
    session.close()
    return booking

def list_bookings():
    session = SessionLocal()
    bookings = session.query(Booking).all()

    click.secho("Bookings:", fg="cyan")
    for b in bookings:
        traveler = session.query(Traveler).filter_by(id=b.traveler_id).first()
        trip = session.query(Trip).filter_by(id=b.trip_id).first()
        traveler_name = traveler.name if traveler else "Unknown Traveler"
        trip_dest = trip.destination if trip else "Unknown Trip"
        click.echo(f"{b.id}.{traveler_name}-{trip_dest}, Status: {b.status}")
    session.close()
    return bookings
    
def get_traveler_bookings():
    traveler_id = click.prompt("Enter Traveler ID to view bookings", type=int)
    session = SessionLocal()
    bookings = session.query(Booking).filter_by(traveler_id=traveler_id).all()

    click.secho(f"Bookings for traveler ID {traveler_id}:", fg="cyan")
    for b in bookings:
        trip = session.query(Trip).filter_by(id=b.trip_id).first()
        trip_dest = trip.destination if trip else "Unknown Trip"
        click.echo(f"{b.id}.{trip_dest}, Status: {b.status}")

    session.close()
    return bookings

def get_trip_bookings():
    trip_id = click.prompt(f"Enter trip ID to view bookings", type=int)
    session = SessionLocal()
    bookings = session.query(Booking).filter_by(trip_id=trip_id).all()

    click.secho(f"Bookings for trip ID {trip_id}:", fg="cyan")
    for b in bookings:
        traveler = session.query(Traveler).filter_by(id=b.traveler_id).first()
        traveler_name = traveler.name if traveler else "Unknown Traveler"
        click.echo(f"{b.id}.{traveler_name}, Status: {b.status}")

    session.close()
    return bookings

def cancel_booking():
    booking_id = click.prompt("Enter booking ID to cancel", type=int)
    session = SessionLocal()
    booking = session.query(Booking).filter_by(id=booking_id).first()
    if booking: 
        booking.status = "Cancelled"
        session.commit()
        click.secho(f"Booking {booking_id} cancelled sucessfully!\n", fg="red")
    else:
        click.secho(f"Booking ID {booking_id} not found!", fg="red")
    session.close()


