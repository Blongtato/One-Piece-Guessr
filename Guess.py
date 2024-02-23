import CharacterInfo as ci
import random
def compare(x, y):  # Compares character selected by user to actual character by each attribute
    # Height Comparison
    if x.height > y.height:
        height_var = "Shorter"
    elif x.height < y.height:
        height_var = "Taller"
    else:
        height_var = "Correct!"
    # Faction Comparison
    if x.faction == y.faction:
        fact_var = "Correct!"
    elif x.faction[0] == y.faction[0]:
        fact_var = "Close"
    else:
        fact_var = "Incorrect"
    # Debut Arc Comparison
    if x.debut > y.debut:
        deb_var = "Earlier"
    elif x.debut < y.debut:
        deb_var = "Later"
    else:
        deb_var = "Correct!"
    # Origin Comparison
    if x.origin == y.origin:
        or_var = "Correct!"
    elif x.origin[0] == y.origin[0]:
        or_var = "Close"
    else:
        or_var = "Incorrect"
    # Race Comparison
    if x.race == y.race:
        race_var = "Correct!"
    else:
        race_var = "Incorrect"
    # Haki Comparison
    if x.haki > y.haki:
        haki_var = "Less"
    elif x.haki < y.haki:
        haki_var = "More"
    else:
        haki_var = "Correct!"
    # Devil Fruit Comparison
    if x.df_type == y.df_type:
        df_var = "Correct!"
    else:
        df_var = "Incorrect"
    # Prints out comparisons
    print(f"|Height: {x.height}m, {height_var}|\n"
          f"|Group: {x.faction[0]}({x.faction[1]}), {fact_var}|\n"
          f"|Debut Arc: {ci.arcs[x.debut]}, {deb_var}|\n"
          f"|Origin: {x.origin[0]}({x.origin[1]}), {or_var}|\n"
          f"|Race/Tribe: {x.race}, {race_var}|\n"
          f"|Haki: {x.haki} forms, {haki_var}|\n"
          f"|Devil Fruit: {x.df_type}, {df_var}|")

# User inputs character guess and chooses a random character from list
guess = input("Input first character : ")
answer = random.choice(ci.names)

while guess != answer:
    try:
        compare(ci.people[guess], ci.people[answer])
    except:
        print("Name not found.")
    guess = input("Next one? ")
print("Good Job!")
