import wiki_api
import random

BERLIN_SIGHTS = ["Brandenburger Tor",
    "Berliner Fernsehturm",
    "Reichstagsgebäude",
    "Berliner Dom",
    "Siegessäule",
    "East Side Gallery",
    "Schloss Charlottenburg",
    "Checkpoint Charlie"]

def point_count(player, points):
    player_points = {}

    if points == 0:
        player_points[player] = 2
    elif points == 1:
        player_points[player] = 1
    else:
        player_points[player] = 0

    return player_points

def player_round_run(gameplay_rounds, solution):
    answer_count = 0

    for round in gameplay_rounds:
        print(round)
        guess = input("witch sights is it?: ")
        if guess == solution:
            break
        else:
            print("your answer ist wrong")
            answer_count += 1

    return answer_count

def suggest(notes):
    selected_notes = random.sample(notes, 3)
    return selected_notes


def player_round_start(player):
    print(f"{player} start round: ")
    choose_quiz = random.choice(BERLIN_SIGHTS)
    return choose_quiz


def player_info(number_of_player):
    name_of_players = []

    for num in range(number_of_player):
        player = input(f"Player {num + 1}: Enter your Name: ")
        name_of_players.append(player)

    return name_of_players


def start_game():
    while True:
        try:
            num_player = int(input("How many player want to play: "))
            num_round = int(input("How many rounds do you want to play: "))
            if num_player <= 0  or num_round <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please enter a number!")

    player_list = player_info(num_player)
    for num in range(num_round):
        for player in player_list:
            start_quiz = player_round_start(player)
            sights_sentence = wiki_api.wiki_article(start_quiz)
            notes = suggest(sights_sentence)
            game_run = notes
            rating_player_round = player_round_run(game_run, start_quiz)
            print(point_count(player,rating_player_round))
