def spise_sammen():
    print("Meny")
    print()
    print("1. Stekt uer med blomkålpuré.")
    print("2. Piggvarfilet med ertepuré.")
    print("3. Boknatorsk med kremstuede.")
    print("4. Steinbit, sjøkreps og snøkrabbe.")
    print("5. Norske oster med marmelade.")
    print()
    print(f"Hvilket nummer vil du bestille?", end=" ")
    i = int(input())
    while True:
        if i == 1:
            meny = "Stekt uer med blomkålpuré"
            return f'{meny} kommer straks!'
        if i == 2:
            meny = "Piggvarfilet med ertepuré"
            return f'{meny} kommer straks!'
        if i == 3:
            meny = "Boknatorsk med kremstuede"
            return f'{meny} kommer straks!'
        if i == 4:
            meny = "Steinbit, sjøkreps og snøkrabbe"
            return f'{meny} kommer straks!'
        if i == 5:
            meny = "Norske oster med marmelade"
            return f'{meny} kommer straks!'
        else:
            return("Beklager, det er ikke et gyldig valg!")


print(spise_sammen())
