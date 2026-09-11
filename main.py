from reservation import Reservation
from reservation_manager import ReservationManager


manager = ReservationManager()

reservation1 = Reservation("Ahmet", "2026-09-12", "18:00", 2)
reservation2 = Reservation("Ayşe", "2026-09-13", "19:00", 4)

manager.add_reservation(reservation1)
manager.add_reservation(reservation2)

manager.list_reservations()