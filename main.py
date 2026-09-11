from reservation import Reservation
from reservation_manager import ReservationManager


manager = ReservationManager()

reservation1 = Reservation("Ahmet", "2026-09-12", "18:00", 2)
reservation2 = Reservation("Ayşe", "2026-09-13", "19:00", 4)
reservation3 = Reservation("Ahmet", "2026-09-15", "20:00", 2)

manager.add_reservation(reservation1)
manager.add_reservation(reservation2)
manager.add_reservation(reservation3)

print("Search by name:")
manager.search_reservations("Ahmet")

print("Search by date:")
manager.search_reservations("2026-09-13")