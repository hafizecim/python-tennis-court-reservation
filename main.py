
from colorama import Fore, Style, init

from reservation import Reservation
from reservation_manager import ReservationManager


init(autoreset=True)

manager = ReservationManager()
manager.load_from_file()


while True:
    print()
    print(Fore.CYAN + "===== 🎾 Tennis Court Reservation System 🎾 =====")
    print(Fore.MAGENTA + "1 - ➕ Add Reservation")
    print(Fore.MAGENTA + "2 - 📋 List Reservations")
    print(Fore.MAGENTA + "3 - 🔍 Search Reservation")
    print(Fore.MAGENTA + "4 - 🗑️  Delete Reservation")
    print(Fore.MAGENTA + "5 - 📊 Reservation Report")
    print(Fore.MAGENTA + "0 - 🚪 Exit")

    choice = input(Fore.YELLOW + "Choose an option: ")

    if choice == "1":
        name = input("Name: ")
        date = input("Date (YYYY-MM-DD): ")
        time = input("Time (HH:MM): ")

        if name == "" or date == "" or time == "":
            print(Fore.RED + " ❌ Name, date and time cannot be empty.")
            continue

        try:
            player_count = int(input("Player count (1-4): "))

            if player_count < 1 or player_count > 4:
                print(Fore.RED + " ❌ Player count must be between 1 and 4.")
                continue

        except ValueError:
            print(Fore.RED + " ❌ Please enter a number.")
            continue

        reservation = Reservation(
            name,
            date,
            time,
            player_count
        )

        manager.add_reservation(reservation)
        manager.save_to_file()

        print(Fore.GREEN + "✅ Reservation added.")

    elif choice == "2":
        print()
        print(Fore.CYAN + "Reservations:")
        manager.list_reservations()

    elif choice == "3":
        keyword = input(Fore.YELLOW + " ⚠️ Enter name or date: ")
        manager.search_reservations(keyword)

    elif choice == "4":
        name = input(Fore.YELLOW + " ⚠️ Enter the name to delete: ")
        manager.delete_reservation(name)
        manager.save_to_file()

    elif choice == "5":
        manager.show_report()

    elif choice == "0":
        print(Fore.GREEN + "👋 Goodbye!")
        break

    else:
        print(Fore.RED + "❌ Invalid choice.")
