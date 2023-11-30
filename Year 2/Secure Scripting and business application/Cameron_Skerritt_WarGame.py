import random
import time
import re
import random
import os 

#----------------------------------------
#|		 SEPERATOR FOR NEATEN CODE		|
#----------------------------------------
def seperator():
	print("-----------------------------------------------------------------")


#--------------------------------
#|		  ASCII ART FOR WAR		|
#--------------------------------
def warAsciiArt(): # War Ascii Art
	print("""
				 █     █░ ▄▄▄       ██▀███  
				▓█░ █ ░█░▒████▄    ▓██ ▒ ██▒
				▒█░ █ ░█ ▒██  ▀█▄  ▓██ ░▄█ ▒
				░█░ █ ░█ ░██▄▄▄▄██ ▒██▀▀█▄  
				░░██▒██▓  ▓█   ▓██▒░██▓ ▒██▒
				░ ▓░▒ ▒   ▒▒   ▓▒█░░ ▒▓ ░▒▓░
				  ▒ ░ ░    ▒   ▒▒ ░  ░▒ ░ ▒░
				  ░   ░    ░   ▒     ░░   ░ 
				    ░          ░  ░   ░     
				                            
					""")

#--------------------
#|		 GAME 		|
#--------------------
class war: # This is where the war game begins
	global savedFileLoaded
	savedFileLoaded = False
	playerOneScore = 0
	playerTwoScore = 0
	roundLimitAmount = None
	playUntilDone = False
	roundsPlayed = 0
	middlePile = []

	def loadSaveFile(self): # load a save file funcrion
		
		while True:
			askUserIfTheySaved = str(input("Load a save file? [y/n] ")).lower() 
			if askUserIfTheySaved == "y":
				print("\ntype: ls to list directory | menu to go to main menu")
				print("To load save file include .txt!")
				loadUpSaveFile = input("Enter file name: ").lower()
				if loadUpSaveFile == "ls": # if user types "ls" prints their current directory
						current_directory = os.getcwd()
						all_files = os.listdir(current_directory)
						txt_files = [file for file in all_files if file.endswith(".txt")] # filters out anything that does not end with .txt
						print("\n~~~~~~~~~~~~~~~~~~~~~~")
						for txt_file in txt_files:
							print(txt_file) # prints all files that have .txt
						print("~~~~~~~~~~~~~~~~~~~~~~\n")
						continue # continues with loop
						# theres a bug somewhere here

				elif loadUpSaveFile == "menu": # if user types "menu" they will get sent back to menu
					mainMenu() # calls mainMenu Function
					return True

				elif os.path.isfile(loadUpSaveFile): # is called when user enters a file name for example: (save.txt)
					print("~~~ LOADING FILE ~~~\n")

					with open(loadUpSaveFile, "r") as file: 
						content = file.readlines() # reads the contents of the file
						loadedPlayerOne = content[0].strip().split() # reads Player One stats (username + score)
						loadedPlayerTwo = content[1].strip().split() # reads Player Two stats (username + score)

						self.playerOneName, loadedPlayerOneScore = loadedPlayerOne # combines playerOne name + their loaded score into LoadedPlayerOne
						self.playerTwoName, loadedPlayerTwoScore = loadedPlayerTwo # combines playerTwo name + their loaded score into LoadedPlayerTwo
						
						# Convert to int
						self.playerOneScore = int(loadedPlayerOneScore) # converts playerOne score from string to int so it can be used in game.
						self.playerTwoScore = int(loadedPlayerTwoScore) # converts playerTwo score from string to int so it can be used in game.
						print("~~~~~~~~ LOADED PLAYERS ~~~~~~~~")
						print(f"Player 1: {self.playerOneName}, Score: {self.playerOneScore}")
						print(f"Player 2: {self.playerTwoName}, Score: {self.playerTwoScore}")
						print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
						return True

					print("\n[!] Usenames loaded from save!")
					print("[!] Scores   loaded from save!")
					global savedFileLoaded
					savedFileLoaded = True
					return self.playerOneName, self.playerOneScore, self.playerTwoName, self.playerTwoScore # returns the username & score for playerOne & playerTwo

				else:
					print("[!] FILE NOT FOUND") 
					self.loadSaveFile() # calls self.loadSaveFile() if no file is found.
					return False
				

			elif askUserIfTheySaved == "n":

				print("[!] No save file loaded.")
				seperator()
				return None, None # returns nothing if user enters "n"
			
			else:
				
				print("[!] You did not enter [y/n]\n") # fail catch if user does not enter y or n
				
		else:
			seperator()
			print("[!] You did not enter [y/n]\n") # fail catch if user does not enter y or n
			seperator()


	#----------------------------------------
	#|		  SHUFFLE DECK & INITIALIZE		|
	#----------------------------------------
	def initializeDeck(self):
		suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
		ranks = "2 3 4 5 6 7 8 9 10 Jack Queen King Ace War Joker".split() # splits each character into its own string
		self.deck = [(suit, rank) for suit in suits for rank in ranks] # creates a deck of cards by combining each suit with each rank. Returns a tuple.
		random.shuffle(self.deck) # shuffle the deck.

	#----------------------------------------
	#|	   SPLIT DECK & HAND OUT CARDS		|
	#----------------------------------------
	def dealPlayerCards(self):
		# we split the deck into two for both players
		self.playerOne = self.deck[:30] # Gives playerOne 30 cards
		self.playerTwo = self.deck[30:] # Gives playerTwo 30 cards

	#----------------------------------------
	#|		  PLAYER ONE WINS ROUND			|
	#----------------------------------------
	def playerOneWinsRound(self):
		self.printUsersCurrentCardCount() # Shows remaining cards for each user
		self.playerOneScore += 1 # We increment player Ones score by 1
		print(f"[!] {self.playerOneName} Wins The Round!")
		self.printCurrentScore() # Shows current score for each user

	#----------------------------------------
	#|		  PLAYER TWO WINS ROUND			|
	#----------------------------------------
	def playerTwoWinsRound(self):
		self.printUsersCurrentCardCount() # Shows remaining cards for each user
		self.playerTwoScore += 1 # We increment player Twos score by 1
		print(f"[!] {self.playerTwoName} Wins The Round!")
		self.printCurrentScore() # Shows current score for each user

	#----------------------------------------
	#|			SANITIZE USER NAME			|
	#----------------------------------------
	playerAmountCounter = 1 # Only meant for formatting the print function.
	def sanitizeUserName(self,username): # Requires username to when called
		
		while True:
			if len(username) == 0: # checks if length of name is 0.
				seperator()
				print("[!] Cannot enter empty name! Try again...") 
				seperator()
				username = input(f"Enter usename: ") # Forces user to re-enter username.

			elif any(char in '!@#$%^&*()-_=+[]{}|;:,.<>?/~`"\'\\' for char in username): # Checks for any bad symbols in the list provided.
				seperator()
				print("[!] Cannot enter special characters! Try again...")
				seperator()
				username = input(f"Enter usename: ") # Forces user to re-enter username.
			else:
				print(f"[+] PLAYER {self.playerAmountCounter}) - {username} username set!") # If both criteria are met, username is set.
				self.playerAmountCounter += 1 # incremenets playerAmountCounter by 1.
				return username # returns username


	#----------------------------------------
	#|			USERS ENTER NAMES			|
	#----------------------------------------
	def enterUserName(self):
		# Allows the user to enter a player 1 & 2 name
			global playerOneName
			global playerTwoName
				
			print("\n[*]Enter usename for Player 1 & 2")

			self.playerOneName = self.sanitizeUserName(input(f"\n[*] Player 1 enter username: ")) # Calls sanitizeUserName with the input username (then checks if it meets the criteria)
			self.playerTwoName = self.sanitizeUserName(input(f"\n[*] Player 2 enter username: ")) # Calls sanitizeUserName with the input username (then checks if it meets the criteria)
			
			print("[+] Player names set!")
			seperator()
			time.sleep(0.50)

	#----------------------------------------
	#|	   PROMPT USER FOR ROUND LIMIT		|
	#----------------------------------------
	def promptForRoundLimit(self):
		while True:
			self.roundLimiterInput = str(input("Do you want enable a round limit? (y/n)\n$> ")).lower() # forces lower case to avoid errors
			if self.roundLimiterInput == "y":
				self.roundLimitAmount = 0 # Sets round limit to 0.
				while self.roundLimitAmount < 3: # Loops until the user enters anything above 2. This is to prevent draws.
					try:
						self.roundLimitAmount = int(input("[+] Enter max amount of rounds: \n$> ")) # sets max amount of rounds / OR till cards run out.
						if self.roundLimitAmount < 3: # can only allow more than 2 rounds so we dont have any draws.
							print("[!] Enter a number greater than 2.")
					except ValueError:
						seperator()
						print("\n[!] Cannot Enter non-integer values. Try again.") # catches error if user enters non-int
						seperator()
				
				print(f"\n[+] Max rounds set: {self.roundLimitAmount}")
				seperator()
				self.playUntilDone = False
				return True

			elif self.roundLimiterInput == "n": # if user enter n we skip RoundLimitInput
				print("\n[!] No max rounds set!")
				print("[!] You will play default WAR! The game will take a while...")
				self.playUntilDone = True # Play until done is set to True (game will continue until someone runs out of cards)
				return True
				seperator()

			else:
				seperator()
				print("[!]You did not enter y or n") # forces user to enter y or n
				seperator()


	#----------------------------------------
	#|			START ROUND FUNCTION		|
	#----------------------------------------
	def printUsersCurrentCardCount(self):
		print(f"P1) {self.playerOneName}: {playerOneTopCard[1]} of {playerOneTopCard[0]} - Cards left: {len(self.playerOne)} \nP2) {self.playerTwoName}: {playerTwoTopCard[1]} of {playerTwoTopCard[0]} - Cards left: {len(self.playerTwo)}")
		# ^ Formatted string to show player ones & twos name, their chosen card (suit-rank) and how many cards each user has left.
	
	def startRound(self):
		global middlePile

		if (self.roundLimitAmount is not None and self.roundsPlayed < self.roundLimitAmount) or self.playUntilDone: 
		# ^ Checks to see if roundLimit is not set to nothing and if the playedRounds are less than the inputted RoundLimit OR if self.playUntilDone is set to True.
			self.roundsPlayed += 1 #increments rounds played
			
			print(f"\t\t\t\tRound {self.roundsPlayed}\n") # shows amount of rounds played
			
			global playerOneTopCard
			global playerTwoTopCard

			playerOneTopCard = self.playerOne.pop() # remove playerOne card
			playerTwoTopCard = self.playerTwo.pop() # remove PlayerTwo card
			
			global cardValues 
			cardValues = { # Holds each card value
			"Ace": 14,
			"King": 13,
			"Queen": 12,
			"Jack": 11,
			"10": 10,
			"9": 9,
			"8": 8,
			"7": 7,
			"6": 6,
			"5": 5,
			"4": 4,
			"3": 3,
			"2": 2
			}

			#----------------------------------------
			#|		 SPECIAL CARD CHECK - JOKER		|
			#----------------------------------------
			if playerOneTopCard[1] == "Joker" and playerTwoTopCard[1] == "Joker": # if both players pull a joker card
				self.printUsersCurrentCardCount()
				print("\n~~~~~~~~~~~~~~~~~ SPECIAL CARD IN PLAY ~~~~~~~~~~~~~~~~~")
				print("IMPOSSIBLE,  BOTH PLAYERS PICKED A JOKER! ITS ALL OUT WAR!")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				self.printUsersCurrentCardCount() # shows current cards left
				self.beginWar() # special rule: we automatically call a WAR
				return

			elif playerOneTopCard[1] == "Joker": # if player one pulls a joker card
				self.printUsersCurrentCardCount()
				print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SPECIAL CARD IN PLAY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				print(f"{self.playerOneName} feels a pity against the opponent, you give 3 cards to your opponent...")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				if len(self.playerOne) < 3: # checks to see if the user has enough cards
					print(f"{self.playerOneName} does not have enough cards to give...")
					self.printUsersCurrentCardCount() # shows current cards left
					self.printCurrentScore() # shows current score
					return
				else: # if player one has enough cards
					for _ in range(3): # we loop 3 times, inserting a total of 3 cards into playerTwo's hand
						self.playerTwo.insert(0, self.playerOne.pop()) # we insert one card to playerTwos hand and remove one card from playerOnes hand

					self.printUsersCurrentCardCount() # shows current cards left
					self.printCurrentScore() # shows current score
					return

			elif playerTwoTopCard[1] =="Joker": # if player Two pulls a joker card
				self.printUsersCurrentCardCount()
				print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SPECIAL CARD IN PLAY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				print(f"{self.playerTwoName} feel a pity against the opponent, you give 3 cards to your opponent...")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				if len(self.playerTwo) < 3: # checks to see if the user has enough cards
					print(f"{self.playerTwoName} does not have enough cards to give...")
					self.printUsersCurrentCardCount()
					return
				else: # if player two has enough cards
					for _ in range(3): # we loop 3 times, inserting a total of 3 cards into playerOne's hand

						self.playerOne.insert(0, self.playerTwo.pop()) # we insert one card to playerOnes hand and remove one card from playerTwos hand
					self.printUsersCurrentCardCount() # shows current cards left
					self.printCurrentScore() # shows current score
					return

				
				
			#----------------------------------------
			#|		 SPECIAL CARD CHECK - WAR		|
			#----------------------------------------
			elif playerOneTopCard[1] == "War" and playerTwoTopCard[1] == "War": # if both players pick up a war card
				self.printUsersCurrentCardCount()
				print("\n\t\t\t~~~~~~~~~~~~~~~~~~~~~~ WAR IN PROGRESS ~~~~~~~~~~~~~~~~~~~~~~")
				print("\t\t\tUNIMAGINABLE SUFFERING! BOTH PLAYERS HAVE SELECTED A WAR CARD! ")
				print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
				middlePile = [playerOneTopCard, playerTwoTopCard]
				warAsciiArt() # prints out the WAR ascii art
				self.beginWar() # calls the war function

			elif playerOneTopCard[1] == "War":
				self.printUsersCurrentCardCount()
				print("\n~~~~~~~~~ SPECIAL CARD IN PLAY ~~~~~~~~~")
				print(f"{self.playerOneName}  STARTED A WAR!")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				middlePile = [playerOneTopCard, playerTwoTopCard]
				warAsciiArt() # prints out the WAR ascii art
				self.beginWar() # calls the war function


			elif playerTwoTopCard[1] == "War": # if playerTwo draws a WAR card
				self.printUsersCurrentCardCount()
				print("\n~~~~~~~~~ SPECIAL CARD IN PLAY ~~~~~~~~~")
				print(f"{self.playerTwoName}  STARTED A WAR!")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				middlePile = [playerOneTopCard, playerTwoTopCard]				
				warAsciiArt() # prints out the WAR ascii art
				self.beginWar() # calls the war function
			

			#--------------------------------
			#|		 NORMAL CARD CHECK		|
			#--------------------------------

			elif cardValues[playerOneTopCard[1]] > cardValues[playerTwoTopCard[1]]: # if playerOnes card has a greater value than playerTwos card
				middlePile = [playerOneTopCard, playerTwoTopCard] # places both cards onto the middle pile
				self.playerOne.extend(middlePile) # used as a place to store cards from both players and handed out after a player wins
				self.playerOneWinsRound() # Player One Wins the round

			elif cardValues[playerOneTopCard[1]] < cardValues[playerTwoTopCard[1]]: # if playerTwos card has a greater value than playerOnes card
				middlePile = [playerOneTopCard, playerTwoTopCard] # places both cards onto the middle pile
				self.playerTwo.extend(middlePile) # used as a place to store cards from both players and handed out after a player wins
				self.playerTwoWinsRound() # Player Two Wins the round

			elif cardValues[playerOneTopCard[1]] == cardValues[playerTwoTopCard[1]]: # if both ranks are the same, we call the WAR function
				seperator()
				middlePile = [playerOneTopCard, playerTwoTopCard]
				self.printUsersCurrentCardCount()
				print("\n\t\t\t~~~~~~~~~~~~ WAR IN PROGRESS ~~~~~~~~~~")
				print("\t\t\tA WAR HAS BROKEN OUT! ITS ALL OUT MAYHEM!")
				print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
				warAsciiArt() # prints out WAR ascii art
				self.beginWar() # calls the war function

			else:
				print("Something bad happend!") # Error catching, this is never printed unless something goes horribly wrong.

			middlePile = []
			input("\n\t\t- - - Press Any Key To Continue - - -\n") # allows the user to continue the game
			seperator()
		else:
			self.comparePlayerScores() # if rounds run out, this function is called
			return True


	def playerPicksTheirInput(self, playername):
		# this is for the instant kill mechanic during WAR
		print("PICK A NUMBER BETWEEN 1 AND 100! Pick wisely...")
		while True:
			try:
				userInput = int(input(f"{playername} $> "))
				if userInput >= 1 and userInput <= 100:
					return userInput
				else:
					print("Enter a number between 1 and 100.")
			except ValueError:
				print("Invalid input.")

	def printOutPlayerCards(self):
		print(f"P1) {self.playerOneName}: {playerOneTopCard[1]} of {playerOneTopCard[0]} - Cards left: {len(self.playerOne)} \nP2) {self.playerTwoName}: {playerTwoTopCard[1]} of {playerTwoTopCard[0]} - Cards left: {len(self.playerTwo)}")

	#----------------------------------------
	#|			START WAR FUNCTION			|
	#----------------------------------------
	def beginWar(self):
		global playerOneTopCard
		global playerTwoTopCard
		global cardValues

		if len(self.playerOne) <= 3 or len(self.playerTwo) <= 3: # checks to see if both players have enough cards for war
			print("[!] Not enough cards for war.")
			self.StopGame() # if either user does not have enough cards, we decide a winner via stopGame()

		else:
			
			middlePile.extend([self.playerOne.pop() for _ in range(3)])
			middlePile.extend([self.playerTwo.pop() for _ in range(3)]) # playerTwo places 3 cards to the middle pile
			print(f"[!] {self.playerOneName} and {self.playerTwoName} placed 3 cards down each into the middle deck!\nMiddle Deck has: ", len(middlePile), "cards\nThe players now have:")

			print(f"[!] {self.playerOneName} has: {len(self.playerOne)} cards")
			print(f"[!] {self.playerTwoName} has: {len(self.playerTwo)} cards\n")
			playerOneTopCard = self.playerOne.pop() # playerOne picks a card
			playerTwoTopCard = self.playerTwo.pop() # playerTwo picks a card

			middlePile.append(playerOneTopCard)
			middlePile.append(playerTwoTopCard)
			print("[+] Both Players placed their card into middle deck\nMiddle deck contains: ", len(middlePile), "cards\n")
			self.printUsersCurrentCardCount()
	        #----------------------------------------
			#|		 SPECIAL CARD CHECK - JOKER		|
			#----------------------------------------

			if playerOneTopCard[1] == "Joker" and playerTwoTopCard[1] == "Joker": # if both users pick a joker during war
				print("\n~~~~~~~~~~~~~~~~~ SPECIAL CARD IN PLAY ~~~~~~~~~~~~~~~~~")
				print("IMPOSSIBLE,  BOTH PLAYERS PICKED A JOKER! ITS ALL OUT WAR!")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				print("[!] The war still rages on!")
				self.printUsersCurrentCardCount() # prints out current card count
				self.beginWar() # we call war again


			elif playerOneTopCard[1] == "Joker": # if playerOne picks a joker
				print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SPECIAL CARD IN PLAY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				print(f"{self.playerOneName} feels a pity against the opponent, you give 3 cards to your opponent...")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				print("[!] The war still rages on!")
				if len(self.playerOne) < 3: # checks to see if they have enough cards to give
					print(f"{self.playerOneName} does not have enough cards to give to: {self.playerTwoName}") # if playerOne does not have enough cards this gets printed
				else: # if they do:
					for _ in range(3): # we loop 3 times
						self.playerTwo.insert(0, self.playerOne.pop()) # we insert a card into playerTwos hand and remove one from playerOne
					self.printUsersCurrentCardCount() # prints current card count
					print("[!] The war still rages on!")
					self.beginWar() # calls war function

				
			elif playerTwoTopCard[1] =="Joker": # if playerTwo picks a joker
				print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SPECIAL CARD IN PLAY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				print(f"{self.playerTwoName} feel a pity against the opponent, you give 3 cards to your opponent...")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				print("[!] The war still rages on!")
				if len(self.playerTwo) < 3:
					print(f"{self.playerTwoName} does not have enough cards to give to: {self.playerOneName}") # if playerTwo does not have enough cards this gets printed
				else:
					for _ in range(3): # we loop 3 times
						self.playerOne.insert(0, self.playerTwo.pop()) # we insert a card into playerOnes hand and remove one from playerTwo
					self.printUsersCurrentCardCount() # prints current card count
					print("[!] The war still rages on!")
					self.beginWar() # calls war function

				
				#-------------------------------------------------------------------------------------------------------------
				#|		 SPECIAL CARD CHECK - WAR	This is untested code, I could not get this scenario to run when testing.|
				#-------------------------------------------------------------------------------------------------------------

			elif playerOneTopCard[1] == "War": # if player one picks a war card 
				print("\n~~~~~~~~~ SPECIAL CARD IN PLAY ~~~~~~~~~")
				print(f"{self.playerOneName}  STARTED A WAR!")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				warAsciiArt() # prints war ascii art
				self.printUsersCurrentCardCount() # Shows current cards left
				self.beginWar() # we re-call war function.

			elif playerTwoTopCard[1] == "War": # if player two picks a war card
				print("\n~~~~~~~~~ SPECIAL CARD IN PLAY ~~~~~~~~~")
				print(f"{self.playerTwoName}  STARTED A WAR!")
				print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				warAsciiArt() # prints war ascii art
				self.printUsersCurrentCardCount() # Shows current cards left
				self.beginWar() # we re-call war function.

			elif cardValues[playerOneTopCard[1]] == cardValues[playerTwoTopCard[1]]: # if both users have the same card, the war continues.
				print("[!] War continues!")
				self.printUsersCurrentCardCount() # prints out current cards left
				self.beginWar() # We re-call war function


			elif cardValues[playerOneTopCard[1]] > cardValues[playerTwoTopCard[1]]: # if playerOnes card is greater than playerTwos card
				print(f"{self.playerOneName} WON\n[!] Awarding {self.playerOneName} with ", len(middlePile), "cards")
				self.playerOne.extend(middlePile) # awards playerOne with the war cards
				seperator()
				self.playerOneScore += 1 # increments playerOnes score
				print(f"[!] {self.playerOneName} has: {len(self.playerOne)} cards")
				print(f"[!] {self.playerTwoName} has: {len(self.playerTwo)} cards\n")
				print(f"[!] {self.playerOneName} Wins The War!") 
				self.printCurrentScore() # prints current score

			else:
				print(f"{self.playerTwoName} WON\n[!] Awarding {self.playerTwoName} with ", len(middlePile), "cards")
				self.playerTwo.extend(middlePile) # awards playerTwo with the war cards
				seperator()
				self.playerTwoScore += 1
				print(f"[!] {self.playerOneName} has: {len(self.playerOne)} cards")
				print(f"[!] {self.playerTwoName} has: {len(self.playerTwo)} cards\n")
				print(f"[!] {self.playerTwoName} Wins The War!")
				self.printCurrentScore() # prints current score
			

	#----------------------------------------
	#|			COMPARE PLAYER SCORES 		|
	#----------------------------------------
	def comparePlayerScores(self): # this function is only called when playing with a round limit
		#seperator()
		if self.playerOneScore > self.playerTwoScore: # if playerOne has a greater score than playerTwo
			print(f"THE WINNER OF WAR IS: {self.playerOneName}")
			saveFile(self.playerOneName, self.playerOneScore, self.playerTwoName, self.playerTwoScore) # Save file is called with playerOnes username + score, playerTwos username + score
			mainMenu() # returns user to mainMenu

		elif self.playerOneScore == self.playerTwoScore: # if both users have equal score
			print("ITS A DRAW")
			saveFile(self.playerOneName, self.playerOneScore, self.playerTwoName, self.playerTwoScore) # Save file is called with playerOnes username + score, playerTwos username + score
			mainMenu() # returns user to mainMenu

		else: # if PlayerTwo has a greater score than PlayerOne
			print(f"THE WINNER OF WAR IS: {self.playerTwoName}")
			saveFile(self.playerOneName, self.playerOneScore, self.playerTwoName, self.playerTwoScore) # Save file is called with playerOnes username + score, playerTwos username + score
			mainMenu() # returns user to mainMenu

		


	#----------------------------------------
	#|			SHOW CURRENT SCORE			|
	#----------------------------------------
	def printCurrentScore(self): # Formatted Current Score
		print(f"\nCurrent Score")
		print(f"{self.playerOneName} {self.playerOneScore} | {self.playerTwoScore} {self.playerTwoName}") # Displays users scores in a formatted string
		seperator()
	
	#----------------------------------------
	#|			START WAR FUCNTION			|
	#----------------------------------------
	def startCardGameOfWar(self):
		self.initializeDeck() # calls the initDeck which shuffles the cards
		self.dealPlayerCards() # we call the dealPlayerCards to split the deck into two
		print(f"{self.playerOneName} - holds: {len(self.playerOne)} cards")
		print(f"{self.playerTwoName} - holds: {len(self.playerTwo)} cards")
		while len(self.playerOne) > 0 and len(self.playerTwo) > 0: # this checks the length of both players to see if they have any cards left

			self.startRound() # if the statement is True, we start the round.
		self.StopGame() # if False, we stop the game.


	#----------------------------------------
	#|			STOP GAME FUCNTION			|
	#----------------------------------------
	def StopGame(self): 
		global playerOneScore
		global playerTwoScore

		if len(self.playerOne) <= 3: # checks to see if the playerOne hand is <=3 (Not enough cards for war) or player has ran out of cards
			print(f"{self.playerOneName} did not have enough cards for WAR!")
			print("\n~~~~~~~ SPECIAL RULE IN PLAY ~~~~~~~")
			print(f"{self.playerTwoName} WINS!")
			saveFile(self.playerOneName, self.playerOneScore, self.playerTwoName, self.playerTwoScore) # Save file is called with playerOnes username + score, playerTwos username + score

		elif len(self.playerTwo) <= 3: # checks to see if the playerTwo hand is <=3 (Not enough cards for war) or player has ran out of cards
			print(f"{self.playerTwoName} did not have enough cards for WAR!")
			print("\n~~~~~~~ SPECIAL RULE IN PLAY ~~~~~~~")
			print(f"{self.playerOneName} WINS!")
			saveFile(self.playerOneName, self.playerOneScore, self.playerTwoName, self.playerTwoScore) # Save file is called with playerOnes username + score, playerTwos username + score
			mainMenu() # returns user to mainMenu

		elif len(self.playerOne) == 0 and len(self.playerTwo) == 0: # if the length of bother players hands are 0
			print("\n~~~~~~~ SPECIAL RULE IN PLAY ~~~~~~~")
			print("No one wins!")
			mainMenu() # returns user to mainMenu

		else:
			print("It's a draw! :(") # This is a fail-safe incase all other if-elif statements fail.
			mainMenu() # returns user to mainMenu

