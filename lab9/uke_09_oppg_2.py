def mase_for_is():
    print("Kan jeg få en is?")
    while True:
        answer = input()
        if answer != "ja":
            print("Vær så snill, si ja!")
            continue

        return "Tusen takk!"
        
print(mase_for_is())