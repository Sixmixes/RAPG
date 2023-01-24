import random as rn

#pasted from char.json file
characters = ["Centaur", "Minotaur", "Harpy", "Medusa", "Phoenix", "Kraken", "Leviathan", "Werewolf", "Vampire", "Zombie", "Ghost", "Angel", "Demon", "Fairy", "Goblin", "Elf", "Orc", "Troll", "Dragon", "Mermaid", "Ninja", "Samurai", "Pirate", "Knight", "Queen", "King", "Prince", "Princess", "Wizard", "Witch", "Sorcerer", "Necromancer", "Paladin", "Druid", "Cleric", "Ranger", "Bard", "Summoner", "Alchemist", "Robot", "Cyborg", "Alien", "Astronaut", "Spy", "Detective", "Cop", "Soldier", "Athlete", "Artist", "Musician", "Writer", "Philosopher", "Historian", "Archaeologist", "Biologist", "Chemist", "Physicist", "Mathematician", "Engineer", "Programmer", "Hacker", "Entrepreneur", "CEO", "Politician", "Diplomat", "Activist", "Lawyer", "Judge", "Priest", "Rabbi", "Imam", "Monk", "Shaman", "Medicine Man", "Hunter", "Farmer", "Fisherman", "logger", "Miner", "Construction Worker", "Electrician", "Plumber", "Carpenter", "Mechanic", "Chef", "Baker", "Bartender", "Waiter", "Hairdresser", "Makeup artist", "Fashion designer", "Model", "Photographer", "Film director", "Screenwriter", "Actor", "Dancer", "Magician", "Circus performer", "Ventriloquist", "Puppeteer", "Stand-up comedian", "Improv actor", "Maid", "Butler", "Janitor", "Security guard", "Firefighter", "EMT", "Nurse", "Doctor", "Surgeon", "Dentist", "Veterinarian", "Counselor", "Social worker", "Teacher", "Professor", "Librarian", "Archivist", "Curator", "Zookeeper", "Botanist", "Geologist", "Astronomer", "Meteorologist", "Oceanographer", "Paleontologist", "Anthropologist", "Sociologist", "Psychologist", "Economist", "Statistician", "Actuary", "Liguist", "Translator", "Interpreter", "Travel agent", "Tour guide", "Hotel manager", "Airline pilot", "Flight attendant", "Ship captian", "Sailor", "Diver", "Skipper", "Kayaker", "Conoer", "Rafter", "Rock climber", "Mountaineer", "Skier", "Snowboarder", "Surfer", "Bodybuilder", "Weightlifter", "Gymnast", "Swimmer", "Runner", "Cyclist", "Triathlete", "Boxer", "Wrestler", "Martial artist", "Fencer", "Archer", "Golfer", "Tennis player", "Bowling Player", "Pool player", "Darts player", "Baseball player", "Basketball player", "Football player", "Soccer player", "Hockey player", "Lacrosse", "Rugby player", "Cricket player", "Volleyball player", "Track and field athlete", "Figure skater", "Ice skater", "Speed skater", "Skateboarder", "BMX rider", "Motocross rider", "Snowmobiler", "ATV rider", "Jet skier", "Wakeboarder", "Kitesurfer", "Windsurfer", "Parasailer", "Hang glider", "Balloonist", "Glider pilot", "Airplane pilot", "Helicopter pilot", "Jet pilot", "Military pilot", "Space tourist", "Mission specialist", "Payload specialist", "Cosmonaut", "Space explorer", "Space engineer", "Space scientist", "Space doctor", "Space lawyer"]

#pasted from scifantasy-obj.json file
objects = ["Magic wand", "Light saber", "Time machine", "Teleportation device", "Force field generator", "Holographic projector", "Invisibility Cloak", "Hoverboard", "Cybernetic implant", "Jetpack", "Neural interface", "Laser gun", "Plasma rifle", "Warp drive", "Holodeck", "Force pike", "Gravity gun", "Power armor", "Anti-gravity platform", "Neural disruptor", "Cryogenic chamber", "Mind control device", "Telekinesis amplifier", "Force-sensitive amulet", "Robotic companion", "Gravity-manipulating gauntlets", "Holographic disguise generator", "Quantum entanglement communicator", "Force-sensitive training remote", "Anti-gravitational levitation device", "Hyperspace-capable spaceship", "Force-sensitive holocron", "Self-replicating nanobots", "Holoscanner", "Force-sensitive training orb", "Holosuit", "Holocron databank", "Forc-sensitive cloaking device", "Fusion-powered energy sword", "Holoprojector", "Fusion Rifle"]

#pasted from scifantasy-settings.json file
settings = ["a futuristic city", "a distant planet", "a spaceship", "a post-apocalyptic wasteland", "a virtual reality world", "a parallel universe", "a time portal", "a hidden underground facility", "a floating island", "an alien worldand", "a black hole", "a cyberpunk metropolis", "a underwater research station", "a genetically engineered jungle", "a robot-run factory", "a moon base", "a holographic representation of a historical location", "a chemically altered desert", "a high tech laboratory", "a supernatural realm", "a time traveling train", "a holographic concert hall", "an intergalactic marketplace", "a secret government research facility", "a sprawling megalopolis", "a massive orbital station", "a virtual simulation of historical event", "a underwater city", "an abandoned space station", "a Dyson sphere", "a planet-sized spaceship", "a hollowed-out asteroid", "a massive underwater trench", "an artificial intelligence-controlled metropolis", "a massive underground bunker", "a floating city in the clouds", "a terraformed planet", "a space elevator", "a teleportation hub", "a biopunk city", "a floating island fortress", "a cyber-dystopian metropolis", "a post-singularity society", "a sentient planet", "a floating city on a gas giant", "a utopia run by bots", "a post-human civilization", "a secret underground city of a long-lost civilization", "a dark dimension", "a hidden underground facility housing ancient technology", "a massive floating city in the middle of the ocean", "a pocket dimension", "a high-tech underwater city", "a virtual reality game world", "a rogue AI-controlled spaceship", "a colony on a distant moon", "a high-tech floating fortress", "a low-gravity space station", "a virtual reality prison", "a massive underwater research facility", "a steampunk metropolis", "a post-apocalyptic city-state", "a high-tech military base", "a secret underground bunker for a powerful orginization", "a cyberpunk dystopia", "a virtual reality simulation", "a virtual reality simulation of a post-apocalyptic world", "a massive orbital ring", "a space colony on the edge of a black hole", "a biomechanical city", "A secret underground city of a long-lost civilization"]


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
        prompt = character + ' ' + 'with a ' + obj + ' in ' + setting + ', ' + adj + ' ' + ' '.join(liststyles)

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