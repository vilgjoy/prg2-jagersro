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
       print("bad stats, försök igen")
       player_horse["speed"] = 0
       player_horse["agility"] = 0

print(player_horse)

ai_horse = {
    "name": "NPC",
    "speed": 0,
    "agility": 0
    }


while True:
    random_speed = random.randint(1, 6)
    random_agility = 8 - random_speed
    if 1 <= random_agility <= 6:
        ai_horse["speed"] = random_speed
        ai_horse["agility"] = random_agility
        break

print("NPC:s häst:", ai_horse)
