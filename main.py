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

# Создание объектов
venue = Venue("V001", "Concert Hall", "New York", 5000)
event = Event("E001", "Rock Concert", "2024-11-20", "V001")
customer = Customer("C001", "John Doe", "john.doe@example.com", "123-456-7890")
ticket = Ticket("T001", "E001", "A1", 100.0, "C001")
booking = Booking("B001", "T001", "2024-10-25", "Confirmed")
payment = Payment("P001", "B001", 100.0, "2024-10-25", "Credit Card")

# Сериализация объектов в словарь
data = {
    "venue": vars(venue),
    "event": vars(event),
    "customer": vars(customer),
    "ticket": vars(ticket),
    "booking": vars(booking),
    "payment": vars(payment)
}

# Запись и чтение данных в/из JSON
#with open('event.json', 'w', encoding='utf8') as f:
#    json.dump(data, f, ensure_ascii=False, indent=4)

with open('event.json', 'r', encoding='utf8') as f:
    text = json.load(f)
    pprint(text)