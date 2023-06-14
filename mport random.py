mport random


class Game:
    def __init__(self):
        self.world = World()
        self.player = Player()

    def play(self):
        while True:
            # Get the player's input
            action = input("What do you want to do? ")

            # Update the world based on the player's input
            self.world.update(action, self.player)

            # Check if the player has won the game
            if self.world.is_won():
                print("Congratulations! You have completed the game.")
                break

            # Generate a new level
            self.world.generate_level()

            # Learn from the player's previous actions
            self.world.learn()

            # Print the current player and level information
            print("Player: ", self.player.__dict__)
            print("Current Level: ", self.world.current_level)
            print()

            
class World:
    def __init__(self):
        self.levels = []
        self.current_level = 0

    def update(self, action, player):
        # If the player chooses to move, move them to the next location
        if action == "move":
            player.move()

        # If the player chooses to attack, attack the nearest enemy
        elif action == "attack":
            player.attack(self.levels[self.current_level].enemies)

        # If the player chooses to use an ability, use the ability
        elif action == "ability":
            player.use_ability()

    def generate_level(self):
        # Generate a new level based on the player's previous actions
        level = Level()
        level.enemies = []
        for _ in range(random.randint(1, 5)):
            enemy = Enemy()
            enemy.position = (random.randint(0, 100), random.randint(0, 100))
            level.enemies.append(enemy)
        self.levels.append(level)
        self.current_level += 1

    def learn(self):
        # Learn from the player's previous actions by adjusting the difficulty of the next level
        if self.current_level > 0:
            previous_level = self.levels[self.current_level - 1]
            if previous_level.is_won():
                # If the player won the previous level, make the next level harder
                self.levels[self.current_level].enemies = [
                    enemy for enemy in previous_level.enemies if enemy.health > 0
                ]
            else:
                # If the player lost the previous level, make the next level easier
                for enemy in previous_level.enemies:
                    enemy.health -= 1

    def is_won(self):
        # Check if the player has completed all levels
        return self.current_level >= len(self.levels)


class Player:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10
        self.abilities = {}

    def move(self):
        # Move the player to the specified location
        x = int(input("Enter the x-coordinate: "))
        y = int(input("Enter the y-coordinate: "))
        self.position = (x, y)

    def attack(self, enemies):
        # Attack the nearest enemy
        if len(enemies) > 0:
            enemy = min(enemies, key=lambda e: self.calculate_distance(e.position))
            enemy.health -= self.attack_power
            if enemy.health <= 0:
                enemies.remove(enemy)

    def use_ability(self):
        # Use the specified ability
        if len(self.abilities) > 0:
            ability = input("Which ability do you want to use? ")
            if ability in self.abilities:
                self.abilities[ability](self)

    def calculate_distance(self, position):
        # Calculate the Euclidean distance between the player and a position
        return ((self.position[0] - position[0]) ** 2 + (self.position[1] - position[1]) ** 2) ** 0.5


class Enemy:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10

    def attack(self, player):
        player.health -= self.attack_power


class Level:
    def __init__(self):
        self.enemies = []

    def is_won(self):
        # Check if all enemies are defeated
        return len(self.enemies) == 0


# Start the game
game = Game()
game.play()
import random


class Game:
    def __init__(self):
        self.world = World()
        self.player = Player()
        self.npcs = [NPC("NPC 1"), NPC("NPC 2"), NPC("NPC 3")]

    def play(self):
        while True:
            # Get the player's input
            action = input("What do you want to do? ")

            # Update the world based on the player's input
            self.world.update(action, self.player)

            # Update NPC behavior based on the player's actions
            for npc in self.npcs:
                npc.update(self.player, self.world.current_level)

            # Check if the player has won the game
            if self.world.is_won():
                print("Congratulations! You have completed the game.")
                break

            # Generate a new level
            self.world.generate_level()

            # Learn from the player's previous actions
            self.world.learn()

            # Print the current player and level information
            print("Player: ", self.player.__dict__)
            print("Current Level: ", self.world.current_level)
            print()

            
