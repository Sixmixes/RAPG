import random as rn
import pyperclip as pc

#pasted from char.json file
characters = ["Centaur", "Minotaur", "Harpy", "Medusa", "Phoenix", "Kraken", "Leviathan", "Werewolf", "Vampire", "Zombie", "Ghost", "Angel", "Demon", "Fairy", "Goblin", "Elf", "Orc", "Troll", "Dragon", "Mermaid", "Ninja", "Samurai", "Pirate", "Knight", "Queen", "King", "Prince", "Princess", "Wizard", "Witch", "Sorcerer", "Necromancer", "Paladin", "Druid", "Cleric", "Ranger", "Bard", "Summoner", "Alchemist", "Robot", "Cyborg", "Alien", "Astronaut", "Spy", "Detective", "Cop", "Soldier", "Athlete", "Artist", "Musician", "Writer", "Philosopher", "Historian", "Archaeologist", "Biologist", "Chemist", "Physicist", "Mathematician", "Engineer", "Programmer", "Hacker", "Entrepreneur", "CEO", "Politician", "Diplomat", "Activist", "Lawyer", "Judge", "Priest", "Rabbi", "Imam", "Monk", "Shaman", "Medicine Man", "Hunter", "Farmer", "Fisherman", "logger", "Miner", "Construction Worker", "Electrician", "Plumber", "Carpenter", "Mechanic", "Chef", "Baker", "Bartender", "Waiter", "Hairdresser", "Makeup artist", "Fashion designer", "Model", "Photographer", "Film director", "Screenwriter", "Actor", "Dancer", "Magician", "Circus performer", "Ventriloquist", "Puppeteer", "Stand-up comedian", "Improv actor", "Maid", "Butler", "Janitor", "Security guard", "Firefighter", "EMT", "Nurse", "Doctor", "Surgeon", "Dentist", "Veterinarian", "Counselor", "Social worker", "Teacher", "Professor", "Librarian", "Archivist", "Curator", "Zookeeper", "Botanist", "Geologist", "Astronomer", "Meteorologist", "Oceanographer", "Paleontologist", "Anthropologist", "Sociologist", "Psychologist", "Economist", "Statistician", "Actuary", "Liguist", "Translator", "Interpreter", "Travel agent", "Tour guide", "Hotel manager", "Airline pilot", "Flight attendant", "Ship captian", "Sailor", "Diver", "Skipper", "Kayaker", "Conoer", "Rafter", "Rock climber", "Mountaineer", "Skier", "Snowboarder", "Surfer", "Bodybuilder", "Weightlifter", "Gymnast", "Swimmer", "Runner", "Cyclist", "Triathlete", "Boxer", "Wrestler", "Martial artist", "Fencer", "Archer", "Golfer", "Tennis player", "Bowling Player", "Pool player", "Darts player", "Baseball player", "Basketball player", "Football player", "Soccer player", "Hockey player", "Lacrosse", "Rugby player", "Cricket player", "Volleyball player", "Track and field athlete", "Figure skater", "Ice skater", "Speed skater", "Skateboarder", "BMX rider", "Motocross rider", "Snowmobiler", "ATV rider", "Jet skier", "Wakeboarder", "Kitesurfer", "Windsurfer", "Parasailer", "Hang glider", "Balloonist", "Glider pilot", "Airplane pilot", "Helicopter pilot", "Jet pilot", "Military pilot", "Space tourist", "Mission specialist", "Payload specialist", "Cosmonaut", "Space explorer", "Space engineer", "Space scientist", "Space doctor", "Space lawyer"]

#pasted from scifantasy-obj.json file
objects = ["Magic wand", "Light saber", "Time machine", "Teleportation device", "Force field generator", "Holographic projector", "Invisibility Cloak", "Hoverboard", "Cybernetic implant", "Jetpack", "Neural interface", "Laser gun", "Plasma rifle", "Warp drive", "Holodeck", "Force pike", "Gravity gun", "Power armor", "Anti-gravity platform", "Neural disruptor", "Cryogenic chamber", "Mind control device", "Telekinesis amplifier", "Force-sensitive amulet", "Robotic companion", "Gravity-manipulating gauntlets", "Holographic disguise generator", "Quantum entanglement communicator", "Force-sensitive training remote", "Anti-gravitational levitation device", "Hyperspace-capable spaceship", "Force-sensitive holocron", "Self-replicating nanobots", "Holoscanner", "Force-sensitive training orb", "Holosuit", "Holocron databank", "Forc-sensitive cloaking device", "Fusion-powered energy sword", "Holoprojector", "Fusion Rifle"]

