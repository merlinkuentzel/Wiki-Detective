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


def player_round_run(note, solution, answers):
    """function for entering answers, checking them, and calculating scores"""
    answer_count = 0

    print(note)

    for key, val in answers.items():
        print(f"{key}: {val}")
    print()

    while True:
        try:
            guess = input("Was wird gesucht: ").upper()
            if guess not in answers:
                raise ValueError
            print()
            result = answers[guess]
            break
        except ValueError:
            print("Bitte wähle zwischen A-D")

    if result == solution:
        print(f"Rictige Antwort: {solution} ist gesucht!")
        print("---------------------------")
        print()
        answer_count += 1
    else:
        print("Deine Antwort ist falsch!")
        print("---------------------------")
        print()

    return answer_count


def generate_answers(solution):
    """function for creating answer choices"""
    possible_answers = BERLIN_SIGHTS.copy()
    possible_answers.remove(solution)
    letters = ["A", "B", "C", "D"]

    sights = random.sample(possible_answers, 3)
    sights.append(solution)

    random.shuffle(sights)
    answers_options = dict(zip(letters, sights))

    return answers_options


def suggest(notes):
    """function for creating the tip"""
    selected_notes = random.choice(notes)
    return selected_notes


def player_round_start(player):
    """function for generating the solution"""
    print(f"{player} deine runde startet: ")
    print()
    choose_quiz = random.choice(BERLIN_SIGHTS)
    return choose_quiz


def player_info(number_of_player):
    """function to collect player names"""
    name_of_players = []

    for num in range(number_of_player):
        player = input(f"Spieler {num + 1}: Gib deinen Namen ein: ")
        name_of_players.append(player)

    return name_of_players


def start_game():
    """function to control the game"""
    while True:
        try:
            num_player = int(input("Wieviele Spieler gibt es: "))
            if num_player <= 0:
                raise ValueError
            else:
                break
        except ValueError:
            print("Bitte gebe eine Zahl ein!")

    player_list = player_info(num_player)
    player_scores = {}

    for player in player_list:
        player_scores[player] = 0
        for round_num in range(3):
            start_quiz = player_round_start(player)
            answers = generate_answers(start_quiz)
            sights_sentence = wiki_api.wiki_article(start_quiz)
            notes = suggest(sights_sentence)
            rating_player_round = player_round_run(notes, start_quiz, answers)
            player_scores[player] += rating_player_round

    score_set = set(player_scores.values())
    highest_score = sorted(score_set, reverse=True)

    print("Das Ergebniss:")
    for score in highest_score:
        for key, val in player_scores.items():
            if val == score:
                print(f"{key}: {val}")

