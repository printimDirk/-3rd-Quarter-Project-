list = {
    1: 'inches to centimeters',
    2: 'centimeters to inches',
    3: 'feet to meters',
    4: 'meters to feet',
    5: 'yards to meters',
    6: 'meters to yards',
    7: 'miles to kilometers',
    8: 'kilometers to miles',
    9: 'pounds to kilograms',
    10: 'kilograms to pounds',
    11: 'km/h to mph',
    12: 'mph to km/h',
    13: 'celsius to fahrenheit',
    14: 'fahrenheit to celsius',
    15: 'liters to gallons',
    16: 'gallons to liters',
    17: 'ounces to grams',
    18: 'grams to ounces',
    19: 'calories to joules',
    20: 'joules to calories'
}

print('\nHello this program is a way to convert measuremnts from unit to another unit')
print('To choose what you want to convert, just type the number from 1 to 20, and to exit, type 21')
   
choice = int(input("\nEnter the number of the conversion you want: "))


if choice in list:
    print(f"You chose: {list[choice]}")

    value = float(input("Enter the value to convert: "))

    if choice == 1:  # inches to centimeters
        result = value * 2.54
    elif choice == 2:  # centimeters to inches
        result = (value / 2.54)
    elif choice == 3:  # feet to meters
        result = value * 0.3048
    elif choice == 4:  # meters to feet
        result = value / 0.3048
    elif choice == 5:  # yards to meters
        result = value * 0.9144
    elif choice == 6:  # meters to yards
        result = value / 0.9144
    elif choice == 7:  # miles to kilometers
        result = value * 1.60934
    elif choice == 8:  # kilometers to miles
        result = value / 1.60934
    elif choice == 9:  # pounds to kilograms
        result = value * 0.453592
    elif choice == 10:  # kilograms to pounds
        result = value / 0.453592
    elif choice == 11:  # km/h to mph
        result = value * 0.621371
    elif choice == 12:  # mph to km/h
        result = value / 0.621371
    elif choice == 13:  # celsius to fahrenheit
        result = (value * 9 / 5) + 32
    elif choice == 14:  # fahrenheit to celsius
        result = (value - 32) * 5 / 9
    elif choice == 15:  # liters to gallons
        result = value * 0.264172
    elif choice == 16:  # gallons to liters
        result = value / 0.264172
    elif choice == 17:  # ounces to grams
        result = value * 28.3495
    elif choice == 18:  # grams to ounces
        result = value / 28.3495
    elif choice == 19:  # calories to joules
        result = value * 4.184
    elif choice == 20:  # joules to calories
        result = value / 4.184
    
    print("Result:", round(result, 2))

elif choice == 21:
    print("Thank you for using this app!")
    breakpoint
else:
    print("Invalid choice. Please enter a number from 1 to 20.")


