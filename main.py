import game_logic

def main():
    print("---------------------------")
    print("Willkommen zu Wiki-Berlin!")
    print("---------------------------")
    print("In diesem kleinen Ratespiel geht es darum, anhand von Tips, eine kleine Auswahl berühmte Berliner Sehenswürdigkeiten zu erraten.")
    print("Am anfang entscheidet Ihr, wie viele Spieler es geben wird und wie viele Runden ihr spielt.")
    print("Anschließend Spielt Ihr der Reihe nach. Es beginnt Spieler 1 und jeder spieler hat Runden, um Sehenswürdigkeiten zu erraten")
    print("Sollte es weiter Spieler geben, geht es mit Spieler 2 weiter")
    print("Für jede richtige Antwort gibt es ein Punkt")
    print("Der Spieler mit den meisten Punkten gewinnt")
    print("---------------------------")
    print("Möge der klügere Spieler gewinne :P")
    print()
    game_logic.start_game()

if __name__ == "__main__":
    main()