import random

print("Skapa din häst!")

player_horse = {
    "name": "",
    "speed": 0,
    "agility": 0
}


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


player_horse["name"] = input('Vad ska din häst heta: ')
print("Din häst har speed och agility, max 6 i en stat, max totalt 8 totalt")
stats_ok = False
while stats_ok == False:
    while player_horse["speed"] < 1 or player_horse["speed"] > 6:
        player_horse["speed"] = input_int("Hur snabbt är din häst(1-6): ")
    while player_horse["agility"] < 1 or player_horse["agility"] > 6:
        player_horse["agility"] = input_int("Hur smidig är din häst(1-6): ")

    if player_horse["speed"] + player_horse["agility"] == 8:
        stats_ok = True
    else:
        print("Bad stats, försök igen")
        player_horse["speed"] = 0
        player_horse["agility"] = 0


def create_computer_horse():
    speed = random.randint(2, 6)
    name_parts = ["ai", "tech", "lord", "evil",
                  "clanker", "pony", "horse", "oat", "leaf", "ship"]
    horse = {
        "name": random.choice(name_parts).capitalize() + "" + random.choice(name_parts),
        "speed": speed,
        "agility": 8-speed
    }
    return horse


computer_horse = create_computer_horse()
###################################################################
print(player_horse)
print(computer_horse)


def game_turn():
    player_speed = player_horse["speed"] + random.randint(1, 6)
    player_agility = player_horse["agility"] - random.randint(1, 6)
    if player_agility >= 0:
        player_speed -= player_agility
    computer_speed = computer_horse["speed"] + random.randint(1, 6)
    computer_agility = random.randint(1, 6) - computer_horse["agility"]
    if computer_agility >= 0:
        computer_speed -= computer_agility
    print(
        f"Spelarens häst {player_horse['name']} springer {player_speed} steg")
    print(
        f"Datorns häst {computer_horse['name']} springer {computer_speed} steg")
    return [player_speed, computer_speed]


player_steps = 0
computer_steps = 0
for i in range(10):
    steps = game_turn()
    player_steps += steps[0]
    computer_steps += steps[1]

print(f"Antal steg: player {player_steps}, computer {computer_steps}")