def mainMenu(): # Main Menu
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Welcome To My War Game!")
	print("Here are the rules of the game")
	print("""
   - Special cards are in play, especially during a war! Prepare to lose a lot of cards.
   - A war is activated if two players have the same rank card!
   - Press any key to continue the game.

   ~~~~~~~~~~~~~~~~~~~~~~~~~ SPECIAL CARDS ~~~~~~~~~~~~~~~~~~~~~~~~~
   - Joker - You give the enemy 3 of your cards
   - War - Starts a war instantly

   ~~~~~~~~~~~~~~~~~~~~~~~~~ WIN CONDITIONS ~~~~~~~~~~~~~~~~~~~~~~~~~
   - Whoever reaches 0 cards wins (With no Win Limit)
   - If you enable Win Limit, whoever has a higher score wins! (unless you run out of cards!)


   ~~~~~~~~~~~~~~~~~~~~~~~~~ SAVE FUNCTION ~~~~~~~~~~~~~~~~~~~~~~~~~
   - When asked to save, please only put the NAME and not name.txt! (saveFileNameExample)
   - The file will save in your current directory where the game was ran.
   - To load a save enter the full name of the file. (saveFileName.txt)
   - Type "ls" to list your directory.
   - Type "menu" to go back to the main menu.
   - Type "quit" to exit the game.

   ~~~~~~~~~~~~~~~~~~~~~~~~~ SPECIAL RULES ~~~~~~~~~~~~~~~~~~~~~~~~~
   - A winner is decided in a long game by who has a greater score UNLESS they run out of cards THEN its decided by who has more cards.
   - If both players run out of cards at the same time, no winner is crowned.
	""")

	while True: # Loops till user enters a valid input
		askUserToStartGame = input("Start game? type: start / quit: ").lower() # asks the user to start the game or to quit
		if askUserToStartGame == "start":
			seperator()
			print("[+] Starting game...")
			seperator()
			startGame() # Calls Start Game Function
			return True
		elif askUserToStartGame == "quit":
			print("[+] Exiting game...")
			exit() # Exits game
			return True
		else:
			print("Enter start or quit.")
	

