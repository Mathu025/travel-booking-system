from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship 
from.database import Base

class Traveler(Base):
    __tablename__ = "travelers"

    id = Column(Integer, primary_key=True, index=True)
    name= Column(String, nullable=False)
    email= Column(String, unique=True, nullable=False)
    phone= Column(String)
    passport_number = Column(String, unique=True, nullable=False)

    bookings = relationship("Booking", back_populates="traveler")