import json
from json import JSONDecodeError
from pprint import pprint

class Venue:
    def __init__(self, venue_id: str, name: str, location: str, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity должно быть положительным целым числом.")
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
        if price < 0:
            raise ValueError("Price должна быть положительным числом.")
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
        if amount < 0:
            raise ValueError("Amount должна быть положительным числом.")
        self.payment_id = payment_id
        self.booking_id = booking_id
        self.amount = amount
        self.payment_date = payment_date
        self.method = method

# Выгрузка инфы из старого файла
filename = 'Event.json'

def load_data(filename):
    try:
        with open(filename, 'r', encoding='utf8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл не найден.")
        return {}
    except JSONDecodeError:
        print("Ошибка декодирования JSON.")
        return {}

old_data = load_data(filename)

# Создание объектов
venue = Venue("V001", "Concert Hall", "New York", 6000)
event = Event("E001", "Rock Concert", "2024-11-20", "V001")
customer = Customer("C001", "John Doe", "john.doe@example.com", "123-456-7890")
ticket = Ticket("T001", "E001", "A1", 100.0, "C001")
booking = Booking("B001", "T001", "2024-10-25", "Confirmed")
payment = Payment("P001", "B001", 100.0, "2024-10-25", "Credit Card")

# Сериализация объектов в словарь
new_data = {
    "venues": vars(venue),
    "events": vars(event),
    "customers": vars(customer),
    "tickets": vars(ticket),
    "bookings": vars(booking),
    "payments": vars(payment)
}

# Объединение информации
def add_data(old_data, new_data):
    for key in old_data.keys():
        if key in new_data:
            old_data[key].append(new_data[key])

add_data(old_data, new_data)

# Запись и чтение данных в/из JSON
new_filename = 'Event2.json'

try:
    with open(new_filename, 'w', encoding='utf8') as f:
        json.dump(old_data, f, ensure_ascii=False, indent=2)
except IOError:
    print("Ошибка записи в файл.")

try:
    with open(new_filename, 'r', encoding='utf8') as f:
        text = json.load(f)
        pprint(text)
except FileNotFoundError:
    print("Файл для чтения не найден.")
except IOError:
    print("Ошибка чтения файла.")
except JSONDecodeError:
    print("Ошибка JSON.")