def saveFile(playerOneName, playerOneScore, playerTwoName, playerTwoScore): # Saves players session with current USERNAME + SCORE for both PLAYERS

	while True:
		doYouWishToSave = input("[?] Save file? [y/n]")
		if doYouWishToSave == "y":
			print("[!] DO NOT INCLUDE .txt!")
			saveFileName = input("Save file name: ")
			print("~~~ SAVING FILE ~~~")
			file = open(f"{saveFileName}.txt", "w")
			file.write(f"{playerOneName} {playerOneScore}\n") # writes player ones name + score
			file.write(f"{playerTwoName} {playerTwoScore}") # writes player twos name + score
			file.close()
			print("~~~ FILE SAVED ~~~")
			while True:
				askToReturnToMainMenu = input("Return to main menu? [y/n]: ").lower()
				if askToReturnToMainMenu == "y":
					mainMenu()
					return True
				elif askToReturnToMainMenu == "n":
					exit()
					return True
				else:
					print("Please enter y/n")
			

		elif doYouWishToSave == "n":
			print("[!] Proceeding to main menu...")
			mainMenu()
			return True

		else:
			print("[!] You did not enter [y/n]")

def startGame():
	global savedFileLoaded
	game = war()
	game.loadSaveFile()
	if savedFileLoaded == False: # if a save file was loaded, this function is skipped.
		game.enterUserName()

	game.promptForRoundLimit()
	game.startCardGameOfWar()

mainMenu()
# - - - - - - - - - - - # 
# SOURCES 
# https://github.com/AppleJuiceNerd/War-Card-Game-Simulator/blob/main/War.py
# https://github.com/maximedrn/war-card-game/blob/master/main.py
# https://github.com/Soumya-Kushwaha/WAR-Card-Game/blob/main/WarCardGame.py
# https://patorjk.com/software/taag
# https://pastebin.com/EeXw6GVy