#pasted from scifantasy-settings.json file
settings = ["a futuristic city", "a distant planet", "a spaceship", "a post-apocalyptic wasteland", "a virtual reality world", "a parallel universe", "a time portal", "a hidden underground facility", "a floating island", "an alien worldand", "a black hole", "a cyberpunk metropolis", "a underwater research station", "a genetically engineered jungle", "a robot-run factory", "a moon base", "a holographic representation of a historical location", "a chemically altered desert", "a high tech laboratory", "a supernatural realm", "a time traveling train", "a holographic concert hall", "an intergalactic marketplace", "a secret government research facility", "a sprawling megalopolis", "a massive orbital station", "a virtual simulation of historical event", "a underwater city", "an abandoned space station", "a Dyson sphere", "a planet-sized spaceship", "a hollowed-out asteroid", "a massive underwater trench", "an artificial intelligence-controlled metropolis", "a massive underground bunker", "a floating city in the clouds", "a terraformed planet", "a space elevator", "a teleportation hub", "a biopunk city", "a floating island fortress", "a cyber-dystopian metropolis", "a post-singularity society", "a sentient planet", "a floating city on a gas giant", "a utopia run by bots", "a post-human civilization", "a secret underground city of a long-lost civilization", "a dark dimension", "a hidden underground facility housing ancient technology", "a massive floating city in the middle of the ocean", "a pocket dimension", "a high-tech underwater city", "a virtual reality game world", "a rogue AI-controlled spaceship", "a colony on a distant moon", "a high-tech floating fortress", "a low-gravity space station", "a virtual reality prison", "a massive underwater research facility", "a steampunk metropolis", "a post-apocalyptic city-state", "a high-tech military base", "a secret underground bunker for a powerful orginization", "a cyberpunk dystopia", "a virtual reality simulation", "a virtual reality simulation of a post-apocalyptic world", "a massive orbital ring", "a space colony on the edge of a black hole", "a biomechanical city", "A secret underground city of a long-lost civilization"]


adjectives = ["Alluring", "Adorable", "Aesthetic", "Animated", "Awe-inspiring", "Attractive", "Agile", "Admired", "Beautiful", "Bewitching", "Brave", "Bold", "Bright", "Bodacious", "Benign", "Bewildered", "Alien", "Android", "Amorphous", "Antique", "Arachnid", "Artificial", "Augmented", "Bionic", "Bizarre", "Bladed", "Blind", "Bloodied", "Blue", "Bodiless", "Bony", "Brittle", "Bronze", "Bulbous", "Burnt", "Camouflaged", "Carbon-based", "Cadaverous", "Chitinous", "Clockwork", "Colossal", "Combative", "Composing", "Composite", "Computerized", "Concealed", "Cybernetic", "Cyberpunk", "Dented", "Deprived", "Deserted", "Detailed", "Digital", "Diseased", "Disguised", "Disintegrated", "Distorted", "Domineering", "Drone", "Electric", "Ectoplasmic", "Electro-mechanical", "Emaciated", "Enlarged", "Enormous", "Enshrined", "Ergonomic", "Ethereal", "Exoskeletal", "Extraterrestrial", "Faceless", "Feathered", "Feral", "Flawed", "Fluidic", "Frail", "Frayed", "Futuristic", "Gaseous", "Gaunt", "Glosing", "Glowing", "Gossameric", "Granite", "Grasping", "Gravitational", "Grotesque", "Horned", "Humanoid", "Hydro-mechanical", "Hyper-realistic", "Icy", "Impenetrable", "Inanimate", "Incandescent", "Incomplete", "Incorporeal", "Industrial", "Infared", "Insectoid", "Insidious", "Intergalactic", "Interstellar", "Intricate", "Invisibile", "Iridescent", "Irradiated", "Jagged", "Kinetic", "Lacerated", "Luminous", "Lunar", "Mechanical", "Medi-tech", "Metallic", "Mimetic", "Molten", "Monstrous", "Multi-limbed", "Muscular", "Nano-tech", "Necrotic", "Neon", "Neural", "Non-corporeal", "Non-human", "Nuclear", "Organic", "Outlandish", "Outmoded", "Overgrown", "Overloaded", "Oversized", "Pale", "Particle", "Perforated", "Petrified", "Phantasmal", "Photic", "Photonic", "Platinum", "Pliable", "Plummeting", "Polymer", "Prehistoric", "Pristine", "Psionic", "Pulsating", "Quantum", "Radiant", "Radioactive", "Ragged", "Enraged", "Rapid", "Reanimated", "Rebel", "Red", "Reflective", "Regenerating", "Reinforced", "Reptillian", "Resillient", "Robotic", "Rusted", "Sable", "Sapphire", "Satin", "Scaled", "Scarred", "Sci-fi", "Sculpted", "Shaded", "Shadow", "Shapeshifting", "Shimmering", "Silken", "Skeletal", "Skinless", "Slick", "Smooth", "Snapped", "Solar", "Solid", "Soulless", "Sparkling", "Spectral", "Spherical", "Spiky", "Splintered", "Sprouted", "Splotched", "Steel", "Steampunk", "Stony", "Storm", "Stranded", "Stretched", "Striped", "Stylized", "Subterranean", "Sunken", "Supernatural", "Superpowered", "Surreal", "Tarnished", "Techno", "Telepathic", "Temporal"]


