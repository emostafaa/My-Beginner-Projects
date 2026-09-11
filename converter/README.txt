========================================
CONVERTER - TUI VERSION
========================================

A simple terminal-based unit converter written in Python.
Convert between temperature, data, and distance units
through an interactive text menu.


----------------------------------------
FEATURES
----------------------------------------

- Temperature: Celsius <-> Fahrenheit
- Data: KB <-> MB, MB <-> GB, GB <-> KB, KB <-> Bytes
- Distance: mm <-> cm, cm <-> m, m <-> km
- Cross-platform screen clearing (Windows / Linux / macOS)
- Input validation - rejects non-numeric input and re-prompts
- Timed feedback so results and errors are readable before
  the screen clears


----------------------------------------
REQUIREMENTS
----------------------------------------

- Python 3.10 or newer (uses match/case)
- Standard library only - no external packages


----------------------------------------
INSTALLATION
----------------------------------------

Just download the file:

    git clone <your-repo-url>
    cd <your-repo>

Or save the script as convert.py.


----------------------------------------
USAGE
----------------------------------------

Run it with Python:

    python3 convert.py

You'll see a main menu:

    1. Temperatures
    2. Data
    3. distance
    4. exit
    enter a choice:

Type the number of a category and press Enter.


TEMPERATURE MENU
----------------
    1. from celcius to fahrenheit
    2. from fahrenheit to celcius
    0. back


DATA MENU
---------
    1. from kilobyte to megabyte
    2. from megabyte to kilobyte
    3. from megabyte to gigabyte
    4. from gigabyte to megabyte
    5. from gigabyte to kilobyte
    6. from kilobyte to byte
    0. back


DISTANCE MENU
-------------
    1. from millimeter to centimeter
    2. from centimeter to meter
    3. from meter to kilometer
    4. from kilometer to meter
    5. from meter to centimeter
    6. from centimeter to millimeter
    0. back


After picking a conversion, enter the value and the
result is printed. Press Enter to return to the menu.


----------------------------------------
EXAMPLE
----------------------------------------

    1. Temperatures
    2. Data
    3. distance
    4. exit
    enter a choice: 1

    1. from celcius to fahrenheit
    2. from fahrenheit to celcius
    0. back
    enter a choice: 1
    enter degree in celcius: 100
    100 degress celcius equals 212 fahrenheit


----------------------------------------
PROJECT STRUCTURE
----------------------------------------

    convert.py
    |
    +-- convert
    |   +-- temp        # temperature conversions
    |   +-- data        # data size conversions
    |   +-- distance    # distance conversions
    |
    +-- if __name__ == "__main__"
        +-- convert.print_converters()

Each conversion is a static method on its sub-class, e.g.:

    convert.temp.fromcelciustofahrenheit()
    convert.data.fromkbtomb()
    convert.distance.frommtokm()


----------------------------------------
ERROR HANDLING
----------------------------------------

- Non-numeric input  ->  "please enter a number"  (re-prompts)
- Invalid menu choice ->  "invalid option"         (re-displays menu)
- Empty input         ->  treated as invalid

All error messages pause for 1.5 seconds before the screen
clears so you can read them.


----------------------------------------
PLATFORM NOTES
----------------------------------------

- Linux / macOS:  uses 'clear'
- Windows:        uses 'cls'

The script auto-detects the platform:

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


----------------------------------------
KNOWN LIMITATIONS
----------------------------------------

- Integer input only (no decimals)
- Data conversions use 1024 (binary/KiB), not 1000 (decimal/KB)
- No history or batch conversion


----------------------------------------
LICENSE
----------------------------------------

MIT - free to use, modify, and share.


========================================
This README was written by AI (DeepSeek).
========================================
