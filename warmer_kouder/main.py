import random

def pick_random_number(bereik):
    random_number = random.randint(1, bereik)
    return random_number

def get_value(text, data_type):
    while True:
        try:
            return data_type(input(text))
        except:
            print("Dit is een incorrect datatype, probeer het opnieuw!")

def pick_difficulty():
    print("Welkom bij Warmer-Kouder.")
    print("Raad welk nummer het is terwijl wij je vertellen of het warmer of kouder is.")
    print("Op welke difficulty wil je spelen?")
    print("1) makkelijk (10 pogingen, nummer tussen 1 en 100)")
    print("2) normaal (6 pogingen, nummer tussen 1 en 100)")
    print("3) moeilijk (10 pogingen, nummer tussen 1 en 1000)")

    choice = get_value("", int)

    if choice == 1:
        pogingen = 10
        bereik = 100
    elif choice == 2:
        pogingen= 6
        bereik = 100
    elif choice == 3:
        pogingen = 10
        bereik= 1000

    return pogingen, bereik
  
  
def input_number(pogingen, random_number):
    iteration = 0
    while True:
        iteration += 1

        if iteration > pogingen:
            print(f"je hebt geen guesses meer... het goede nummer was {random_number}")
            return iteration

        guess = get_value(f"Wat is je {iteration}e guess?: ", int)

        if guess < random_number:
            print("Die guess was koud... het nummer is hoger")
        elif guess > random_number:
            print("Die guess was warm... het nummer is lager")
        else:
            print("Je hebt het goed!!")
            return iteration
    
def update_highscores(name, score, filename="highscores.txt"):
    try:
        with open(filename, "r") as f:
            scores = []
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    n, s = parts
                    scores.append((n, int(s)))
    except FileNotFoundError:
        scores = []

    scores.append((name, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    with open(filename, "w") as f:
        for n, s in scores:
            f.write(f"{n} {s}\n")

    return scores
    
def vraag_speler_naam():
    name = get_value("Please enter name: ", str)
    return name

def bereken_score(pogingen, iteration):
    score = pogingen - iteration
    return score

pogingen, bereik = pick_difficulty()
random_number = pick_random_number(bereik)
iteration = input_number(pogingen, random_number)
name = vraag_speler_naam()
score = bereken_score(pogingen, iteration)
update_highscores(name, score)
