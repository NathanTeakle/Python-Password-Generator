import string
import random


## Just a title for the Script
print ("Python based Password Generator | Author, NTeakle 9/09/2022")


## Characters to generate password from
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_random_password():
	## Sets the total length for the entire passsword, if you set it to 30, you will need to set alphabetical characters to 10,
    	## digits to 10,
   	## special characters to 10,
    	## to generate a total length of 30
	length = int(input("Enter password length: "))

	## Specift the number of character types
	alphabets_count = int(input("Enter alphabetical character count in password: "))
	digits_count = int(input("Enter digit count in password: "))
	special_characters_count = int(input("Enter special character count in password: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	## Check the total length with characters sum count
	## Print not valid if the sum is greater than length
	if characters_count > length:
		print("Characters total count is greater than the password length")
		return


	## Initializing the password generation
	password = []
	
	## Selecting random alphabets
	for i in range(alphabets_count):
		password.append(random.choice(alphabets))


	## Selecting random digits
	for i in range(digits_count):
		password.append(random.choice(digits))


	## Selecting random special characters
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))


	## If the total characters count is less than the password length,
	## Add random characters to make it equal to the length
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	## Chuffling the resultant password
	random.shuffle(password)

	## Converting the list to string
	## Crinting the list
	print("".join(password))



## Invoking the function
generate_random_password()