class World:
    def __init__(self):
        self.levels = []
        self.current_level = 0

    def update(self, action, player):
        # If the player chooses to move, move them to the next location
        if action == "move":
            player.move()

        # If the player chooses to attack, attack the nearest enemy
        elif action == "attack":
            player.attack(self.levels[self.current_level].enemies)

        # If the player chooses to use an ability, use the ability
        elif action == "ability":
            player.use_ability()

    def generate_level(self):
        # Generate a new level based on the player's previous actions
        level = Level()
        level.enemies = []
        for _ in range(random.randint(1, 5)):
            enemy = Enemy()
            enemy.position = (random.randint(0, 100), random.randint(0, 100))
            level.enemies.append(enemy)
        self.levels.append(level)
        self.current_level += 1

    def learn(self):
        # Learn from the player's previous actions by adjusting the difficulty of the next level
        if self.current_level > 0:
            previous_level = self.levels[self.current_level - 1]
            if previous_level.is_won():
                # If the player won the previous level, make the next level harder
                self.levels[self.current_level].enemies = [
                    enemy for enemy in previous_level.enemies if enemy.health > 0
                ]
            else:
                # If the player lost the previous level, make the next level easier
                for enemy in previous_level.enemies:
                    enemy.health -= 1

    def is_won(self):
        # Check if the player has completed all levels
        return self.current_level >= len(self.levels)


class Player:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10
        self.abilities = {}

    def move(self):
        # Move the player to the specified location
        x = int(input("Enter the x-coordinate: "))
        y = int(input("Enter the y-coordinate: "))
        self.position = (x, y)

    def attack(self, enemies):
        # Attack the nearest enemy
        if len(enemies) > 0:
            enemy = min(enemies, key=lambda e: self.calculate_distance(e.position))
            enemy.health -= self.attack_power
            if enemy.health <= 0:
                enemies.remove(enemy)

    def use_ability(self):
        # Use the specified ability
        if len(self.abilities) > 0:
            ability = input("Which ability do you want to use? ")
            if ability in self.abilities:
                self.abilities[ability](self)

    def calculate_distance(self, position):
        # Calculate the Euclidean distance between the player and a position
        return ((self.position[0] - position[0]) ** 2 + (self.position[1] - position[1]) ** 2) ** 0.5


class Enemy:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10

    def attack(self, player):
        player.health -= self.attack_power


class Level:
    def __init__(self):
        self.enemies = []

    def is_won(self):
        # Check if all enemies are defeated
        return len(self.enemies) == 0


class NPC:
    def __init__(self, name):
        self.name = name
        self.feelings = {"happiness": 0, "anger": 0, "fear": 0}

    def update(self, player, current_level):
        # Update NPC behavior based on the player's actions and current level
        self.feelings["happiness"] += random.randint(1, 5)
        self.feelings["anger"] += random.randint(1, 3)
        self.feelings["fear"] += random.randint(1, 2)
        print(f"{self.name}: {self.feelings}")

    def interact(self, player):
        # Perform an interaction with the player
        pass
class Player:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10
        self.abilities = {}
        self.job = None

    def move(self):
        # Move the player to the specified location
        x = int(input("Enter the x-coordinate: "))
        y = int(input("Enter the y-coordinate: "))
        self.position = (x, y)

    def attack(self, enemies):
        # Attack the nearest enemy
        if len(enemies) > 0:
            enemy = min(enemies, key=lambda e: self.calculate_distance(e.position))
            enemy.health -= self.attack_power
            if enemy.health <= 0:
                enemies.remove(enemy)

    def use_ability(self):
        # Use the specified ability
        if len(self.abilities) > 0:
            ability = input("Which ability do you want to use? ")
            if ability in self.abilities:
                self.abilities[ability](self)

    def calculate_distance(self, position):
        # Calculate the Euclidean distance between the player and a position
        return ((self.position[0] - position[0]) ** 2 + (self.position[1] - position[1]) ** 2) ** 0.5


class NPC:
    def __init__(self, name):
        self.name = name
        self.feelings = {"happiness": 0, "anger": 0, "fear": 0}
        self.job = None

    def update(self, player, current_level):
        # Update NPC behavior based on the player's actions and current level
        self.feelings["happiness"] += random.randint(1, 5)
        self.feelings["anger"] += random.randint(1, 3)
        self.feelings["fear"] += random.randint(1, 2)
        print(f"{self.name}: {self.feelings}")

    def interact(self, player):
        # Perform an interaction with the player
        pass
