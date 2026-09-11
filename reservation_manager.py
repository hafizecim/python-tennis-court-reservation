import json
from reservation import Reservation

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

    def save_to_file(self):
        data = []

        for reservation in self.reservations:
            data.append({
                "name": reservation.name,
                "date": reservation.date,
                "time": reservation.time,
                "player_count": reservation.player_count
            })

        with open("reservations.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Reservations saved.")


    def load_from_file(self):
        try:
            with open("reservations.json", "r") as file:
                data = json.load(file)

            for item in data:
                reservation = Reservation(
                    item["name"],
                    item["date"],
                    item["time"],
                    item["player_count"]
                )

                self.reservations.append(reservation)

            print("Reservations loaded.")

        except FileNotFoundError:
            print("Reservation file not found.")