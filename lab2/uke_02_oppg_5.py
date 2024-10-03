#oppgave 5a
def wavelength_to_color(x):
    if 380 < x <= 450:
        return "Violet"
    elif 450 < x <= 485:
        return "Blue"
    elif 485 < x <= 500:
        return "Cyan"
    elif 500 < x <= 565:
        return "Green"
    elif 565 < x <= 590:
        return "Yellow"
    elif 590 < x <= 625:
        return "Orange"
    elif 625 < x <= 750:
        return "Red"
print(wavelength_to_color(565))
print(wavelength_to_color(400))
print(wavelength_to_color(6500))

print()

#oppgave 5b
def frequency_to_color(y):
    # Regner om Hz til meter
    x = (3e8 / (y * 10**12)) * 10**9
    return wavelength_to_color(x)
print(frequency_to_color(610))
print(frequency_to_color(450))
print(frequency_to_color(1.5e-2))

print()

#oppgave 5C
def frequency_or_wavelength_to_color():
    print("Enter a unit (nm or THz):")
    unit = input()
    if unit == "nm":
        print("Enter a value in nm:")
        value = int(input())
        if 380 <= value <= 750:
            print()
            print(wavelength_to_color(value))
        else:
            print()
            print("There is no color with wavelength " + str(value) + " nm")
    elif unit == "THz":
        print("Enter a value in THz:")
        value = int(input())
        if 400 <= value <= 790:
            print()
            print(frequency_to_color(value))
        else:
            print()
            print("There is no color with frequency " + str(value) + " THz")
    else:
        print()
        print("The unit must be either nm or THz, it can not be " + unit)

frequency_or_wavelength_to_color()