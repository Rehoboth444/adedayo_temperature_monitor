# Temperature Monitor and Alarm Checker
# This program takes 5 temperature readings from a machine, stores them in a list,
# prints the highest, lowest and average, and warns if any reading is above a safe limit.
# My own twist: the user sets the safe limit themselves, so it works for any machine.

NUMBER_OF_READINGS = 5  # how many readings we collect


def get_number(prompt):
    """Keep asking until the user types a valid number, then return it as a float."""
    while True:  # loop repeats until we get a good answer
        text = input(prompt)
        try:
            return float(text)  # convert the typed text to a decimal number
        except ValueError:
            # This runs if the user typed letters or symbols instead of a number
            print("That is not a number. Please type digits only, for example 72.5")


def main():
    print("=== Machine Temperature Monitor ===")

    # Twist: the user decides what temperature is safe for their machine
    safe_limit = get_number("Enter the safe temperature limit for this machine (°C): ")

    # Collect the readings and store them in a list
    readings = []
    for number in range(1, NUMBER_OF_READINGS + 1):
        value = get_number(f"Enter reading {number} of {NUMBER_OF_READINGS} (°C): ")
        readings.append(value)

    # Work out the highest, lowest and average
    highest = max(readings)
    lowest = min(readings)
    average = sum(readings) / len(readings)

    print("\n--- Results ---")
    print(f"Readings: {readings}")
    print(f"Highest: {highest:.1f} °C")
    print(f"Lowest: {lowest:.1f} °C")
    print(f"Average: {average:.1f} °C")

    # Check every reading against the safe limit
    print(f"\n--- Alarm check (safe limit: {safe_limit:.1f} °C) ---")
    warnings = 0
    for number, reading in enumerate(readings, start=1):
        if reading > safe_limit:
            print(f"WARNING: Reading {number} ({reading:.1f} °C) is above the safe limit!")
            warnings += 1
        elif reading == safe_limit:
            print(f"Caution: Reading {number} ({reading:.1f} °C) is exactly at the limit.")
        else:
            print(f"OK: Reading {number} ({reading:.1f} °C) is safe.")

    # Final summary message
    if warnings > 0:
        print(f"\nALARM: {warnings} reading(s) went above the safe limit. Check the machine!")
    else:
        print("\nAll readings are within the safe limit. Machine is running normally.")


# Run the program
main()
