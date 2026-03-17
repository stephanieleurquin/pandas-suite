def calculate_room_price(room_type, nights):
    """Calcule le prix total pour une chambre et nombre de nuits."""
    prices = {"single": 60, "double": 100, "triple": 120}
    room_type = room_type.lower()
    if room_type not in prices:
        return None
    total = prices[room_type] * nights
    if nights >= 5:
        total *= 0.9
    return total
print("Welcome to StayFab Smart Assistant!")
print("[LIMITED TIME OFFER] 10% off if you will reserve 5 nights or more!")

while True:
    room_type = input("1- Enter room type (Single, Double, Triple): ")

    if room_type.lower() not in ["single", "double", "triple"]:
        print("Invalid room type. Please choose Single, Double, or Triple.")
        continue

    while True:
        try:
            nights = int(input("2- How many number of nights? "))
            if nights < 1:
                print("Invalid number of nights. Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    total_price = calculate_room_price(room_type, nights)

    if nights >= 5:
        print(f"Total price for a {room_type.capitalize()} room for {nights} night(s): ${total_price} (10% off applied!)")
    else:
        print(f"Total price for a {room_type.capitalize()} room for {nights} night(s): ${total_price} (No discount applied)")
