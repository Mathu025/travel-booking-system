from datetime import date
from database import SessionLocal
from models import Trip
import click

def add_trip():
    destination = click.prompt("Enter Trip destination")
    start_date_str = click.prompt("Enter Start Date (YYYY-MM-DD)")
    end_date_str = click.prompt("Enter End Date (YYYY-MM-DD)")
    capacity = click.prompt("Enter trip capacity", type=int)

    start_date = date.fromisoformat(start_date_str)
    end_date = date.fromisoformat(end_date_str)

    session = SessionLocal()
    trip = Trip(
        destination=destination,
        start_date=start_date,
        end_date=end_date,
        capacity=capacity
    )
    session.add(trip)
    session.commit()
    session.close()
    click.secho(f"Trip to {destination} added successfully!\n", fg="green")
    return trip

def list_trips():
    session = SessionLocal()
    trips = session.query(Trip).all()
    session.close()

    click.secho(f"Trips:", fg="cyan")
    for t in trips:
        click.echo(f"{t.id}. {t.destination} ({t.start_date}-{t.end_date}), Capacity: {t.capacity} ")
    return trips

def get_trip():
    trip_id = click.prompt("Enter trip ID", type=int)
    session = SessionLocal()
    trip = session.query(Trip).filter_by(id=trip_id).first()
    session.close()

    click.secho(f"Trip {trip.id}: {trip.destination} ({trip.start_date}-{trip.end_date}) Capacity: {trip.capacity}", fg="cyan")
    return trip

def delete_trip():
    trip_id = click.prompt("Enter trip ID to delete", type=int)
    session = SessionLocal()
    trip = session.query(Trip).filter_by(id=trip_id).first()

    session.delete(trip)
    session.commit()
    session.close()
    click.secho(f"Trip '{trip.destination}' deleted successfully!", fg="green")