#ROOM 1

import random

PIN = f"{random.randint(0,9999):04d}"
pin = False
desk_key = False
key=False
while True:
    print("\nGAME MENU:\n")
    print("1. Open exit door")
    print("2. Open safe")
    print("3. Open desk drawer")
    print("4. Look around")

    ch1 = input("\nEnter your choice: ")
    
    if ch1 == "1":
        if not key:
            print("I need a key to unlock it!")
        else:
            print("Unlocked the door!")
            print("Escaped Room Successfully!!!")
            break

    elif ch1 == "2":
        if pin and not key:
            user_PIN = input("Please enter the PIN: ")

            if PIN == user_PIN:
                print("Unlocked Safe. Received a key")
                key = True
            else:
                print("Invalid PIN")
                
        elif key:
            print("Safe is already unlocked")
        else:
            print("I don't know the code!")

    elif ch1 == "3":
        if desk_key and not pin:
            print(f"Found a piece of card with a 4-digit number on it. The number is {PIN}")
            pin = True
        elif pin:
            print("The desk is already unlocked")
        else:
            print("Looks like the desk is locked")

    elif ch1=='4':
        if not desk_key:
            print("Found a desk key")
            desk_key=True
        else:
            print("Nothing useful here")

    else:
        print("Invalid option")

