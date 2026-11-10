# Temperature Monitor and Alarm Checker

## What it does
This Python program takes 5 temperature readings from a machine and stores them in a list. It prints the highest, lowest and average reading, then checks every reading against a safe limit and warns if any are too high.

## How to run it
Install Python 3, then run: python temperature_monitor.py

## Sample output
```
=== Machine Temperature Monitor ===
Enter the safe temperature limit for this machine (°C): 80
Enter reading 1 of 5 (°C): 75.5
Enter reading 2 of 5 (°C): 80
Enter reading 3 of 5 (°C): 82
Enter reading 4 of 5 (°C): 90
Enter reading 5 of 5 (°C): 60

--- Results ---
Readings: [75.5, 80.0, 82.0, 90.0, 60.0]
Highest: 90.0 °C
Lowest: 60.0 °C
Average: 77.5 °C

--- Alarm check (safe limit: 80.0 °C) ---
OK: Reading 1 (75.5 °C) is safe.
Caution: Reading 2 (80.0 °C) is exactly at the limit.
WARNING: Reading 3 (82.0 °C) is above the safe limit!
WARNING: Reading 4 (90.0 °C) is above the safe limit!
OK: Reading 5 (60.0 °C) is safe.

ALARM: 2 reading(s) went above the safe limit. Check the machine!
```

## My own twist
The user sets the safe temperature limit themselves, so the program works for any machine and not just one fixed limit.

## What I learned
I learned how to use a loop to keep asking until the user types a valid number, and how try/except stops the program from crashing when someone types letters instead of numbers. I also learned that testing with numbers I can work out by hand is the best way to check my code is correct.

## Author
Adedayo Rehoboth Oluwademilade, ND1 Mechatronics Engineering, YabaTech.
