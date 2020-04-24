order = ""
started = False
while order != "quit":
    order = input(" > ").lower()
    if order == "start":
        if started:
            print("Car is already started...")
        else:
            started = True
            print("Car started...Ready to go!")
    elif order == "stop":
        if not started:
            print("Car is already stopped !")
        else:
            started = False
            print("Car stopped")
    elif order == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif order == "quit":
        break
    else:
        print("Sorry,I don't understand that!")