import json
from pprint import pprint

class Venue:
    def __init__(self, venue_id: str, name: str, location: str, capacity: int):
        self.venue_id = venue_id
        self.name = name
        self.location = location
        self.capacity = capacity

class Event:
    def __init__(self, event_id: str, name: str, date: str, venue_id: str):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.venue_id = venue_id

class Customer:
    def __init__(self, customer_id: str, name: str, email: str, phone: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone

class Ticket:
    def __init__(self, ticket_id: str, event_id: str, seat_number: str, price: float, customer_id: str):
        self.ticket_id = ticket_id
        self.event_id = event_id
        self.seat_number = seat_number
        self.price = price
        self.customer_id = customer_id

class Booking:
    def __init__(self, booking_id: str, ticket_id: str, booking_date: str, status: str):
        self.booking_id = booking_id
        self.ticket_id = ticket_id
        self.booking_date = booking_date
        self.status = status

class Payment:
    def __init__(self, payment_id: str, booking_id: str, amount: float, payment_date: str, method: str):
        self.payment_id = payment_id
        self.booking_id = booking_id
        self.amount = amount
        self.payment_date = payment_date
        self.method = method

with open('event.json', 'r', encoding='utf8') as f:
    text = json.load(f)
    pprint(text)
