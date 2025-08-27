from database import SessionLocal
from models import Traveler

def add_traveler(name, email, phone, passport_number):
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
    return traveler

def list_travelers():
    session = SessionLocal()
    travelers = session.query(Traveler).all()
    session.close()
    return travelers

def get_traveler(traveler_id):
    session = SessionLocal()
    traveler = session.query(Traveler).filter_by(id=traveler_id).first()
    session.close()
    return traveler

def delete_traveler(traveler_id):
    session = SessionLocal()
    traveler = session.query(Traveler).filter_by(id=traveler_id).first()
    if traveler:
        session.delete(traveler)
        session.commit()
        result = True
    else:
        result = False
    session.close()
    return result
