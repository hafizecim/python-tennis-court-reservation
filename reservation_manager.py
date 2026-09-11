class ReservationManager:
    def __init__(self):
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def list_reservations(self):
        for reservation in self.reservations:
            print(
                reservation.name,
                reservation.date,
                reservation.time,
                reservation.player_count
            )

    def delete_reservation(self, name):
        for reservation in self.reservations:
            if reservation.name == name:
                self.reservations.remove(reservation)
                print("Reservation deleted.")
                return

        print("Reservation not found.")

    def search_reservations(self, keyword):
        found = False

        for reservation in self.reservations:
            if reservation.name == keyword or reservation.date == keyword:
                print(
                    reservation.name,
                    reservation.date,
                    reservation.time,
                    reservation.player_count
                )
                found = True

        if not found:
            print("Reservation not found.")