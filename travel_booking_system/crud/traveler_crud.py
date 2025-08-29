from database import SessionLocal
from models import Traveler
import click

def add_traveler():
    name = click.prompt("Enter traveler name")
    email = click.prompt("Enter traveler email")
    phone = click.prompt("Enter traveler phone")
    passport_number = click.prompt("Enter passport number")

    session = SessionLocal()
    traveler = Traveler(
        name=name,
        email=email,
        phone=phone,
        passport_number=passport_number
    )
    session.add(traveler)
    session.commit()
    session.close()
    click.secho(f"Traveler {name} added successfully!\n", fg="green")
    return traveler

def list_travelers():
    session = SessionLocal()
    travelers = session.query(Traveler).all()
    session.close()

    click.secho("Travelers:", fg="cyan")
    for t in travelers:
        click.echo(f"{t.id}. {t.name} ({t.email}), {t.phone}")
    return travelers

def get_traveler():
    traveler_id = click.prompt("Enter traveler ID", type=int)
    session = SessionLocal()
    traveler = session.query(Traveler).filter_by(id=traveler_id).first()
    session.close()

    click.secho(f"Traveler {traveler.id}: {traveler.name} {traveler.email}", fg="cyan")

    return traveler

def delete_traveler():
    traveler_id = click.prompt("Enter traveler ID to delete", type=int)
    session = SessionLocal()
    traveler = session.query(Traveler).filter_by(id=traveler_id).first()

    session.delete(traveler)
    session.commit()
    session.close()
    click.secho(f"Traveler '{traveler.name}' deleted successfully!", fg="green")
