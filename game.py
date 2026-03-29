import random

# Define constants
MAP_SIZE = 10
NUM_PLAYERS = 5
MAX_HEALTH = 100

# Define player class
class Player:
    def __init__(self, name):
        self.name = name
        self.health = MAX_HEALTH
        self.position = (random.randint(0, MAP_SIZE-1), random.randint(0, MAP_SIZE-1))

# Generate players
players = [Player(f"Player {i+1}") for i in range(NUM_PLAYERS)]

# Game loop
while len(players) > 1:
    # Display players and their positions
    print("\nCurrent positions:")
    for player in players:
        print(f"{player.name}: {player.position}")

    # Simulate movement
    for player in players:
        # Move player randomly
        movement = random.choice(['up', 'down', 'left', 'right'])
        if movement == 'up':
            player.position = (player.position[0], max(player.position[1] - 1, 0))
        elif movement == 'down':
            player.position = (player.position[0], min(player.position[1] + 1, MAP_SIZE - 1))
        elif movement == 'left':
            player.position = (max(player.position[0] - 1, 0), player.position[1])
        elif movement == 'right':
            player.position = (min(player.position[0] + 1, MAP_SIZE - 1), player.position[1])

        # Simulate damage from being outside the map
        if player.position[0] < 0 or player.position[0] >= MAP_SIZE or \
           player.position[1] < 0 or player.position[1] >= MAP_SIZE:
            player.health -= 10
            print(f"{player.name} took 10 damage from being outside the map!")

        # Simulate other players encountering each other
        for other_player in players:
            if other_player != player and other_player.position == player.position:
                print(f"{player.name} and {other_player.name} encountered each other!")
                player.health -= 20
                other_player.health -= 20

    # Remove defeated players
    players = [player for player in players if player.health > 0]

# Display winner
print(f"\n{players[0].name} wins the game!")
