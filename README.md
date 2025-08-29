# TRAVEL BOOKING SYSTEM

** By Mathu Alex **

- A simple **CLI-Based Travel Booking system** built with **Python**, **Click** and **SQLALCHEMY**, with database migrations handled via **Alembic**. 
- It allows you to manage travelers, trips and bookings through an interactive command-line interface.


## Table of Contents

- Features

- Technologies Used

- Data Schema

- Links

- Setup Instructions

- Support and Contact details

- License

## Features

### 1. Manage Travelers

- Add a new traveler
- List all travelers
- View details of a specific traveler
- Delete a traveler

### 2. Manage Trips

- Add a new trip
- List all trips
- View details of a specific trip
- Delete a trip

### Manage Bookings

- Add a new booking for a traveler and trip
- View all bookings
- Get bookings by a traveler
- Get bookings by trip
- Cancel a booking

## Technologies Used

- Python 3.12.3
- Click for CLI interaction
- SQLAlchemy for ORM and database management
- Alembic for migrations

## Data Schema

### Entities

1. Traveler

        id (PK)

        name (string)

        mail (string, unique)

        phone (string)

        passport_number (string, unique)

2. Trip

        id (PK)

        destination (string)

        start_date (date)

        end_date (date)

        capacity (integer)

3. Booking

        id (PK)

        traveler_id (FK → Traveler.id)

        trip_id (FK → Trip.id)

        booking_date (date)

        status (string, e.g., Confirmed, Cancelled)

Relationships:

One Traveler can have many Bookings.

One Trip can have many Bookings.

## Links

- Repository Link: https://github.com/Mathu025/travel-booking-system


## Setup Instructions

- Follow these steps to get the project running on your local machine.

### Clone this repo

- git clone <https://github.com/Mathu025/travel-booking-system>

- Press Code . if opened from external terminal to open in VS Code.

### Create a virtual env and install dependencies

- python -m venv venv
- source venv/bin/activate   # Linux/macOS
- venv\Scripts\activate      # Windows
- pip install -r requirements.txt

### Seed the database

- python seed.py

### Run the interactive menu

- python main.py

## Support and Contact Details

If you have any questions, suggestions, or need assistance, please contact:

- Email: <mathualex72@gmail.com>

## License

MIT License

Copyright &copy; Mathu Alex.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.