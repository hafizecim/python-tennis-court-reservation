from reservation import Reservation
from reservation_manager import ReservationManager


manager = ReservationManager()
manager.load_from_file()


while True:
    print()
    print("===== Tennis Court Reservation System =====")
    print("1 - Add Reservation")
    print("2 - List Reservations")
    print("3 - Search Reservation")
    print("4 - Delete Reservation")
    print("5 - Reservation Report")
    print("0 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        date = input("Date (YYYY-MM-DD): ")
        time = input("Time (HH:MM): ")

        if name == "" or date == "" or time == "":
            print("Name, date and time cannot be empty.")
            continue

        try:
            player_count = int(input("Player count (1-4): "))

            if player_count < 1 or player_count > 4:
                print("Player count must be between 1 and 4.")
                continue

        except ValueError:
            print("Please enter a number.")
            continue

        reservation = Reservation(
            name,
            date,
            time,
            player_count
        )

        manager.add_reservation(reservation)
        manager.save_to_file()

        print("Reservation added.")

    elif choice == "2":
        print()
        print("Reservations:")
        manager.list_reservations()

    elif choice == "3":
        keyword = input("Enter name or date: ")
        manager.search_reservations(keyword)

    elif choice == "4":
        name = input("Enter the name to delete: ")
        manager.delete_reservation(name)
        manager.save_to_file()
    
    elif choice == "5":
        manager.show_report()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")