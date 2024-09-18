"""Conversion of temperature from celsius to fahrenheit , fahrenheit to celsius"""

# Fahrenheit=(celsius*1.8)+32

# celsius = int(input("Enter the temperature in celsius:"))
# Fahrenheit = (celsius * 1.8) + 32
# print(f"The temperature in fahrenheit is {round(Fahrenheit, 3)}")


# Celsius=(Fahrenheit-32)/1.8

Fahrenheit = float(input("Enter the temperature in fahrenheit:"))
Celsius = (Fahrenheit - 32) / 1.8
print(f"The temperature in Celsius is {round(Celsius, 3)}")
