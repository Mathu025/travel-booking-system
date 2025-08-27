from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship 
from.database import Base

class Traveler(Base):
    __tablename__ = "travelers"

    id = Column(Integer, primary_key=True)
    name= Column(String, nullable=False)
    email= Column(String, unique=True, nullable=False)
    phone= Column(String)
    passport_number = Column(String, unique=True, nullable=False)

    bookings = relationship("Booking", back_populates="traveler")

class Trip(Base):
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True)
    destination = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    capacity = Column(Integer, nullable=False)

    bookings = relationship("Booking", back_populates="trip")

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    traveler_id = Column(Integer, ForeignKey("travelers.id"))
    trip_id = Column(Integer, ForeignKey("trips.id"))
    booking_date = Column(Date, nullable=False)
    status = Column(String, default="Confirmed")

    traveler = relationship("Traveler", back_populates="bookings")
    trip = relationship("Trip", back_populates="bookings")

