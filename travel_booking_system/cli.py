import click
from crud.traveler_crud import add_traveler, list_travelers
from crud.trip_crud import add_trip, list_trips
from crud.booking_crud import add_booking, cancel_booking, get_traveler_bookings, get_trip_bookings

from database import engine, Base
from  models import Traveler, Trip, Booking

Base.metadata.create_all(bind=engine)

# ----------------- Traveler  Commands -----------------
@click.group()
def traveler():
    """Traveler commands"""
    pass

@traveler.command()
def view_trips():
    """View All trips"""
    trips = list_trips()
    for trip in trips:
        click.echo(f"{trip.id}: {trip.destination} ({trip.start_date}- {trip.end_date}) Capacity: {trip.capacity}")

@traveler.command()
@click.option("--traveler-id", type=int, prompt=True)
@click.option("--trip-id", type=int, prompt=True)
def book_trip(traveler_id, trip_id):
    """Book a trip"""
    booking, msg = add_booking(traveler_id, trip_id)
    click.echo(msg)

@traveler.command()
@click.option("--traveler-id", type=int, prompt=True)
def view_bookings(traveler_id):
    """View bookings for a traveler"""
    bookings = get_traveler_bookings(traveler_id)
    for b in bookings:
        click.echo(f"Booking {b.id}: Trip {b.trip_id} status {b.status}")


# ----------------- Admin Commands -----------------
@click.group()
def admin():
    """Admin commands"""
    pass

@admin.command()
def view_trips():
    trips = list_trips()
    for trip in trips:
        click.echo(f"{trip.id}: {trip.destination} ({trip.start_date} - {trip.end_date}) Capacity: {trip.capacity}")

@admin.command()
@click.option("--trip-id", type=int, prompt=True)
def view_bookings(trip_id):
    bookings = get_trip_bookings(trip_id)
    for b in bookings:
        click.echo(f"Booking {b.id}: Traveler {b.traveler_id} Status {b.status}")



# ----------------- Main CLI -----------------
@click.group()
def cli():
    """Travel Booking System CLI"""
    pass

cli.add_command(traveler)
cli.add_command(admin)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    cli()



