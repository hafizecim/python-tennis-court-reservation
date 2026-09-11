from reservation_manager import ReservationManager


manager = ReservationManager()

manager.load_from_file()

print("Loaded reservations:")
manager.list_reservations()