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

people = {  # Dictionary populated with all available characters with name as key and instance as value
    "Bepo": Character(2.40, ["Pirate", "Heart Pirates"], 18, ["New World", "Zou"], "Mink", 0, "None"),
    "Boa Hancock": Character(1.91, ["Pirate", "Kuja Pirates"], 19, ["Calm Belt", "Amazon Lily"], "Human", 3, "Paramecia"),
    "Brook": Character(2.77, ["Pirate", "Straw Hat"], 17, ["West Blue", "Unknown"], "Human", 0, "Paramecia"),
    "Carrot": Character(1.61, ["Kingdom", "Zou"], 27, ["New World", "Zou"], "Mink", 0, "None"),
    "Donquixote Rosinante": Character(2.93, ["World Government", "Marines"], 26, ["Red Line", "Mary Geoise"], "Human", 0, "Paramecia"),
    "Eggplant Soldier": Character(1.35, ["Pirate", "Big Mom Pirates"], 28, ["New World", "Whole Cake Island"], "Human", 0, "None"),
    "Franky": Character(2.40, ["Pirate", "Straw Hat"], 14, ["South Blue", "Unknown"], "Human", 0, "None"),
    "Jinbe": Character(3.01, ["Pirate", "Straw Hat"], 20, ["Grand Line", "Fish-Man Island"], "Fish-Man", 2, "None"),
    "Kozuki Momonosuke": Character(1.10, ["Kingdom", "Wano"], 25, ["Grand Line", "Unknown"], "Human", 1, "Zoan"),
    "Monkey D. Luffy": Character(1.74, ["Pirate", "Straw Hat"], 0, ["East Blue", "Goa Kingdom"], "Human", 3, "Zoan"),
    "Nami": Character(1.70, ["Pirate", "Straw Hat   "], 1, ["East Blue", "Conomi Islands"], "Human", 0, "None"),
    "Nico Robin": Character(1.88, ["Pirate", "Straw Hat"], 7, ["West Blue", "Ohara"], "Human", 0, "Paramecia"),
    "Rob Lucci": Character(2.12, ["World Government", "Cipher Pol"], 14, ["Grand Line", "Unknown"], "Human", 2, "Zoan"),
    "Roronoa Zoro": Character(1.81, ["Pirate", "Straw Hat"], 0, ["East Blue", "Unknown"], "Human", 3, "None"),
    "Sabo": Character(1.87, ["Other", "Revolutionary Army"], 22, ["East Blue", "Goa Kingdom"], "Human", 2, "Logia"),
    "Shanks": Character(1.99, ["Pirate", "Red Hair Pirates"], 0, ["West Blue", "Unknown"], "Human", 3, "None"),
    "Tony Tony Chopper": Character(0.90, ["Pirate", "Straw Hat"], 9, ["Grand Line", "Drum Island"], "Reindeer", 0, "Zoan"),
    "Trafalgar D. Water Law": Character(1.91,["Pirate", "Heart Pirates"], 18, ["North Blue", "Flevance"], "Human", 2, "Paramecia"),
    "Usopp": Character(1.76, ["Pirate", "Straw Hat"], 2, ["East Blue", "Gecko Islands"], "Human", 1, "None"),
    "Vinsmoke Sanji": Character(1.80, ["Pirate", "Straw Hat"], 3, ["North Blue", "Germa Kingdom"], "Human", 2, "None"),
    "Yamato": Character(2.63, ["Kingdom", "Wano"], 30, ["New World", "Wano"], "Oni", 3, "Zoan")
}
names = list(people.keys())  # Turns keys of dictionary into list of names so random generator can pick one
