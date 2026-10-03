rooms = {
    "A": input("Enter status of Room A (Clean/Dirty): ").capitalize(),
    "B": input("Enter status of Room B (Clean/Dirty): ").capitalize()
}

location = input("Enter vacuum location (A/B): ").upper()

print("\n--- Vacuum Cleaner ---")

while rooms["A"] == "Dirty" or rooms["B"] == "Dirty":

    print("\nCurrent Location:", location)
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])

    # Simple Reflex Action
    if rooms[location] == "Dirty":
        print("Action: SUCK")
        rooms[location] = "Clean"

    # Move to other room
    elif location == "A":
        print("Action: MOVE RIGHT")
        location = "B"

    else:
        print("Action: MOVE LEFT")
        location = "A"

print("\nRoom A: Clean")
print("Room B: Clean")
print("Goal Achieved! Both rooms are clean.")
