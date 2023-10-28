# Exercise 1
number_01 = 50
number_02 = 25.50
spacer = "- - - - - - - - - - - - - - - - - - - "  * 2

print(spacer)
print("\t\t\t[ EXERCISE 1 ]\n")
print("[1]", number_01 + number_02, "\t", f"type: addition \t data type: {type(number_01 + number_02)}")
print("[2]", number_01 - number_02, "\t", f"type: subtraction \t data type: {type(number_01 + number_02)}")
print("[3]", number_01 * number_02, "\t", f"type: multiplication \t data type: {type(number_01 + number_02)}")
print("[4]", "{:.3f}".format(number_01 / number_02), "\t", f"type: division \t data type: {type(number_01 + number_02)}")
print("[5]", number_01 + int(number_02), "\t\t", f"type: conversion \t data type: {type(number_01 + number_02)}")
print(spacer)

#Exercise 2
print(spacer)
print("\t\t\t[ EXERCISE 2 ]\n")
dmu_module = "In this lab exercise of DMU module, we will manipulate strings in Python."
print(f"[1]", (dmu_module))
print("[2] length:", len(dmu_module))
print(f"[3] {dmu_module.upper()}")
print(f"[4]", (dmu_module))
print(f"[5]", (dmu_module.strip()))
print(f"[6] Starts with: 'in this' > {(dmu_module.startswith('In this'))} & Ends with: 'exercise' > {(dmu_module.endswith('exercise'))}")
print(spacer)

# Exercise 3
print(spacer)
print("\t\t\t[ EXERCISE 3]")
spacer = "- - - - - - - - - - - - - - - - - - - - - - - - " * 2

while True:
    user_input_name = input("Enter username: ")
    if user_input_name.isalpha() and len(user_input_name) >= 4:
        while True:
            try:
                user_purchase_amount = int(input("Enter Amount: $ "))
                if str(user_purchase_amount).isdigit():
                    print(spacer,"\n")
                    template = f"\tDear {user_input_name.capitalize()}, I am writing to you to tell you that I have deposited ${user_purchase_amount} into your bank account. \n\tSincerely,\n\tMarget Thatcher"
                    print(template)
                    print("\n",spacer)
                    exit()
            except ValueError:
                print("[!] Must only enter numbers.")
    else:
        print("[!] Must only enter letters & have a length greater than 4!")
