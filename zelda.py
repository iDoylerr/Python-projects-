import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10

    def attack(self, enemy):
        damage = random.randint(1, self.attack_power)
        enemy.health -= damage
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.attack_power = 5

    def attack(self, player):
        damage = random.randint(1, self.attack_power)
        player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage.")

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    enemy = Enemy("Goblin")

    print("A wild Goblin appears!")

    while player.health > 0 and enemy.health > 0:
        print(f"\n{player.name}'s Health: {player.health}")
        print(f"{enemy.name}'s Health: {enemy.health}")

        action = input("Do you want to attack? (yes/no): ").lower()

        if action == "yes":
            player.attack(enemy)
            enemy.attack(player)
        elif action == "no":
            print("You decide not to attack.")
            enemy.attack(player)
        else:
            print("Invalid action. Please enter 'yes' or 'no'.")

    if player.health <= 0:
        print("Game over. You were defeated.")
    elif enemy.health <= 0:
        print("Congratulations! You defeated the Goblin.")

if __name__ == "__main__":
    main()
