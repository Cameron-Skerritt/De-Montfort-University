# Exercise 1
placer = "- - - - - - - - - - " * 3

print(placer)
print("\t\t\tExercise 1")
temps = [21, 23, 25, 24, 17, 22, 27]
print("Max temp:", max(temps),"degrees")
print("Min temp:", min(temps),"degrees")

print("\nTemps > 23 degrees:")
for i in temps:
	if i >23:
		print(" ",i)


#Exercise 2
print("\n\t\t\tOdd or even checker!")
try:
	user_input = int(input("Enter number: "))
	if user_input % 2 == 0: # checks if it's divisible by 2 and a remainder of 0.
		print("Its even")
	else:
		print("Its odd!")
except ValueError:
	print("[!] Can only enter numbers!")

print("\n", placer)
# Exercise 3
print("\t\t\tGrade Checker")
print("\nType: exit to stop")
grade_array = []
while True:
	try:
		name_input = input("Enter name: ").capitalize() 
		if name_input == 'Exit':
			break
		user_input = int(input("Enter mark: "))
		grade_array.append([name_input, user_input])

	except ValueError:
		print("[!] Cannot enter letters.")

print(placer)
print("\nName - Grade")
for row in grade_array:
	name = row[0]
	mark = row[1]
	
	if mark in range(90,101): #90, 100
		grade = "A"

	elif mark in range(80,90): #80, 89
		grade = "B"

	elif mark in range(70,80): # 70, 79
		grade = "C"

	elif mark in range(60,70): #60, 69
		grade = "D"

	elif mark in range(50,60): #50, 59
		grade = "E"

	elif mark < 50:
		grade = "F" # 50
	else:
		grade = "[!] valueError [!]" # Error catching

	print(f"{name}  -  {grade}")
