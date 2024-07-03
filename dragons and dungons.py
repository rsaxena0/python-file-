import random

# Character creation
def create_character():
    character = {
        "name": input("Enter your character's name: "),
        "class": input("Choose your class (Warrior, Mage, Rogue): "),
        "level": 1,
        "health": 100,
        "strength": random.randint(5, 10),
        "magic": random.randint(5, 10),
        "dexterity": random.randint(5, 10),
    }
    return character

# Display character stats
def display_character(character):
    print("\nCharacter Stats")
    for key, value in character.items():
        print(f"{key}: {value}")

# Simple combat system
def combat(player, enemy):
    print(f"\nYou are fighting a {enemy['name']}!")
    while player['health'] > 0 and enemy['health'] > 0:
        action = input("Do you want to (A)ttack or (R)un? ").lower()
        if action == 'a':
            if player['class'].lower() == 'warrior':
                damage = player['strength'] + random.randint(0, 5)
            elif player['class'].lower() == 'mage':
                damage = player['magic'] + random.randint(0, 5)
            else:
                damage = player['dexterity'] + random.randint(0, 5)

            enemy['health'] -= damage
            print(f"You dealt {damage} damage to the {enemy['name']}.")

            if enemy['health'] > 0:
                enemy_damage = random.randint(5, 15)
                player['health'] -= enemy_damage
                print(f"The {enemy['name']} dealt {enemy_damage} damage to you.")
        elif action == 'r':
            print("You ran away!")
            break
        else:
            print("Invalid action. Please choose again.")

    if player['health'] <= 0:
        print("You have been defeated!")
    elif enemy['health'] <= 0:
        print(f"You defeated the {enemy['name']}!")

# Main game loop
def main():
    print("Welcome to Dungeons and Dragons!")
    player = create_character()
    display_character(player)

    enemy = {
        "name": "Goblin",
        "health": 50,
    }

    combat(player, enemy)

    if player['health'] > 0:
        print("Congratulations, you have won the game!")
    else:
        print("Game Over.")

if __name__ == "__main__":
    main()

