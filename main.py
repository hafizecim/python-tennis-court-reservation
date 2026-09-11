from reservation import Reservation
from reservation_manager import ReservationManager


manager = ReservationManager()

reservation = Reservation("Ahmet", "2026-09-12", "18:00", 2)

manager.add_reservation(reservation)

print(manager.reservations[0].name)
print(manager.reservations[0].date)
print(manager.reservations[0].time)
print(manager.reservations[0].player_count)