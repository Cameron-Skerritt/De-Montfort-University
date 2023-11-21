import hashlib
import re 
"""
This script was made as a modification of previous code that was given to me.
I was tasked to improve the security by adding in a "safer way to log in"
This included:
- Adding a function to check if the user is >=13 years old.
- Agreeing to the terms & conditions
- Entering in a valid, sanitized username 
- Creating a strong password that isn't easily brute-forceable.
- Hashing the password to store in a database.
- Passing a unique ID for the user
"""
def seperator():
	print("- - - - - - - - - - - - - - - - - - - - - - -") 

def userAgreement(user_id):

		while True:
			try:
				userAge = int(input("Enter AGE: "))
				if userAge < 13: # if user is under the age of 13, we exit the program
					print("[!] Must be 13 or over to use this application.")
					exit()
				elif userAge >= 13: # if user is equal or above the age of 13, we continue.
					print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
					print("""
	We will collect some personal data to help improve our services.
	What data we will collect:				
		- location (general location)
		- Webclient information (browser, time, OS)
		- Website interactions
		- Personalissed advertisements
	""")
					print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
					userAgreement = str(input("Do you agree to our terms and conditions? [y/n] ")).lower()
					if userAgreement == "y": # if the user does agree with T&C's. we continue the program.
						createUserName(user_id)
						return True
					else: # if they do not agree, we exit the program.
						print("[!] You did not agree to our terms and conditions!")
						exit()
			except ValueError: # this catches the userAge error if they enter anything other than a digit.
				print("Must enter a digit.") 


def createUserName(user_id):
	print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
	print("\t\t\tCREATE_USERAME\n\nMust not contain any special characters.\nCan use numbers.\n")

	while True:
		username = input("Enter username: ") # User enters their name.

		if any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?/~`"\'\\' for char in username): # searches every character for the listed characters, if found, namecheck fails & repeats.
			print("- - - - - - - - - - - - - - - - - - - - - - - - - -")
			print("| Username cannot contain any special characters. |")
			print("- - - - - - - - - - - - - - - - - - - - - - - - - -")

		elif len(username) == 0: # checks to see if the length of the user is 0.
			print("- - - - - - - - - - - - - - -")
			print("| Username cannot be empty. |")
			print("- - - - - - - - - - - - - - -")

		else: # if both methods are satisfied, we continue with the program.
			print("- - - - - - - - - - - -")
			print("| [+] Username created |")
			print("- - - - - - - - - - - -")

			createUserPassword(username, user_id) # passes current username into createUserPassword
			return True
			
def createUserPassword(username, user_id):
	print("Create Password.\n Must contain:\n - 8 or more characters\n - 2 or moresymbols\n - 2 or more numbers\n - 2 or more capital letters")
	print("- - - - - - - - - - - - - - -")
	while True:
		password = input("[+] Enter password: ") # user enters their password

		if len(password) < 8:
			print("| Password must be 8 or more characters long.	   | ") # checks to see if the length of the password is 8 or more characters long.
			

		if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) < 2: # checks to see if password contains any of the provided symbols.
			print("| Password must contain at least 2 symbols.  	   |")
			

		if len(re.findall(r'\d', password)) < 2: # checks to see if the password contains 2 digits or more.
			print("| password must contain 2 or more digits.    	   |")
		
		if len(re.findall(r'[A-Z]', password)) < 2: # Checks to see if the password contains 2 or more capitals.
			print("| Password must contain 2 or more capital letters. |")
			print("- - - - - - - - - - - - - - - - - - - - - - -")
		# If any of these checks fail, we keep asking the user to make a create a password until all checks are complete.

		else: 
			reEnterPassword = input("[+] input password again: ") # Runs if all checks are satisfied.
			if reEnterPassword == password:
				encryptedPassword = hashlib.sha512(password.encode()).hexdigest() # This encrypts the users password in sha512
				
				# Store this hash in the database instead of the raw password.
				# to let the user log in, we would compare the hashes, if they match, we let them log in.
				seperator()
				print("ACCOUNT GENERATED")
				print(f"[+] USERNAME: {username}") 
				print("[+] Password created successfully.")
        print(f"[+] USER ID: {user_id}")
				seperator()
				break
			else:
				print("- - - - - - - - - - - - - -")
				print("| Password does not match! |")
				print("- - - - - - - - - - - - - -")
				createUserPassword(username) # if the user fails the check, we call createUserPassword again and pass the same username again.

userAgreement(512) # we call userAgreement and pass in their user_id number (unique identifier)

