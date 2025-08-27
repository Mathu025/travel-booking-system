import click
from crud.traveler_crud import add_traveler, list_travelers
from crud.trip_crud import add_trip, list_trips
from crud.booking_crud import add_booking, cancel_booking, get_traveler_bookings, get_trip_bookings

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