styles = ["abstract", "realistic", "surreal", "fantasy", "Abstract", "Impressionistic", "Photorealistic", "Surrealistic", "Abstract Expressionism", "Art Deco", "Art Nouveau", "Baroque", "Conceptual", "Futuristic", "Hyperrealism", "Illusionistic", "Low Poly", "Minimalistic", "Pointillism", "Pop Art", "Post-Impressioinism", "Realism", "Renaissance", "Romantic", "Surreal", "Surrealism", "Symbolism", "Ukiyo-e", "Vector Art", "Voxel Art", "Pixel Art", "Neural Art", "GAN art", "3D Modeling", "VR Art", "Deep Dream", "Painting", "Sculpture", "Street Art", "Typography", "Landscape", "Mosaic", "Logo Design", "Infographic", "Game Art", "Animation", "Film", "Music Video", "chroma key", "High contrast", "Low contrast", "Cubism", "Expressionism", "Futurism", "Dadaism", "Minimalism", "Photorealism", "Neo-expressionism", "Gothic", "Street", "Graffiti", "Digital", "3D", "Photo-manipulation", "Collage", "Assemblage", "Printmaking", "Land art", "Body art", "Street art", "Street photography", "Still life", "Nature", "Architecture", "Cityscape", "Aerial", "Underwater", "Night", "Black and White", "Sepia", "Color", "Monochrome", "Duotone", "Triptych", "Kinetic Art", "Hard-edge", "Color Field", "Concept art", "conceptual art"]


genmetas = ["Eerie", "Gloomy", "Somber", "Morbid", "Bleak", "Despairing", "Melancholic", "Misanthropic", "Cynical", "Despondent", "Wistful", "Melancholy", "Nostalgic", "Tragic", "Disheartening", "Dispiriting", "Desolate"]

# Number of styles and qualities to include in the prompt
numstyles = 3
numquality = 2

while True:
    user_input = input("Press enter to generate a new prompt, or enter a number 1-6 to update the corresponding list in the previous prompt(or enter 'q' to exit): ")
    if user_input == "":
        # Select random elements from the lists
        character = rn.choice(characters)
        obj = rn.choice(objects)
        setting = rn.choice(settings)
        adj = rn.choice(adjectives)
        liststyles = rn.sample(styles, numstyles)
        listmetas =  rn.sample(genmetas, numquality)

        # Create the prompt
        prompt = '\n' + '\n' + adj + ' ' + character + ' ' + 'with a ' + obj + ' in ' + setting + ', ' + ', '.join(liststyles) + ', ' + ', '.join(listmetas) + '\n' + '\n'

        # Store the prompt and its elements in variables
        prev_prompt = prompt
        prev_characters = character
        prev_objects = obj
        prev_settings = setting
        prev_adjectives = adj
        prev_styles = str(', '.join(liststyles))
        prev_metas = str(', '.join(listmetas))

        # Print the prompt
        print("Prompt: " + prompt)
        pc.copy(prompt)
    elif user_input == "1":
        prev_adjectives = rn.choice(adjectives)
        prev_prompt = '\n' + '\n' + prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + '\n' + '\n'
        print("The adjectives in the previous prompt has been updated to: ",prev_adjectives)
        print("The updated prompt is: ",prev_prompt)
        pc.copy(prev_prompt)
    elif user_input == "2":
        prev_characters = rn.choice(characters)
        prev_prompt = '\n' + '\n' + prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + '\n' + '\n'
        print("The characters in the previous prompt has been updated to: ",prev_characters)
        print("The updated prompt is: ",prev_prompt)
        pc.copy(prev_prompt)
    elif user_input == "3":
        prev_objects = rn.choice(objects)
        prev_prompt = '\n' + '\n' + prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + '\n' + '\n'
        print("The objects in the previous prompt has been updated to: ",prev_objects)
        print("The updated prompt is: ",prev_prompt)
        pc.copy(prev_prompt)
    elif user_input == "4":
        prev_settings = rn.choice(settings)
        prev_prompt = '\n' + '\n' + prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + '\n' + '\n'
        print("The settings in the previous prompt has been updated to: ",prev_settings)
        print("The updated prompt is: ",prev_prompt)
        pc.copy(prev_prompt)
    elif user_input == "5":
        prev_metas = listmetas
        prev_styles = ', '.join(rn.sample(styles, numstyles))
        prev_prompt = '\n' + '\n' + prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + prev_styles + ', ' + ', '.join(prev_metas) + '\n' + '\n'
        print("The styles in the previous prompt has been updated to: ",prev_styles)
        print("The updated prompt is: ",prev_prompt)
        pc.copy(prev_prompt)
    elif user_input == "6":
        prev_styles = liststyles
        prev_metas = ', '.join(rn.sample(genmetas, numquality))
        prev_prompt = '\n' + '\n' + prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' ' + prev_settings + ', ' + ', '.join(prev_styles) + ' ' + prev_metas + '\n' + '\n'
        print("The genmetas in the previous prompt has been updated to: ",prev_metas)
        print("The updated prompt is: ",prev_prompt)
        pc.copy(prev_prompt)
    elif user_input == "q":
        break
    else:
        print("Invalid input. Please enter a number 1-6 or press enter to generate a new prompt.")