class Player:
    # ...

    def select_job_class(self):
        # Display job class options and let the player choose
        print("Select your job class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        # ... (add other job class options)

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.job = "Warrior"
            self.attack_power += 10
            # ... (add other stat adjustments or abilities for the Warrior job class)
        elif choice == 2:
            self.job = "Mage"
            # ... (adjust stats and abilities for the Mage job class)
        elif choice == 3:
            self.job = "Rogue"
            # ... (adjust stats and abilities for the Rogue job class)
        # ... (add cases for other job class choices)
class Game:
    # ...

    def play(self):
        while True:
            # Get the player's input
            action = input("What do you want to do? ")

            # Update the world based on the player's input
            self.world.update(action, self.player)

            # Update NPC behavior based on the player's actions
            for npc in self.npcs:
                npc.update(self.player, self.world.current_level)

            # Check if the player has reached level 10
            if self.player.level >= 10 and self.player.job is None:
                self.player.select_job_class()

            # Check if the player has won the game
            if self.world.is_won():
                print("Congratulations! You have completed the game.")
                break

            # ... (rest of the code)
class Player:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10
        self.abilities = {}
        self.job = None
        self.level = 1

    def move(self):
        # Move the player to the specified location
        x = int(input("Enter the x-coordinate: "))
        y = int(input("Enter the y-coordinate: "))
        self.position = (x, y)

    def attack(self, enemies):
        # Attack the nearest enemy
        if len(enemies) > 0:
            enemy = min(enemies, key=lambda e: self.calculate_distance(e.position))
            enemy.health -= self.attack_power
            if enemy.health <= 0:
                enemies.remove(enemy)

    def use_ability(self):
        # Use the specified ability
        if len(self.abilities) > 0:
            ability = input("Which ability do you want to use? ")
            if ability in self.abilities:
                self.abilities[ability](self)

    def calculate_distance(self, position):
        # Calculate the Euclidean distance between the player and a position
        return ((self.position[0] - position[0]) ** 2 + (self.position[1] - position[1]) ** 2) ** 0.5

    def select_job_class(self):
        # Display job class options and let the player choose
        print("Select your job class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        # ... (add other job class options)

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.job = "Warrior"
            self.attack_power += 10
            # ... (add other stat adjustments or abilities for the Warrior job class)
        elif choice == 2:
            self.job = "Mage"
            # ... (adjust stats and abilities for the Mage job class)
        elif choice == 3:
            self.job = "Rogue"
            # ... (adjust stats and abilities for the Rogue job class)
        # ... (add cases for other job class choices)

    def select_ultimate_job_class(self):
        # Display ultimate job class options and let the player choose
        print("Select your ultimate job class:")
        print("1. Berserker")
        print("2. Archmage")
        print("3. Assassin")
        # ... (add other ultimate job class options)

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.job = "Berserker"
            self.attack_power += 20
            # ... (add other stat adjustments or abilities for the Berserker job class)
        elif choice == 2:
            self.job = "Archmage"
            # ... (adjust stats and abilities for the Archmage job class)
        elif choice == 3:
            self.job = "Assassin"
            # ... (adjust stats and abilities for the Assassin job class)
        # ... (add cases for other ultimate job class choices)
class Game:
    # ...

    def play(self):
        while True:
            # Get the player's input
            action = input("What do you want to do? ")

            # Update the world based on the player's input
            self.world.update(action, self.player)

            # Update NPC behavior based on the player's actions
            for npc in self.npcs:
                npc.update(self.player, self.world.current_level)

            # Check if the player has reached level 10
            if self.player.level >= 10 and self.player.job is None:
                self.player.select_job_class()

            # Check if the player has reached level 100
            if self.player.level >= 100 and self.player.job != "Berserker":
                self.player.select_ultimate_job_class()

            # Check if the player has won the game
            if self.world.is_won():
                print("Congratulations! You have completed the game.")
                break

            # ... (rest of the code)
class Player:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10
        self.abilities = {}
        self.job = None
        self.level = 1
        self.sub_job = None

    def move(self):
        # Move the player to the specified location
        x = int(input("Enter the x-coordinate: "))
        y = int(input("Enter the y-coordinate: "))
        self.position = (x, y)

    def attack(self, enemies):
        # Attack the nearest enemy
        if len(enemies) > 0:
            enemy = min(enemies, key=lambda e: self.calculate_distance(e.position))
            enemy.health -= self.attack_power
            if enemy.health <= 0:
                enemies.remove(enemy)

    def use_ability(self):
        # Use the specified ability
        if len(self.abilities) > 0:
            ability = input("Which ability do you want to use? ")
            if ability in self.abilities:
                self.abilities[ability](self)

    def calculate_distance(self, position):
        # Calculate the Euclidean distance between the player and a position
        return ((self.position[0] - position[0]) ** 2 + (self.position[1] - position[1]) ** 2) ** 0.5

    def select_job_class(self):
        # Display job class options and let the player choose
        print("Select your job class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        # ... (add other job class options)

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.job = "Warrior"
            self.attack_power += 10
            # ... (add other stat adjustments or abilities for the Warrior job class)
        elif choice == 2:
            self.job = "Mage"
            # ... (adjust stats and abilities for the Mage job class)
        elif choice == 3:
            self.job = "Rogue"
            # ... (adjust stats and abilities for the Rogue job class)
        # ... (add cases for other job class choices)

    def select_sub_job_class(self):
        # Display sub job class options and let the player choose
        print("Select your sub job class:")
        print("1. Blacksmith")
        print("2. Alchemist")
        print("3. Enchanter")
        # ... (add other sub job class options)

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.sub_job = "Blacksmith"
            # ... (adjust stats and abilities for the Blacksmith sub job class)
        elif choice == 2:
            self.sub_job = "Alchemist"
            # ... (adjust stats and abilities for the Alchemist sub job class)
        elif choice == 3:
            self.sub_job = "Enchanter"
            # ... (adjust stats and abilities for the Enchanter sub job class)
        # ... (add cases for other sub job class choices)


class NPC:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
        self.abilities = {}
        self.job = None
        self.sub_job = None

    def update(self, player, level):
        # Perform NPC behavior based on player actions and level
        if player.position == self.position:
            self.attack(player)

        if level >= 10 and self.job is None:
            self.select_job_class()

        if level >= 50 and self.sub_job is None:
            self.select_sub_job_class()

    def attack(self, player):
        # Attack the player
        player.health -= self.attack_power

    def select_job_class(self):
        # Randomly select an available job class for the NPC
        job_classes = ["Warrior", "Mage", "Rogue", "Blacksmith", "Alchemist", "Enchanter", ...]
        self.job = random.choice(job_classes)
        # ... (adjust stats and abilities based on the selected job class)

    def select_sub_job_class(self):
        # Randomly select an available sub job class for the NPC
        sub_job_classes = ["Blacksmith", "Alchemist", "Enchanter", ...]
        self.sub_job = random.choice(sub_job_classes)
        # ... (adjust stats and abilities based on the selected sub job class)


class Game:
    def __init__(self):
        self.player = Player()
        self.npcs = []
        self.world = World()

    def start(self):
        # Initialize the game world and NPCs
        # ... (initialize the world and NPCs)

        while True:
            # Display game information and prompt player for action
            print("Level:", self.player.level)
            print("Health:", self.player.health)
            print("Position:", self.player.position)
            print("Job:", self.player.job)
            print("Sub Job:", self.player.sub_job)
            # ... (display other relevant information)

            action = input("What do you want to do? ")

            # Update the world based on the player's input
            self.world.update(action, self.player)

            # Update NPC behavior based on the player's actions and level
            for npc in self.npcs:
                npc.update(self.player, self.player.level)

            # Check if the player has reached level 10
            if self.player.level >= 10 and self.player.job is None:
                self.player.select_job_class()

            # Check if the player has reached level 50
            if self.player.level >= 50 and self.player.sub_job is None:
                self.player.select_sub_job_class()

            # Check if the player has won the game
            if self.world.is_won():
                print("Congratulations! You have completed the game.")
                break
import random

class Player:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10
        self.abilities = {}
        self.job = None
        self.level = 1
        self.sub_job = None

    def move(self):
        # Move the player to the specified location
        x = int(input("Enter the x-coordinate: "))
        y = int(input("Enter the y-coordinate: "))
        self.position = (x, y)

    def attack(self, enemies):
        # Attack the nearest enemy
        if len(enemies) > 0:
            enemy = min(enemies, key=lambda e: self.calculate_distance(e.position))
            enemy.health -= self.attack_power
            if enemy.health <= 0:
                enemies.remove(enemy)

    def use_ability(self):
        # Use the specified ability
        if len(self.abilities) > 0:
            ability = input("Which ability do you want to use? ")
            if ability in self.abilities:
                self.abilities[ability](self)

    def calculate_distance(self, position):
        # Calculate the Euclidean distance between the player and a position
        return ((self.position[0] - position[0]) ** 2 + (self.position[1] - position[1]) ** 2) ** 0.5

    def select_job_class(self):
        # Display job class options and let the player choose
        print("Select your job class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        # ... (add other job class options)

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.job = "Warrior"
            self.attack_power += 10
            # ... (add other stat adjustments or abilities for the Warrior job class)
        elif choice == 2:
            self.job = "Mage"
            # ... (adjust stats and abilities for the Mage job class)
        elif choice == 3:
            self.job = "Rogue"
            # ... (adjust stats and abilities for the Rogue job class)
        # ... (add cases for other job class choices)

    def select_sub_job_class(self):
        # Display sub job class options and let the player choose
        print("Select your sub job class:")
        print("1. Blacksmith")
        print("2. Alchemist")
        print("3. Enchanter")
        # ... (add other sub job class options)

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.sub_job = "Blacksmith"
            # ... (adjust stats and abilities for the Blacksmith sub job class)
        elif choice == 2:
            self.sub_job = "Alchemist"
            # ... (adjust stats and abilities for the Alchemist sub job class)
        elif choice == 3:
            self.sub_job = "Enchanter"
            # ... (adjust stats and abilities for the Enchanter sub job class)
        # ... (add cases for other sub job class choices)


class NPC:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = 10
        self.abilities = {}
        self.job = None
        self.sub_job = None

    def update(self, player, level):
        # Perform NPC behavior based on player actions and level
        if player.position == self.position:
            self.attack(player)

        if level >= 10 and self.job is None:
            self.select_job_class()

        if level >= 50 and self.sub_job is None:
            self.select_sub_job_class()

    def attack(self, player):
        # Attack the player
        player.health -= self.attack_power

    def select_job_class(self):
        # Randomly select an available job class for the NPC
        job_classes = ["Warrior", "Mage", "Rogue", ...]  # Add other job classes
        self.job = random.choice(job_classes)
        # ... (adjust stats and abilities based on the selected job class)

    def select_sub_job_class(self):
        # Randomly select an available sub job class for the NPC
        sub_job_classes = ["Blacksmith", "Alchemist", "Enchanter", ...]  # Add other sub job classes
        self.sub_job = random.choice(sub_job_classes)
        # ... (adjust stats and abilities based on the selected sub job class)


class Game:
    def __init__(self):
        self.player = Player()
        self.npcs = []
        self.world = World()

    def start(self):
        # Initialize the game world and NPCs
        # ... (initialize the world and NPCs)

        while True:
            # Display game information and prompt player for action
            print("Level:", self.player.level)
            print("Health:", self.player.health)
            print("Position:", self.player.position)
            print("Job:", self.player.job)
            print("Sub Job:", self.player.sub_job)
            # ... (display other relevant information)

            action = input("What do you want to do? ")

            # Update the world based on the player's input
            self.world.update(action, self.player)

            # Update NPC behavior based on the player's actions and level
            for npc in self.npcs:
                npc.update(self.player, self.player.level)

            # Check if the player has reached level 10
            if self.player.level >= 10 and self.player.job is None:
                self.player.select_job_class()

            # Check if the player has reached level 50
            if self.player.level >= 50 and self.player.sub_job is None:
                self.player.select_sub_job_class()

            # Check if the player has won the game
            if self.world.is_won():
                print("Congratulations! You have completed the game.")
                break
import random

class Player:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10
        self.abilities = {}
        self.job = None
        self.sub_job = None
        self.level = 1
        self.quests = []
        self.pets = []

    def move(self):
        # Move the player to the specified location
        x = int(input("Enter the x-coordinate: "))
        y = int(input("Enter the y-coordinate: "))
        self.position = (x, y)

    def attack(self, enemies):
        # Attack the nearest enemy
        if len(enemies) > 0:
            enemy = min(enemies, key=lambda e: self.calculate_distance(e.position))
            enemy.health -= self.attack_power
            if enemy.health <= 0:
                enemies.remove(enemy)

    def use_ability(self):
        # Use the specified ability
        if len(self.abilities) > 0:
            ability = input("Which ability do you want to use? ")
            if ability in self.abilities:
                self.abilities[ability](self)

    def calculate_distance(self, position):
        # Calculate the Euclidean distance between the player and a position
        return ((self.position[0] - position[0]) ** 2 + (self.position[1] - position[1]) ** 2) ** 0.5

    def select_job_class(self):
        # Display job class options and let the player choose
        print("Select your job class:")
        print("1. Warrior")
        print("2. Mage")
        print("3. Rogue")
        # ... (add other job class options)

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.job = "Warrior"
            self.attack_power += 10
            # ... (add other stat adjustments or abilities for the Warrior job class)
        elif choice == 2:
            self.job = "Mage"
            # ... (adjust stats and abilities for the Mage job class)
        elif choice == 3:
            self.job = "Rogue"
            # ... (adjust stats and abilities for the Rogue job class)
        # ... (add cases for other job class choices)

    def select_sub_job_class(self):
        # Display sub job class options and let the player choose
        print("Select your sub job class:")
        print("1. Blacksmith")
        print("2. Alchemist")
        print("3. Enchanter")
        # ... (add other sub job class options)

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.sub_job = "Blacksmith"
            # ... (adjust stats and abilities for the Blacksmith sub job class)
        elif choice == 2:
            self.sub_job = "Alchemist"
            # ... (adjust stats and abilities for the Alchemist sub job class)
        elif choice == 3:
            self.sub_job = "Enchanter"
            # ... (adjust stats and abilities for the Enchanter sub job class)
        # ... (add cases for other sub job class choices)

    def accept_quest(self, quest):
        # Add the quest to the player's list of active quests
        self.quests.append(quest)
        print("Quest accepted:", quest.name)

    def refuse_quest(self, quest):
        # Refuse the quest and potentially affect the game world
        print("Quest refused:", quest.name)
        quest.on_refuse()

    def complete_quest(self, quest):
        # Complete the quest and receive rewards
        print("Quest completed:", quest.name)
        quest.on_complete(self)

    def level_up(self):
        # Level up the player and adjust stats and abilities accordingly
        self.level += 1
        self.health += 10
        self.attack_power += 5
        # ... (adjust other stats and abilities based on the player's level)

        # Check if the player has reached the level requirement for selecting a job class
        if self.level == 10 and self.job is None:
            self.select_job_class()

        # Check if the player has reached the level requirement for selecting a sub job class
        if self.level == 50 and self.sub_job is None:
            self.select_sub_job_class()

        # Check if the player has reached the level requirement for obtaining a pet
        if self.level == 25:
            self.obtain_pet()

    def obtain_pet(self):
        # Add a pet to the player's collection
        print("Congratulations! You have obtained a pet.")
        # ... (add code to obtain a pet)

class NPC:
    def __init__(self, position):
        self.position = position

    def interact(self, player):
        # Display NPC interaction options and let the player choose
        print("1. Talk")
        print("2. Accept Quest")
        print("3. Refuse Quest")
        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.talk()
        elif choice == 2:
            self.offer_quest(player)
        elif choice == 3:
            self.refuse_quest(player)

    def talk(self):
        # Display dialogue or information from the NPC
        print("NPC: Welcome, traveler!")

    def offer_quest(self, player):
        # Create and offer a quest to the player
        quest = Quest("Save the Village", self)
        player.accept_quest(quest)

    def refuse_quest(self, player):
        # Inform the player that the quest was refused
        print("NPC: Very well. If you change your mind, let me know.")

class SpecialNPC(NPC):
    def __init__(self, position, hidden_job_class):
        super().__init__(position)
        self.hidden_job_class = hidden_job_class

    def talk(self):
        # Display dialogue or information from the special NPC
        print("Special NPC: Greetings, adventurer!")

    def offer_quest(self, player):
        # Create and offer a quest related to the hidden job class
        quest = HiddenJobQuest("Mysterious Artifact", self.hidden_job_class, self)
        player.accept_quest(quest)

class Quest:
    def __init__(self, name, npc):
        self.name = name
        self.npc = npc

    def on_complete(self, player):
        # Perform actions when the quest is completed
        pass

    def on_refuse(self):
        # Perform actions when the quest is refused
        pass

class HiddenJobQuest(Quest):
    def __init__(self, name, hidden_job_class, npc):
        super().__init__(name, npc)
        self.hidden_job_class = hidden_job_class

    def on_complete(self, player):
        # Unlock the hidden job class for the player
        player.sub_job = self.hidden_job_class
        print("Congratulations! You have unlocked the", self.hidden_job_class, "sub job class.")

class Pet:
    def __init__(self, name):
        self.name = name

# Game initialization
player = Player()
npc1 = NPC((2, 3))
special_npc = SpecialNPC((4, 5), "Shadowmancer")

# Game loop
while True:
    # Check if the player is close to an NPC
    if player.calculate_distance(npc1.position) <= 1:
        npc1.interact(player)
    elif player.calculate_distance(special_npc.position) <= 1:
        special_npc.interact(player)

    # Perform other game logic...

    # Level up the player if necessary
    if player.level < 100:
        player.level_up()

    # Check if the player wants to move
    move_choice = input("Do you want to move? (yes/no) ")
    if move_choice.lower() == "yes":
        player.move()

    # Check if the player wants to attack
    attack_choice = input("Do you want to attack? (yes/no) ")
    if attack_choice.lower() == "yes":
        player.attack(enemies)

    # Check if the player wants to use an ability
    ability_choice = input("Do you want to use an ability? (yes/no) ")
    if ability_choice.lower() == "yes":
        player.use_ability()

    # Perform other game logic...
import random

class Player:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10
        self.abilities = {}
        self.job = None
        self.sub_job = None
        self.level = 1
        self.quests = []
        self.pets = []

    def move(self):
        # Move the player to the specified location
        x = int(input("Enter the x-coordinate: "))
        y = int(input("Enter the y-coordinate: "))
        self.position = (x, y)

    def attack(self, enemies):
        # Attack the nearest enemy
        if len(enemies) > 0:
            enemy = min(enemies, key=lambda e: self.calculate_distance(e.position))
            enemy.health -= self.attack_power
            if enemy.health <= 0:
                enemies.remove(enemy)

    def use_ability(self):
        # Use the specified ability
        if len(self.abilities) > 0:
            ability = input("Which ability do you want to use? ")
            if ability in self.abilities:
                self.abilities[ability](self)

    def calculate_distance(self, position):
        # Calculate the Euclidean distance between the player and a position
        return ((self.position[0] - position[0]) ** 2 + (self.position[1] - position[1]) ** 2) ** 0.5

    def select_job_class(self):
        # Display job class options and let the player choose
        print("Select your job class:")
        print("1. Knight")
        print("2. Wizard")
        print("3. Archer")

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.job = "Knight"
            self.attack_power += 10
            # ... (add other stat adjustments or abilities for the Knight job class)
        elif choice == 2:
            self.job = "Wizard"
            # ... (adjust stats and abilities for the Wizard job class)
        elif choice == 3:
            self.job = "Archer"
            # ... (adjust stats and abilities for the Archer job class)

    def select_sub_job_class(self):
        # Display sub job class options and let the player choose
        print("Select your sub job class:")
        print("1. Blacksmith")
        print("2. Alchemist")
        print("3. Enchanter")
        # ... (add other sub job class options)

        choice = int(input("Enter the number of your choice: "))

        if choice == 1:
            self.sub_job = "Blacksmith"
            # ... (adjust stats and abilities for the Blacksmith sub job class)
        elif choice == 2:
            self.sub_job = "Alchemist"
            # ... (adjust stats and abilities for the Alchemist sub job class)
        elif choice == 3:
            self.sub_job = "Enchanter"
            # ... (adjust stats and abilities for the Enchanter sub job class)

    def accept_quest(self, quest):
        # Add the quest to the player's list of active quests
        self.quests.append(quest)
        print("Quest accepted:", quest.name)

    def refuse_quest(self, quest):
        # Refuse the quest and potentially affect the game world
        print("Quest refused:", quest.name)
        quest.on_refuse()

    def complete_quest(self, quest):
        # Complete the quest and receive rewards
        print("Quest completed:", quest.name)
        quest.on_complete(self.
class God:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
greek_gods = [
    God("Zeus", 500, 50),
    God("Hera", 400, 40),
    God("Poseidon", 450, 45),
    # Add other Greek gods as desired
]

egyptian_gods = [
    God("Ra", 550, 55),
    God("Isis", 350, 35),
    God("Anubis", 400, 40),
    # Add other Egyptian gods as desired
]
class Player:
    def __init__(self):
        self.position = (0, 0)
        self.health = 100
        self.attack_power = 10
        self.abilities = {}
        self.job = None
        self.sub_job = None
        self.level = 1
        self.quests = []
        self.pets = []
        self.faction = None  # New attribute to store the player's faction

    # Rest of the class code...
def choose_faction(self):
    print("Select your faction:")
    print("1. Greek Pantheon")
    print("2. Egyptian Pantheon")

    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        self.faction = "Greek"
    elif choice == 2:
        self.faction = "Egyptian"
def accept_quest(self, quest):
    if quest.god_faction == self.faction:
        self.quests.append(quest)
        print("Quest accepted:", quest.name)
    else:
        print("You cannot accept this quest with your current faction.")
god_quests = [
    GodQuest("Retrieve Zeus's Lightning Bolt", "Greek", {'health': 20, 'attack_power': 10}),
    GodQuest("Find the Book of Thoth", "Egyptian", {'health': 15, 'attack_power': 12}),
    # Add other god quests as desired
]
class Pet:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
class Monster:
    def __init__(self, name, health, attack_power, level):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.level = level
# Normal Pet Monsters
wolf = Pet("Wolf", 80, 20)
owl = Pet("Owl", 60, 15)
panther = Pet("Panther", 90, 25)
sprite = Pet("Sprite", 70, 18)
baby_dragon = Pet("Baby Dragon", 100, 30)
imp = Pet("Imp", 75, 22)
treant_sapling = Pet("Treant Sapling", 85, 23)
fairy = Pet("Fairy", 65, 17)
baby_phoenix = Pet("Baby Phoenix", 95, 28)
elemental_golem = Pet("Elemental Golem", 110, 35)

# Rare Pet Monsters
direwolf = Pet("Direwolf", 120, 40)
griffin = Pet("Griffin", 140, 45)
sabertooth_tiger = Pet("Sabertooth Tiger", 130, 42)
nymph = Pet("Nymph", 110, 38)
wyvern = Pet("Wyvern", 150, 50)
shadow_stalker = Pet("Shadow Stalker", 125, 43)
ancient_ent = Pet("Ancient Ent", 160, 55)
sylph = Pet("Sylph", 135, 46)
fire_drake = Pet("Fire Drake", 170, 60)
stone_golem = Pet("Stone Golem", 180, 65)

# Hidden Pet Monsters
celestial_pegasus = Pet("Celestial Pegasus", 200, 70)
astral_serpent = Pet("Astral Serpent", 220, 75)
ghostly_specter = Pet("Ghostly Specter", 210, 73)
eldritch_horror = Pet("Eldritch Horror", 240, 80)
crystal_unicorn = Pet("Crystal Unicorn", 230, 78)
void_elemental = Pet("Void Elemental", 250, 85)
ancient_sphinx = Pet("Ancient Sphinx", 260, 88)
lunar_guardian = Pet("Lunar Guardian", 240, 82)
time_wraith = Pet("Time Wraith", 270, 90)
divine_beast = Pet("Divine Beast", 280, 95)

# Ultimate Pet Monsters
legendary_dragon = Pet("Legendary Dragon", 300, 100)
chaos_behemoth = Pet("Chaos Behemoth", 350, 110)
primordial_titan = Pet("Primordial Titan", 400, 120)
archangel = Pet("Archangel", 380, 115)
nightmare_leviathan = Pet("Nightmare Leviathan", 420, 125)
demigod = Pet("Demigod", 400, 120)
world_ender = Pet("World Ender", 450, 130)
eternal_phoenix = Pet("Eternal Phoenix", 430, 126)
cosmic_elemental = Pet("Cosmic Elemental", 470, 135)
divine_ascendant = Pet("Divine Ascendant", 500, 150)

# Enemy Monsters
enemy_monsters = [
    Monster("Goblin", 50, 10, 1),
    Monster("Orc", 70, 15, 2),
    Monster("Troll", 90, 20, 3),
    Monster("Dragon", 120, 25, 4),
    Monster("Demon Lord", 150, 30, 5),
    Monster("Behemoth", 180, 35, 6),
    Monster("Lich King", 210, 40, 7),
    Monster("Titan", 240, 45, 8),
    Monster("Ancient Dragon", 270, 50, 9),
    Monster("Chaos God", 300, 55, 10),
]
class Player:
    def __init__(self, name, race, pet):
        self.name = name
        self.race = race
        self.pet = pet

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print("Pet:")
        self.pet.describe()


class NPC:
    def __init__(self, name, race, pet, role):
        self.name = name
        self.race = race
        self.pet = pet
        self.role = role

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print("Pet:")
        self.pet.describe()
        print(f"Role: {self.role}")


class Pet:
    def __init__(self, name, species, abilities):
        self.name = name
        self.species = species
        self.abilities = abilities

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print("Abilities:")
        for ability in self.abilities:
            print("- " + ability)


# Creating player and NPC instances
player = Player("PlayerName", "Human", pet)
npc = NPC("NPCName", "Elf", pet, "Merchant")

# Describing player and NPC
print("Player:")
player.describe()
print("\nNPC:")
npc.describe()
