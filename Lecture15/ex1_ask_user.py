#!usr/bin/python3


def background_check(name, age, colour, py, world):
	print(f"\nYou have provided the following details: \n\tName: {name}\n\tAge: {age}\n\tColour: {colour}\n\tPython preference: {py}\n\tFlat world: {world}\n")
	print(f"Wow! Your name is {len(name)} characters long.")
	
	old = "older than" if age > 22 else "the same age as" if age == 22 else "younger than"
	print(f"Wow! You are {old} me!")
	
	if colour.lower() == "blue":
		print("You know your colours ;)")
	else:
		print(f"I can see that you like {colour}, but try blue sometime.")
	
	if py.lower()[0] == 'y':
		print("Me too!")
	else:
		print("Hmmmmmm, you really don't?")
	
	if world.lower()[0] == "f":
		print("Yup, it's a round world.")
	else:
		print("THE WORLD IS FLAT.")
	
	print()
	
	return "Check complete!"


details={}
details["name"]   = input("What is your name? ")
details["age"]    = int(input("How old are you? "))
assert 0 < details["age"] < 100, "Please insert a valid age between 1 and 99"
details["colour"] = input("What's your fav colour? ")
details["py"] = input("Do you like Python? (Y/N) ")
details["world"]  = input("The world is flat: True or False? ")

print(background_check(**details))


