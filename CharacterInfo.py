class Character:
    # Constructor assigns class attributes
    def __init__(self, height, faction, debut, origin, race, haki, df_type):
        self.height = height
        self.faction = faction
        self.debut = debut
        self.origin = origin
        self.race = race
        self.haki = haki
        self.df_type = df_type

    # Prints out attributes of Class
    def print_info(self):
        print(self.height, self.faction, self.debut, self.origin, self.race, self.haki, self.df_type)

# List holds all story arcs so they can be accessed by index
arcs = ["Romance Dawn", "Orange Town", "Syrup Village", "Baratie", "Arlong Park", "Loguetown", "Reverse Mountain",
        "Whisky Peak", "Little Garden", "Drum Island", "Alabasta", " Jaya", "Skypiea", "Long Ring Long Land", "Water 7",
        "Enies Lobby", "Post-Enies Lobby", "Thriller Bark", "Sabaody Archipelago", "Amazon Lily", "Impel Down",
        "Marineford", "Post-War", "Return to Sabaody", "Fish-Man Island", "Punk Hazard", "Dressrosa", "Zou",
        "Whole Cake Island", "Levely", "Wano", "Egghead"]

# Creates and populates dictionary with data from .csv file
people = dict()
characterFile = open("OP_Data.csv", "r")
for row in characterFile:
    person = row.split(",")
    if person[0] != "Name":
        people[person[0]] = Character(float(person[1]), [person[2], person[3]], int(person[4]), [person[5], person[6]], person[7], int(person[8]), person[9].strip())

names = list(people.keys())  # Turns keys of dictionary into list of names so random generator can pick one