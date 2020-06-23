#Importing random
import random



# *** Class ***
class SpaceshipSimulator:
  # Initialise the simulation
	def __init__(self, spaceshipName):
		self.__spaceshipName = spaceshipName
		self.__spaceshipX = 0
		self.__spaceshipY = 0
		self.__movementCounter = 0
		self.__spaceshipPetrolLevel = 50
		self.__spaceshipMaxPetrolLevel = 50
		self.__destinationX = random.randint(-30, 30) 
		self.__destinationY = random.randint(-30, 30) 
		self.__numberOfMoves = 0

	#Returns the spaceship name
	def getSpaceshipName(self):
		return self.__spaceshipName
	
	#Changes the spaceship name
	def setSpaceshipName(self, newName):
		self.__spaceshipName = newName

	#Moves the spaceship up one unit and subtracts 1 unit of petrol
	#I made it so that you can enter in how many units so that it can be easily modified to move faster
	def moveUp(self, num):
		if self.__spaceshipPetrolLevel > 1 and self.__spaceshipY < 30:
			self.__spaceshipY += num
			self.__spaceshipPetrolLevel -= 1
			self.__numberOfMoves += 1
		else:
			print("Sorry, petrol level is at 0. Refill to proceed")


	#Moves the spaceship down one unit and subtracts 1 unit of petrol
	def moveDown(self, num):
		if self.__spaceshipPetrolLevel > 1 and self.__spaceshipY > -30:
			self.__spaceshipY -= num
			self.__spaceshipPetrolLevel -= 1
			self.__numberOfMoves += 1
		else:		
			print("Sorry, petrol level is at 0. Refill to proceed")


	#Moves the spaceship right one unit and subtracts 1 unit of petrol
	def moveRight(self, num):
		if self.__spaceshipPetrolLevel > 1 and self.__spaceshipX < 30:
			self.__spaceshipX += num
			self.__spaceshipPetrolLevel -= 1
			self.__numberOfMoves += 1
		else:		
			print("Sorry, petrol level is at 0. Refill to proceed")

	
	#Moves the spaceship left one unit and subtracts 1 unit of petrol
	def moveleft(self, num):
		if self.__spaceshipPetrolLevel > 1 and self.__spaceshipX > -30:
			self.__spaceshipX -= num
			self.__spaceshipPetrolLevel -= 1
			self.__numberOfMoves += 1
		else:		
			print("Sorry, petrol level is at 0. Refill to proceed")

	
	#Checks to see if the ship is at the destination
	def isAtDestination(self):
		if self.__spaceshipX == self.__destinationX and self.__spaceshipY == self.__destinationY:
			print("You arrived at your destination in " + str(self.__numberOfMoves) + " moves")
		else:
			print("You are not at the target destination, the destination is at (" + str(self.__destinationX) + "," + str(self.__destinationY) + ")")
	
	#Returns the current petrol level of the spaceship
	def getPetrolLevel(self):
		print("Your current petrol level is " + str(self.__spaceshipPetrolLevel))
	
	#Refils petrol level if it is not at max
	def refillPetrolLevel(self):
		if self.__spaceshipPetrolLevel < 50:
			self.__spaceshipPetrolLevel = self.__spaceshipMaxPetrolLevel
			print("Petrol tank refilled - now at maximum capacity")
		else:
			print("Petrol levels are already at capacity")
	
	#Prints the ships current location
	def getShipLocation(self):
		print("Your current coordinates are (" + str(self.__spaceshipX) + "," + str(self.__spaceshipY) + ")")




# *** Procedural Section ***

# START OF PROGRAM RUN: Give the spaceship a name
spaceshipName = input('What is the spaceships name? ')

# variable spaceship = the spaceship (instance of simulator)
spaceship = SpaceshipSimulator(spaceshipName)

# Choice is set to blank by default.
choice = ""

# Present menu options
print("WELCOME, PILOT OF THE " + spaceshipName +  " TO THE SPACESHIP SIMULATOR")
print("You task is to navigate to the chosen coordinates")
print("Enter the key choice depending on the choice you want.")
print("U = MOVE UP")
print("D = MOVE DOWN")
print("L = MOVE LEFT")
print("R = MOVE RIGHT")
print("C = CHECK TO SEE IF SHIP AT DESTINATION")
print("P = CHECK PETROL LEVELS")
print("RE = REFILL PETROL LEVELS")
print("X = TERMINATE SIMULATION")

# Iterative loop - where the bulk of the program happens.
# While the choice isn't X (for terminate), continue to loop through.
while(choice != "X"):
	# Will continue to run until key choice X is selected.
	choice = input('What will your choice be? ')

	#Determine course of action for this choice 

	#If user inputs U move up
	if choice == "U":
		spaceship.moveUp(1)
		spaceship.getShipLocation()
	#If user inputs D move down
	elif choice == "D":
		spaceship.moveDown(1)
		spaceship.getShipLocation()
	#If user inputs L move left
	elif choice == "L":
		spaceship.moveleft(1)
		spaceship.getShipLocation()
	#if user inputs R move right
	elif choice == "R":
		spaceship.moveRight(1)
		spaceship.getShipLocation()
	#if user inputs C the program checks to see if you are at your destination
	elif choice == "C":
		spaceship.isAtDestination()
	#If user enters P the program prints petrol levels
	elif choice == "P":
		spaceship.getPetrolLevel()
	#If the user enters RE their fuel is refilled. 
	elif choice == "RE":
		spaceship.refillPetrolLevel()
	else:
		print("Invalid command - please try again")