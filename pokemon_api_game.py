# Pokemon API Game
import requests
from random import randrange

# randomly generate id for pokemon_api from first gen pokemon (1 to 151)
id1 = str(randrange(1, 152))
id2 = str(randrange(1, 152))

# requests to the pokemon_api api to retrieve data
pokemon_api = "https://pokeapi.co/api/v2/pokemon/"

p1_poke = requests.get(pokemon_api + id1)  # player 1
p2_poke = requests.get(pokemon_api + id2)  # player 2 or CPU

p1_poke_name = p1_poke.json()['name'].capitalize()  # player 1 pokemon name
p2_poke_name = p2_poke.json()['name'].capitalize()  # player 2 pokemon name

p1_health = p1_poke.json()['stats'][0]['base_stat']  # player 1 pokemon health
p2_health = p2_poke.json()['stats'][0]['base_stat']  # player 2 pokemon health

print("============================================\n"
      "------------- Pokemon API Game -------------\n"
      "============================================")
# Ask user for single or two player
while True:
    mode = input("Which game mode do you want to play?\n"
                 "1 - Single player\n"
                 "2 - Two player\n")
    # Single player mode
    if mode == "1":
        print(f"============================================\n"
              f"CPU wants to fight!\n"
              f"CPU sent out {p2_poke_name}!\t[HP = {p2_health}]\n"
              f"You sent out {p1_poke_name}!\t[HP = {p1_health}]\n"
              f"============================================\n"
              f"------------------ Fight! ------------------\n"
              f"============================================")
        while True:
            move = randrange(1, 5)
            cpu_poke_move = p2_poke.json()['moves'][move]['move']  # cpu random move
            cpu_move_power = requests.get(cpu_poke_move['url']).json()["power"]
            if cpu_move_power is None:
                cpu_move_power = 0
            try:
                move_select = int(input(f"Select a move to use:\n"
                                        f"1 - {p1_poke.json()['moves'][0]['move']['name']}\n"
                                        f"2 - {p1_poke.json()['moves'][1]['move']['name']}\n"
                                        f"3 - {p1_poke.json()['moves'][2]['move']['name']}\n"
                                        f"4 - {p1_poke.json()['moves'][3]['move']['name']}\n"))
                if 0 < move_select <= 4:
                    p1_poke_move = p1_poke.json()['moves'][move_select - 1]['move']  # player 1 pokemon move
                    p1_move_power = requests.get(p1_poke_move['url']).json()["power"]
                    if p1_move_power is None:
                        p1_move_power = 0
                    print(f"============================================\n"
                          f"{p1_poke_name} used {p1_poke_move['name']}! [Damage = {p1_move_power}]")

                    if p1_move_power >= p2_health:
                        print(f"It was super effective, {p2_poke_name} fainted!\n"
                              f"============================================\n"
                              f"----------- You are the winner! ------------\n"
                              f"============================================")
                        break
                    print(f"============================================\n"
                          f"{p2_poke_name} used {cpu_poke_move['name']}! [Damage = {cpu_move_power}]")

                    if cpu_move_power >= p1_health:
                        print(f"It was super effective, {p1_poke_name} fainted!\n"
                              f"============================================\n"
                              f"------------ CPU is the winner! ------------\n"
                              f"============================================")
                        break
                    else:
                        p2_health -= p1_move_power
                        p1_health -= cpu_move_power
                        print(f"============================================\n"
                              f"Results: {p1_poke_name} took {cpu_move_power} damage. [HP = {p1_health}]\n"
                              f"         {p2_poke_name} took {p1_move_power} damage. [HP = {p2_health}]\n"
                              f"============================================")
                        continue
                else:
                    print("============================================\n"
                          "- Please select a valid move (1, 2, 3 or 4) \n"
                          "============================================")
                    continue
            except ValueError:
                print("============================================\n"
                      "- Please select a valid move (1, 2, 3 or 4) \n"
                      "============================================")
                continue
        break

    # Two player mode
    elif mode == "2":
        print(f"============================================\n"
              f"Player 1 sent out {p1_poke_name}!\t[HP = {p1_health}]\n"
              f"Player 2 sent out {p2_poke_name}!\t[HP = {p2_health}]\n"
              f"============================================\n"
              f"------------------ Fight! ------------------\n"
              f"============================================")
        while True:
            try:
                move_select1 = int(input(f"Player 1, select a move:\n"
                                         f"1 - {p1_poke.json()['moves'][0]['move']['name']}\n"
                                         f"2 - {p1_poke.json()['moves'][1]['move']['name']}\n"
                                         f"3 - {p1_poke.json()['moves'][2]['move']['name']}\n"
                                         f"4 - {p1_poke.json()['moves'][3]['move']['name']}\n"))
                if 0 < move_select1 <= 4:
                    p1_poke_move = p1_poke.json()['moves'][move_select1 - 1]['move']  # player 1 pokemon move
                    p1_move_power = requests.get(p1_poke_move['url']).json()["power"]
                    if p1_move_power is None:
                        p1_move_power = 0
                    # print(f"{p1_poke_name} used {p1_poke_move['name']}! (Damage={p1_move_power})")
                else:
                    print("============================================\n"
                          "- Please select a valid move (1, 2, 3 or 4) \n"
                          "============================================")
                    continue
            except ValueError:
                print("============================================\n"
                      "- Please select a valid move (1, 2, 3 or 4) \n"
                      "============================================")
                continue
            try:
                move_select2 = int(input(f"============================================\n"
                                         f"Player 2, select a move:\n"
                                         f"1 - {p2_poke.json()['moves'][0]['move']['name']}\n"
                                         f"2 - {p2_poke.json()['moves'][1]['move']['name']}\n"
                                         f"3 - {p2_poke.json()['moves'][2]['move']['name']}\n"
                                         f"4 - {p2_poke.json()['moves'][3]['move']['name']}\n"))
                if 0 < move_select2 <= 4:
                    p2_poke_move = p2_poke.json()['moves'][move_select2 - 1]['move']  # player 1 pokemon move
                    p2_move_power = requests.get(p2_poke_move['url']).json()["power"]
                    if p2_move_power is None:
                        p2_move_power = 0
                    # print(f"{p2_poke_name} used {p2_poke_move['name']}! (Damage={p2_move_power})")
                else:
                    print("============================================\n"
                          "- Please select a valid move (1, 2, 3 or 4) \n"
                          "============================================")
                    continue
            except ValueError:
                print("============================================\n"
                      "- Please select a valid move (1, 2, 3 or 4) \n"
                      "============================================")
                continue
            print(f"============================================\n"
                  f"{p1_poke_name} used {p1_poke_move['name']}! [Damage = {p1_move_power}]")
            if p1_move_power >= p2_health:
                print(f"It was super effective, {p2_poke_name} fainted!\n"
                      f"============================================\n"
                      f"--------- Player 1 is the winner! ----------\n"
                      f"============================================")
                break
            print(f"============================================\n"
                  f"{p2_poke_name} used {p2_poke_move['name']}! [Damage = {p2_move_power}]")
            if p2_move_power >= p1_health:
                print(f"It was super effective, {p1_poke_name} fainted!\n"
                      f"============================================\n"
                      f"--------- Player 2 is the winner! ----------\n"
                      f"============================================")
                break
            else:
                p2_health -= p1_move_power
                p1_health -= p2_move_power
                print(f"============================================\n"
                      f"Results: {p1_poke_name} took {p2_move_power} damage. [HP = {p1_health}]\n"
                      f"         {p2_poke_name} took {p1_move_power} damage. [HP = {p2_health}]\n"
                      f"============================================")
        break

    # Re-prompt user for valid game mode
    else:
        print("============================================\n"
              "- Please select a valid game mode (1 or 2) -\n"
              "============================================")
        continue
