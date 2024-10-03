def dummy_chatbot():
    while True:
        print("Hi! Do you want to talk to me?")
        answer = input()
        if answer != "no":
            print("That's cool!")
            continue
        print("All right, bye!")
        return

dummy_chatbot()