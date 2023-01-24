import random as rn

characters = ["Centaur", "Minotaur", "Harpy", "Medusa", "Phoenix", "Kraken", "Leviathan", "Werewolf", "Vampire", "Zombie", "Ghost", "Angel", "Demon", "Fairy", "Goblin", "Elf", "Orc", "Troll", "Dragon", "Mermaid", "Ninja", "Samurai", "Pirate", "Knight", "Queen", "King", "Prince", "Princess", "Wizard", "Witch", "Sorcerer", "Necromancer", "Paladin", "Druid", "Cleric", "Ranger", "Bard", "Summoner", "Alchemist", "Robot", "Cyborg", "Alien", "Astronaut", "Spy", "Detective", "Cop", "Soldier", "Athlete", "Artist", "Musician", "Writer", "Philosopher", "Historian", "Archaeologist", "Biologist", "Chemist", "Physicist", "Mathematician", "Engineer", "Programmer", "Hacker", "Entrepreneur", "CEO", "Politician", "Diplomat", "Activist", "Lawyer", "Judge", "Priest", "Rabbi", "Imam", "Monk", "Shaman", "Medicine Man", "Hunter", "Farmer", "Fisherman", "logger", "Miner", "Construction Worker", "Electrician", "Plumber", "Carpenter", "Mechanic", "Chef", "Baker", "Bartender", "Waiter", "Hairdresser", "Makeup artist", "Fashion designer", "Model", "Photographer", "Film director", "Screenwriter", "Actor", "Dancer", "Magician", "Circus performer", "Ventriloquist", "Puppeteer", "Stand-up comedian", "Improv actor", "Maid", "Butler", "Janitor", "Security guard", "Firefighter", "EMT", "Nurse", "Doctor", "Surgeon", "Dentist", "Veterinarian", "Counselor", "Social worker", "Teacher", "Professor", "Librarian", "Archivist", "Curator", "Zookeeper", "Botanist", "Geologist", "Astronomer", "Meteorologist", "Oceanographer", "Paleontologist", "Anthropologist", "Sociologist", "Psychologist", "Economist", "Statistician", "Actuary", "Liguist", "Translator", "Interpreter", "Travel agent", "Tour guide", "Hotel manager", "Airline pilot", "Flight attendant", "Ship captian", "Sailor", "Diver", "Skipper", "Kayaker", "Conoer", "Rafter", "Rock climber", "Mountaineer", "Skier", "Snowboarder", "Surfer", "Bodybuilder", "Weightlifter", "Gymnast", "Swimmer", "Runner", "Cyclist", "Triathlete", "Boxer", "Wrestler", "Martial artist", "Fencer", "Archer", "Golfer", "Tennis player", "Bowling Player", "Pool player", "Darts player", "Baseball player", "Basketball player", "Football player", "Soccer player", "Hockey player", "Lacrosse", "Rugby player", "Cricket player", "Volleyball player", "Track and field athlete", "Figure skater", "Ice skater", "Speed skater", "Skateboarder", "BMX rider", "Motocross rider", "Snowmobiler", "ATV rider", "Jet skier", "Wakeboarder", "Kitesurfer", "Windsurfer", "Parasailer", "Hang glider", "Balloonist", "Glider pilot", "Airplane pilot", "Helicopter pilot", "Jet pilot", "Military pilot", "Space tourist", "Mission specialist", "Payload specialist", "Cosmonaut", "Space explorer", "Space engineer", "Space scientist", "Space doctor", "Space lawyer"]
objects = ["sword", "shield", "magic wand", "treasure chest"]
settings = ["in a castle", "in a forest", "on a mountain", "in a cave"]
adjectives = ["fierce", "beautiful", "mysterious", "ancient"]
styles = ["abstract", "realistic", "surreal", "fantasy"]
genmetas = ["dark", "light", "colorful", "muted"]

# Number of styles and qualities to include in the prompt
numstyles = 2
numquality = 1

while True:
    user_input = input("Press enter to generate a new prompt, or enter a number 1-6 to update the corresponding list in the previous prompt: ")
    if user_input == "":
        # Select random elements from the lists
        character = rn.choice(characters)
        obj = rn.choice(objects)
        setting = rn.choice(settings)
        adj = rn.choice(adjectives)
        liststyles = rn.sample(styles, numstyles) + rn.sample(genmetas, numquality)

        # Create the prompt
        prompt = character + ' ' + 'with a ' + obj + ' ' + setting + ', ' + adj + ' ' + ' '.join(liststyles)

        # Store the prompt and its elements in variables
        prev_prompt = prompt
        prev_characters = character
        prev_objects = obj
        prev_settings = setting
        prev_adjectives = adj
        prev_styles = liststyles
        prev_genmetas = genmetas

        # Print the prompt
        print("Prompt: " + prompt)
    elif user_input == "1":
        prev_characters = rn.choice(characters)
        prev_prompt = prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_adjectives + ' ' + ' '.join(prev_styles)
        print("The characters in the previous prompt has been updated to: ",prev_characters)
        print("The updated prompt is: ",prev_prompt)
    elif user_input == "2":
        prev_objects = rn.choice(objects)
        prev_prompt = prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_adjectives + ' ' + ' '.join(prev_styles)
        print("The objects in the previous prompt has been updated to: ",prev_objects)
        print("The updated prompt is: ",prev_prompt)
    elif user_input == "3":
        prev_settings = rn.choice(settings)
        prev_prompt = prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_adjectives + ' ' + ' '.join(prev_styles)
        print("The settings in the previous prompt has been updated to: ",prev_settings)
        print("The updated prompt is: ",prev_prompt)
    elif user_input == "4":
        prev_adjectives = rn.choice(adjectives)
        prev_prompt = prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_adjectives + ' ' + ' '.join(prev_styles)
        print("The adjectives in the previous prompt has been updated to: ",prev_adjectives)
        print("The updated prompt is: ",prev_prompt)
    elif user_input == "5":
        prev_styles = rn.choice(styles)
        prev_prompt = prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_adjectives + ' ' + ' '.join(prev_styles)
        print("The styles in the previous prompt has been updated to: ",prev_styles)
        print("The updated prompt is: ",prev_prompt)
    elif user_input == "6":
        prev_genmetas = rn.choice(genmetas)
        prev_prompt = prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_adjectives + ' ' + ' '.join(prev_styles)
        print("The genmetas in the previous prompt has been updated to: ",prev_genmetas)
        print("The updated prompt is: ",prev_prompt)
    else:
        print("Invalid input. Please enter a number 1-6 or press enter to generate a new prompt.")