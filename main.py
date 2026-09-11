from reservation import Reservation
from reservation_manager import ReservationManager


manager = ReservationManager()

reservation1 = Reservation("Ahmet", "2026-09-12", "18:00", 2)
reservation2 = Reservation("Ayşe", "2026-09-13", "19:00", 4)

manager.add_reservation(reservation1)
manager.add_reservation(reservation2)

print("Before delete:")
manager.list_reservations()

manager.delete_reservation("Ahmet")

print("After delete:")
manager.list_reservations()