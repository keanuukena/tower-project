import random

juice = 1
double_juice = 1
floor_num = 1
C1 = False
C2 = False
C3 = False
C4 = False

inventory = ["Map"]
gold = 10
room_type = ["An armoury.", "A circular room.", "A library.", "A shop.", "A dragon lair!"]

print("""	Welcome to TextTower!
You rest at floor 1, and the tower looms before you.

1 - Climb
2 - Inventory
3 - Move to...
4 - Quit""")

while double_juice == 1:
	while juice == 1:
		try:
			choice = int(input(f"Enter your choice:\n"))

			if choice == 1:
				random.shuffle(room_type)
				current_room_type = room_type[1]
				print(f"You climb to floor {floor_num+1}, {current_room_type}")
				floor_num = floor_num + 1

			if choice == 2:
				print(f"You open your pack and have {gold} gold and {inventory[0]}")



		except ValueError:
			print("That wasn't an option!")