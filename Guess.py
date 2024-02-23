import CharacterInfo as ci
import random
def compare(personGuess, personAnswer):  # Compares character selected by user to actual character by each attribute
    # Height Comparison
    if personGuess.height > personAnswer.height:
        height_var = "Shorter"
    elif personGuess.height < personAnswer.height:
        height_var = "Taller"
    else:
        height_var = "Correct!"
    # Faction Comparison
    if personGuess.faction == personAnswer.faction:
        fact_var = "Correct!"
    elif personGuess.faction[0] == personAnswer.faction[0]:
        fact_var = "Close"
    else:
        fact_var = "Incorrect"
    # Debut Arc Comparison
    if personGuess.debut > personAnswer.debut:
        deb_var = "Earlier"
    elif personGuess.debut < personAnswer.debut:
        deb_var = "Later"
    else:
        deb_var = "Correct!"
    # Origin Comparison
    if personGuess.origin == personAnswer.origin:
        or_var = "Correct!"
    elif personGuess.origin[0] == personAnswer.origin[0]:
        or_var = "Close"
    else:
        or_var = "Incorrect"
    # Race Comparison
    if personGuess.race == personAnswer.race:
        race_var = "Correct!"
    else:
        race_var = "Incorrect"
    # Haki Comparison
    if personGuess.haki > personAnswer.haki:
        haki_var = "Less"
    elif personGuess.haki < personAnswer.haki:
        haki_var = "More"
    else:
        haki_var = "Correct!"
    # Devil Fruit Comparison
    if personGuess.df_type == personAnswer.df_type:
        df_var = "Correct!"
    else:
        df_var = "Incorrect"
    # Prints out comparisons
    print(f"|Height: {personGuess.height}m, {height_var}|\n"
          f"|Group: {personGuess.faction[0]}({personGuess.faction[1]}), {fact_var}|\n"
          f"|Debut Arc: {ci.arcs[personGuess.debut]}, {deb_var}|\n"
          f"|Origin: {personGuess.origin[0]}({personGuess.origin[1]}), {or_var}|\n"
          f"|Race/Tribe: {personGuess.race}, {race_var}|\n"
          f"|Haki: {personGuess.haki} forms, {haki_var}|\n"
          f"|Devil Fruit: {personGuess.df_type}, {df_var}|")


# User inputs character guess and chooses a random character from list
guess = input("Input first character : ")
answer = random.choice(ci.names)

while guess != answer:
    try:
        compare(ci.people[guess], ci.people[answer])
    except KeyError:
        print("Name not found.")
    guess = input("Next one? ")
print("Good Job!")
