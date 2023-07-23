def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    try:
        temperature = float(input("Enter temperature value: "))
        unit = input("Enter unit of measurement (C for Celsius, F for Fahrenheit): ").upper()

        if unit == 'C':
            fahrenheit = celsius_to_fahrenheit(temperature)
            print(f"{temperature:.2f}°C is equal to {fahrenheit:.2f}°F.")
        elif unit == 'F':
            celsius = fahrenheit_to_celsius(temperature)
            print(f"{temperature:.2f}°F is equal to {celsius:.2f}°C.")
        else:
            print("Invalid unit of measurement. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid input. Please enter a valid temperature value.")

if __name__ == "__main__":
    main()
