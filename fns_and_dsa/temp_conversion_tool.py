# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    # We're only reading the global variable, so no need for global keyword
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    # We're only reading the global variable, so no need for global keyword
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Get temperature input
    temp_input = input("Enter the temperature to convert: ")
    try:
        temperature = float(temp_input)
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Get unit input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    while unit not in ('C', 'F'):
        print("Invalid unit. Please enter either 'C' or 'F'.")
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    # Perform conversion
    if unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    else:
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")

if __name__ == "__main__":
    main()