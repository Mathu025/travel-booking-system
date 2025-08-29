import click
from crud.traveler_crud import add_traveler, list_travelers, get_traveler, delete_traveler
from crud.trip_crud import add_trip, list_trips, get_trip, delete_trip
from crud.booking_crud import add_booking, list_bookings, cancel_booking, get_traveler_bookings, get_trip_bookings

@click.command()
def menu():
    while True:
        click.secho("\n===== Travel Booking System =====", fg="cyan", bold=True)
        click.secho("1. Manage Travelers", fg="green")
        click.secho("2. Manage Trips", fg="green")
        click.secho("3. Manage Bookings", fg="green")
        click.secho("4. Exit", fg="red")

        choice = click.prompt("Enter your choice", type=int)

        if choice == 1:
            manage_travelers()
        elif choice == 2:
            manage_trips()
        elif choice == 3:
            manage_bookings()
        elif choice == 4:
            click.secho("Goodbye!", fg="yellow")
            break
        else:
            click.secho("Invalid Choice. Try again.", fg="red")

def manage_travelers():
    click.secho("\n----- Manage Travelers -----", fg="cyan")
    click.secho("1. Add Traveler", fg="green")
    click.secho("2. View Travelers", fg="green")
    click.secho("3. Get Traveler", fg="green")
    click.secho("4. Delete Traveler", fg="green")
    click.secho("5. Back to Main Menu", fg="yellow")

    choice = click.prompt("Enter your choice", type=int)

    if choice == 1:
        add_traveler()
    elif choice == 2:
        list_travelers()
    elif choice == 3:
        get_traveler()
    elif choice == 4:
        delete_traveler()

def manage_trips():
    click.secho("\n----- Manage Trips -----", fg="cyan")
    click.secho("1. Add Trip", fg="green")
    click.secho("2. View Trips", fg="green")
    click.secho("3. Get Trip", fg="green")
    click.secho("4. Delete Trip", fg="green")
    click.secho("5. Back to Main Menu", fg="yellow")

    choice = click.prompt("Enter your choice", type=int)

    if choice == 1:
        add_trip()
    elif choice == 2:
        list_trips()
    elif choice == 3:
        get_trip()
    elif choice == 4:
        delete_trip()

def manage_bookings():
    click.secho("\n----- Manage Bookings -----", fg="cyan")
    click.secho("1. Add Booking", fg="green")
    click.secho("2. View Bookings ", fg="green")
    click.secho("3. Get Traveler Bookings", fg="green")
    click.secho("4. Get Trip Bookings", fg="green")
    click.secho("5. Cancel Bookings", fg="yellow")

    choice = click.prompt("Enter your choice", type=int)

    if choice == 1:
        add_booking()
    elif choice == 2:
        list_bookings()
    elif choice == 3:
        get_traveler_bookings()
    elif choice == 4:
        get_trip_bookings()
    elif choice == 5:
        cancel_booking()
    else:
        click.secho("Invalid Choice. Try again.", fg="red")

if __name__ == "__main__":
    menu()



