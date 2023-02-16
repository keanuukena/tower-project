import random

juice = 1
double_juice = 1
floor_num = 1
luck = [1,2]
C1 = False
C2 = False
C3 = False
C4 = False

inventory = ["map", "cheese", "sword"]
gold = 10
hp = 10
room_type = ["An armoury.", "A circular room.", "A library.", "A shop.", "A dragon lair!", "A treasure room.", "A dining hall.", "A room with a chest.", "A candlelit room.",
"A stone corridor.", "A foggy room.", "A room with cobwebs.", "A hot room.", "A dark room."]

print("""	Welcome to TextTower!
You rest at floor 1, and the tower looms before you.""")

while double_juice == 1:
	while juice == 1:
		random.shuffle(luck)
		win = luck[1]
		try:
			print("""
1 - Climb
2 - Inventory
3 - Move to...
4 - Quit""")
			choice = int(input(f"Enter your choice:\n"))

			if choice == 1:
				random.shuffle(room_type)
				current_room_type = room_type[1]
				print(f"You climb to floor {floor_num+1}, {current_room_type}")
				floor_num = floor_num + 1

				#armoury
				if current_room_type == "An armoury.":
					inventory.append("armor")
					print("You found some armor!")
					room_type.remove("An armoury.")

				#circular room
				if current_room_type == "A circular room.":
					print("A skeleton battles you!")
					if win == 1:
						print("The skeleton rattles its bones and then spooks you for 2 damage!\nYou bonk the skeleton with your sword and win!")
						hp -= 2
						if "armor" in inventory:
							print("Your armor takes the hit and shatters!")
							hp += 2
							inventory.remove("armor")
					else:
						print("You dodge the skeleton's spookyness and bonk it with your sword!\nYou win!")
					print("You found an unlocked chest and found 3 gold!")
					gold += 3
					room_type.remove("A circular room.")

				#library
				if current_room_type == "A library.":
					print("Musty shelves hide forgotten secrets...")
					if win == 1:
						print("You find a cursed spellbook. Someone must've spilled curse-juice on it.")
						inventory.append("cursed spellbook")
					if win == 2:
						print("You found a goblin dictionary! It smells like grandma...")
						inventory.append("goblin dictionary")

				#shop
				if current_room_type == "A shop.":
					print("Some tower-gnomes have set up a shop!")
					while 1 == 1:
						print("""cheese - 6 gold
armor - 6 gold
key - 6 gold""")
						purchase_ask = input("Will you buy anything or attempt to steal? (buy/steal/leave)\n")
						purchase_ask = purchase_ask.lower()
						if purchase_ask == "buy":
							purchase = input("Which item will you buy?\n")
							purchase = purchase.lower()
							if purchase == "cheese" and gold >= 6:
								print("You bought some cheese! The gnomes have punctured holes in it to make fake swiss cheese.")
								inventory.append("cheese")
								gold -= 6
							elif purchase == "armor" and gold >= 6:
								print("You bought some gnome-sized armor! It's too small to wear, but you can hold it as a shield I guess.")
								inventory.append("armor")
								gold -= 6
							elif purchase == "key" and gold >= 6:
								print("You bought a key! The dark wizard lost his master key once, and gnomes quickly spread copies all over the place.")
								inventory.append("key")
								gold -= 6
							else:
								print("We can't sell you that. (maybe you misspelled an item, or you're just poor. :(")
						if purchase_ask == "steal":
							if win == 1:
								print("You distract the gnomes by tossing 1 gold on the floor. You don't have time to grab the key, though.")
								inventory.append("cheese")
								inventory.append("armor")
								illegal = True
								gold -= 1
							if win == 2:
								print("You defeat the gnomes with your sword, but one of them stabbed you with its pointy hat.")
								print("You lost 4 health!")
								print("You quickly loot the shop and 10 gold, and hope the other gnomes don't find out...")
								gold += 10
								inventory.append("cheese")
								inventory.append("armor")
								inventory.append("key")
								illegal = True
							break
						if purchase_ask == "leave":
							print("You leave the shop.")
							break

			if choice == 2:
				print(f"You open your pack and have {gold} gold. You have {hp} health. You also have...")
				for item in inventory:
					print(item)
				use_item_ask = str(input(f"Type 'use' to use an item.\n"))
				use_item_ask = use_item_ask.lower()
				if use_item_ask == "use":
					use_item = str(input(f"Which item would you like to use?\n"))
					use_item = use_item.lower()

					if use_item == "cheese":
						regen = 1 + random.randrange(1,3)
						print(f"You ate your cheese and recovered {regen} health.")
						hp += regen

					if use_item == "goblin dictionary":
						print("You can now speak goblin! It sounds like someone dropped a fork in a sink disposal.")
						speak_goblin = True

					if use_item == "cursed spellbook":
						print("You read the spellbook and feel very cursed...")
						print("You gain 3 health!")
						inventory.append("curse")

					else:
						print("Nothing happened. (Maybe you spelled an item wrong?)")

			if choice == 3:
				print("ok")

			if choice == 4:
				print("Goodbye.")
				double_juice += 1
				break
			
			if choice > 4 or choice < 0 and choice != 42:
				print("That wasn't a choice!")

		except ValueError:
			print("That wasn't an option!")