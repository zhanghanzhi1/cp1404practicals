from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_cost = 0.0

    print("Let's drive!")
    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()
        if choice == 'q':
            print(f"Total trip cost: ${total_cost:.2f}")
            print("Taxis are now:")
            list_taxis(taxis)
            break
        elif choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if current_taxi:
                total_cost += drive_taxi(current_taxi)
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")


def list_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    list_taxis(taxis)
    try:
        choice = int(input("Choose taxi: "))
        return taxis[choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


def drive_taxi(taxi):
    distance = float(input("Drive how far? "))
    cost = taxi.drive(distance)
    print(f"Your {taxi.name} trip cost you ${cost:.2f}")
    return cost


if __name__ == '__main__':
    main()
