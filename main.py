class Venue:
    id: str
    name: str
    location: str
    capacity: int

class Event:
    id: str
    name: str
    date: str
    venue_id: str

class Customer:
    id: str
    name: str
    email: str
    phone: str

class Ticket:
    id: str
    event_id: str
    seat_number: str
    price: float
    customer_id: str

class Booking:
    id: str
    ticket_id: str
    booking_date: str
    status: str

class Payment:
    id: str
    booking_id: str
    amount: float
    payment_date: str
    method: str

