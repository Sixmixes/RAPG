import random as rn
import pyperclip as pc

#pasted from char.json file
characters = ["Centaur", "Minotaur", "Harpy", "Medusa", "Phoenix", "Kraken", "Leviathan", "Werewolf", "Vampire", "Zombie", "Ghost", "Angel", "Demon", "Fairy", "Goblin", "Elf", "Orc", "Troll", "Dragon", "Mermaid", "Ninja", "Samurai", "Pirate", "Knight", "Queen", "King", "Prince", "Princess", "Wizard", "Witch", "Sorcerer", "Necromancer", "Paladin", "Druid", "Cleric", "Ranger", "Bard", "Summoner", "Alchemist", "Robot", "Cyborg", "Alien", "Astronaut", "Spy", "Detective", "Cop", "Soldier", "Athlete", "Artist", "Musician", "Writer", "Philosopher", "Historian", "Archaeologist", "Biologist", "Chemist", "Physicist", "Mathematician", "Engineer", "Programmer", "Hacker", "Entrepreneur", "CEO", "Politician", "Diplomat", "Activist", "Lawyer", "Judge", "Priest", "Rabbi", "Imam", "Monk", "Shaman", "Medicine Man", "Hunter", "Farmer", "Fisherman", "logger", "Miner", "Construction Worker", "Electrician", "Plumber", "Carpenter", "Mechanic", "Chef", "Baker", "Bartender", "Waiter", "Hairdresser", "Makeup artist", "Fashion designer", "Model", "Photographer", "Film director", "Screenwriter", "Actor", "Dancer", "Magician", "Circus performer", "Ventriloquist", "Puppeteer", "Stand-up comedian", "Improv actor", "Maid", "Butler", "Janitor", "Security guard", "Firefighter", "EMT", "Nurse", "Doctor", "Surgeon", "Dentist", "Veterinarian", "Counselor", "Social worker", "Teacher", "Professor", "Librarian", "Archivist", "Curator", "Zookeeper", "Botanist", "Geologist", "Astronomer", "Meteorologist", "Oceanographer", "Paleontologist", "Anthropologist", "Sociologist", "Psychologist", "Economist", "Statistician", "Actuary", "Liguist", "Translator", "Interpreter", "Travel agent", "Tour guide", "Hotel manager", "Airline pilot", "Flight attendant", "Ship captian", "Sailor", "Diver", "Skipper", "Kayaker", "Conoer", "Rafter", "Rock climber", "Mountaineer", "Skier", "Snowboarder", "Surfer", "Bodybuilder", "Weightlifter", "Gymnast", "Swimmer", "Runner", "Cyclist", "Triathlete", "Boxer", "Wrestler", "Martial artist", "Fencer", "Archer", "Golfer", "Tennis player", "Bowling Player", "Pool player", "Darts player", "Baseball player", "Basketball player", "Football player", "Soccer player", "Hockey player", "Lacrosse", "Rugby player", "Cricket player", "Volleyball player", "Track and field athlete", "Figure skater", "Ice skater", "Speed skater", "Skateboarder", "BMX rider", "Motocross rider", "Snowmobiler", "ATV rider", "Jet skier", "Wakeboarder", "Kitesurfer", "Windsurfer", "Parasailer", "Hang glider", "Balloonist", "Glider pilot", "Airplane pilot", "Helicopter pilot", "Jet pilot", "Military pilot", "Space tourist", "Mission specialist", "Payload specialist", "Cosmonaut", "Space explorer", "Space engineer", "Space scientist", "Space doctor", "Space lawyer", "A lone figure", "A group of partygoers", "An Egyptian pharaoh", "A being from another world", "A ghostly figure", "A robot or android", "A hooded figure", "A creature from a fantasy realm", "person"]

#pasted from scifantasy-obj.json file
objects = ["Magic wand", "Light saber", "Time machine", "Teleportation device", "Force field generator", "Holographic projector", "Invisibility Cloak", "Hoverboard", "Cybernetic implant", "Jetpack", "Neural interface", "Laser gun", "Plasma rifle", "Warp drive", "Holodeck", "Force pike", "Gravity gun", "Power armor", "Anti-gravity platform", "Neural disruptor", "Cryogenic chamber", "Mind control device", "Telekinesis amplifier", "Force-sensitive amulet", "Robotic companion", "Gravity-manipulating gauntlets", "Holographic disguise generator", "Quantum entanglement communicator", "Force-sensitive training remote", "Anti-gravitational levitation device", "Hyperspace-capable spaceship", "Force-sensitive holocron", "Self-replicating nanobots", "Holoscanner", "Force-sensitive training orb", "Holosuit", "Holocron databank", "Forc-sensitive cloaking device", "Fusion-powered energy sword", "Holoprojector", "Fusion Rifle"]

#pasted from settings.json file
settings = ["a rooftop, looking out over the city while they listen to music on headphones", "surrounded by graffiti and street art.", "lost in their own world as they listen to music on a portable speaker.", "on a concrete slab, surrounded by the neon lights of the city.", "lost in the music as the city bustles around them.", "enjoying the sunset and the sound of waves crashing in the background.", "sitting on a stoop with a pair of headphones on and a notebook in hand.", "surrounded by a crowd of people and the pulsing lights of the DJ booth.", "urban landscape", "city streets", "Urban cityscape at night with neon lights and reflections on wet streets.", "A rooftop with a city view, preferably during sunset or at night.", "A cozy lounge or speakeasy-style setting with dim lighting and vintage decor.", "A graffiti-covered alleyway with interesting textures and pops of color.", "A park or outdoor area with lush greenery and natural elements.", "A vintage record store or music venue with a retro feel.", "A modern, minimalistic recording studio or music production space.", "A concert or live performance setting with stage lighting and a crowd.", "A pool or beach party with a relaxed, laid-back atmosphere.", "A cozy living room or bedroom with soft lighting and personal touches.", "A picturesque beach with clear blue water and white sand.", "A lush green forest with a small stream running through it.", "A snowy mountain landscape with a cabin nestled in the trees.", "A bustling city street with tall skyscrapers and colorful neon lights.", "A desert landscape with a sunset in the background.", "A floating city with a futuristic design.", "A secluded waterfall hidden in a tropical jungle.", "A beautifully manicured garden with a variety of flowers and trees.", "A vintage-inspired train station with steam rising from the engine.", "A abandoned industrial factory with graffiti covered walls.", "The Great Sphinx and the pyramids of Giza", "", "The temples of Luxor and Karnak", "The Valley of the Kings and the tombs of pharaohs", "The Nile River and its banks, with boats and markets", "The desert landscape and its oasis", "The city of Alexandria and its lighthouse", "The hieroglyph-covered walls of an ancient tomb or temple", "A pharaoh's palace or throne room", "A market or bazaar in ancient Thebes or Memphis", "A battle scene featuring Egyptian soldiers and chariots.", "A dimly lit, crowded nightclub with neon lights and laser beams.", "An outdoor rooftop party with city lights in the background.", "A large mansion or villa with a pool and a DJ playing music.", "A beach party with bonfires and people dancing on the sand.", "A concert or music festival with a stage and a large crowd.", "A house party with people dancing and socializing in a living room or basement.", "A boat or yacht party with people dancing and drinking on deck.", "A parade or carnival with colorful floats and costumes.", "A VIP lounge or VIP section in a club or concert venue.", "An after-hours party in a warehouse or industrial space with graffiti and street art.", "A futuristic cityscape with neon lights and holographic billboards", "An alien nightclub with glowing, pulsing walls and strange, otherworldly creatures as patrons", "A floating party island in the clouds, complete with a DJ booth and fireworks display", "A massive intergalactic cruise ship with multiple decks and a dance floor under a starry sky", "A virtual reality party where guests can choose their own avatars and surroundings", "A mystical, enchanted forest with a bonfire and fairy-like creatures dancing around it.", "A underwater city with sea creatures and bioluminescent plants", "A abandoned spaceship or station with flickering lights and graffiti all over.", "A temple ruin or pyramid with hieroglyphics and statues, where people are dancing and partying.", "An otherworldly landscape with unusual geological features such as floating rocks or gravity defying areas where people are dancing on them.", "A dark, abandoned city with crumbling buildings and empty streets", "A dimly-lit underground lair or cave system", "A foggy, misty forest with twisted, gnarled trees", "A desolate, snowy wasteland with no sign of life", "A mechanical factory or laboratory with soulless machines and sterile equipment", "A black void or abyss with no defining features or landmarks", "A reflection of a person's face in a mirror, with their eyes appearing empty or hollow", "A person sitting alone in a dimly lit room with no emotion on their face", "A person walking aimlessly through a crowded city, but not interacting with anyone.", "a dark alley", "a fantasy realm with menacing features", "a misty forest", "another world with unusual features and technology", "a throne surrounded by hieroglyphics", "a dimly lit club", "a deserted city street at night", "a futuristic city", "a distant planet", "a spaceship", "a post-apocalyptic wasteland", "a virtual reality world", "a parallel universe", "a time portal", "a hidden underground facility", "a floating island", "an alien worldand", "a black hole", "a cyberpunk metropolis", "a underwater research station", "a genetically engineered jungle", "a robot-run factory", "a moon base", "a holographic representation of a historical location", "a chemically altered desert", "a high tech laboratory", "a supernatural realm", "a time traveling train", "a holographic concert hall", "an intergalactic marketplace", "a secret government research facility", "a sprawling megalopolis", "a massive orbital station", "a virtual simulation of historical event", "a underwater city", "an abandoned space station", "a Dyson sphere", "a planet-sized spaceship", "a hollowed-out asteroid", "a massive underwater trench", "an artificial intelligence-controlled metropolis", "a massive underground bunker", "a floating city in the clouds", "a terraformed planet", "a space elevator", "a teleportation hub", "a biopunk city", "a floating island fortress", "a cyber-dystopian metropolis", "a post-singularity society", "a sentient planet", "a floating city on a gas giant", "a utopia run by bots", "a post-human civilization", "a secret underground city of a long-lost civilization", "a dark dimension", "a hidden underground facility housing ancient technology", "a massive floating city in the middle of the ocean", "a pocket dimension", "a high-tech underwater city", "a virtual reality game world", "a rogue AI-controlled spaceship", "a colony on a distant moon", "a high-tech floating fortress", "a low-gravity space station", "a virtual reality prison", "a massive underwater research facility", "a steampunk metropolis", "a post-apocalyptic city-state", "a high-tech military base", "a secret underground bunker for a powerful orginization", "a cyberpunk dystopia", "a virtual reality simulation", "a virtual reality simulation of a post-apocalyptic world", "a massive orbital ring", "a space colony on the edge of a black hole", "a biomechanical city", "A secret underground city of a long-lost civilization"]


adjectives = ["Alluring", "Adorable", "Aesthetic", "Animated", "Awe-inspiring", "Attractive", "Agile", "Admired", "Beautiful", "Bewitching", "Brave", "Bold", "Bright", "Bodacious", "Benign", "Bewildered", "Alien", "Android", "Amorphous", "Antique", "Arachnid", "Artificial", "Augmented", "Bionic", "Bizarre", "Bladed", "Blind", "Bloodied", "Blue", "Bodiless", "Bony", "Brittle", "Bronze", "Bulbous", "Burnt", "Camouflaged", "Carbon-based", "Cadaverous", "Chitinous", "Clockwork", "Colossal", "Combative", "Composing", "Composite", "Computerized", "Concealed", "Cybernetic", "Cyberpunk", "Dented", "Deprived", "Deserted", "Detailed", "Digital", "Diseased", "Disguised", "Disintegrated", "Distorted", "Domineering", "Drone", "Electric", "Ectoplasmic", "Electro-mechanical", "Emaciated", "Enlarged", "Enormous", "Enshrined", "Ergonomic", "Ethereal", "Exoskeletal", "Extraterrestrial", "Faceless", "Feathered", "Feral", "Flawed", "Fluidic", "Frail", "Frayed", "Futuristic", "Gaseous", "Gaunt", "Glosing", "Glowing", "Gossameric", "Granite", "Grasping", "Gravitational", "Grotesque", "Horned", "Humanoid", "Hydro-mechanical", "Hyper-realistic", "Icy", "Impenetrable", "Inanimate", "Incandescent", "Incomplete", "Incorporeal", "Industrial", "Infared", "Insectoid", "Insidious", "Intergalactic", "Interstellar", "Intricate", "Invisibile", "Iridescent", "Irradiated", "Jagged", "Kinetic", "Lacerated", "Luminous", "Lunar", "Mechanical", "Medi-tech", "Metallic", "Mimetic", "Molten", "Monstrous", "Multi-limbed", "Muscular", "Nano-tech", "Necrotic", "Neon", "Neural", "Non-corporeal", "Non-human", "Nuclear", "Organic", "Outlandish", "Outmoded", "Overgrown", "Overloaded", "Oversized", "Pale", "Particle", "Perforated", "Petrified", "Phantasmal", "Photic", "Photonic", "Platinum", "Pliable", "Plummeting", "Polymer", "Prehistoric", "Pristine", "Psionic", "Pulsating", "Quantum", "Radiant", "Radioactive", "Ragged", "Enraged", "Rapid", "Reanimated", "Rebel", "Red", "Reflective", "Regenerating", "Reinforced", "Reptillian", "Resillient", "Robotic", "Rusted", "Sable", "Sapphire", "Satin", "Scaled", "Scarred", "Sci-fi", "Sculpted", "Shaded", "Shadow", "Shapeshifting", "Shimmering", "Silken", "Skeletal", "Skinless", "Slick", "Smooth", "Snapped", "Solar", "Solid", "Soulless", "Sparkling", "Spectral", "Spherical", "Spiky", "Splintered", "Sprouted", "Splotched", "Steel", "Steampunk", "Stony", "Storm", "Stranded", "Stretched", "Striped", "Stylized", "Subterranean", "Sunken", "Supernatural", "Superpowered", "Surreal", "Tarnished", "Techno", "Telepathic", "Temporal"]


styles = ["Abstract", "Impressionistic", "Photorealistic", "Surrealistic", "Abstract Expressionism", "Art Deco", "Art Nouveau", "Baroque", "Conceptual", "Futuristic", "Hyperrealism", "Illusionistic", "Low Poly", "Minimalistic", "Pointillism", "Pop Art", "Post-Impressioinism", "Realism", "Renaissance", "Surreal", "Surrealism", "Symbolism", "Ukiyo-e", "Vector Art", "Voxel Art", "Pixel Art", "Neural Art", "GAN art", "3D Modeling", "VR Art", "Deep Dream", "Painting", "Sculpture", "Street Art", "Landscape", "Mosaic", "Logo Design", "Infographic", "Game Art", "Animation", "Film", "Music Video", "chroma key", "High contrast", "Low contrast", "Cubism", "Expressionism", "Futurism", "Dadaism", "Minimalism", "Photorealism", "Neo-expressionism", "Gothic", "Street", "Graffiti", "Digital", "3D", "Photo-manipulation", "Collage", "Assemblage", "Land art", "Body art", "Street art", "Street photography", "Still life", "Nature", "Architecture", "Cityscape", "Aerial", "Underwater", "Night", "Black and White", "Sepia", "Color", "Monochrome", "Duotone", "Triptych", "Kinetic Art", "Hard-edge", "Color Field", "Concept art", "conceptual art", "Oil painting", "Natural", "Colored", "Award-winning photography", "Cinematic lighting", "Limited pallete", "Pastel colors", "Cyberpunk", "Render", "Rendered in unreal engine", "Photo", "Glitch art", "Space art", "Epic composition", "Night time", "Vivid colors", "Soft lighting", "Wavy", "Extradimensional", "Depth of field", "Tonemapping", "Illustration", "Digital painting", "Line art", "Ink", "Color field painting", "God rays", "Saturated", "Desaturated", "Tonal colors", "Full body", "Eyes focus", "Anime", "Aerial view", "Street level view", "Panoramic", "Hard edge", "Thick lines", "Color page", "Precise lineart", "Neon ligthing", "Sun rays", "Nostalgic", "Brutalism", "Winter", "Summer", "Studio lighting", "bokeh", "Motion lines", "Wallpaper", "Muted colors", "Colorgrading", "Vintage", "Aesthetic", "Cosmic horror", "Abstract art", "Simplistic", "Dim", "Blurred background", "Ambient lighting", "Intense shadows", "Slow motion", "Reflections", "Detailed", "Detailed face", "animecore", "Astrophotography", "Biomechanical", "Darkwave", "Deathpunk", "Glitchcore", "Glowwave", "Holographic", "Beautifully lit", "Technopunk", "Sci-fi", "Crystalline", "Movie still", "2D", "Claymation", "Charcoal sketch", "Low poly", "Blender render"]


genmetas = ["Eerie", "Gloomy", "Somber", "Morbid", "Bleak", "Despairing", "Melancholic", "Misanthropic", "Cynical", "Despondent", "Wistful", "Melancholy", "Tragic", "Disheartening", "Dispiriting", "Desolate", "realistic", "8k", "4k", "detailed", "hyperdetailed", "sharp focus", "masterpiece", "absurdres", "highres", "professional", "photorealism", "studio quality", "hyper realistic"]

artists = ["Aaron Horkey", "Abigail Larson", "Adam Paquette", "Adolph Menzel", "Adonna Khare", "Affandi", "Agnes Lawrence Pelton", "Agustin Fernandez", "Akira Toriyama", "Al Williamson", "Alan Lee", "Albert Bierstadt", "Alexander Milne Calder", "Alberto Giacometti", "Albrecht Durer", "Alena Aenami", "Alex Grey", "Alexander Bogen", "Alexander Jansson", "Alexandre Cabanel", "Alexej von Jawlensky", "Alfred Kubin", "Alfred Parsons", "Alice Neel", "Alice Rahon", "Alphonse Mucha", "Alyssa Monks", "Amanda Clark", "Amedeo Modigliani", "Amir Zand", "Laurel Burch", "Ander Wyeth", "Andre Leblanc", "Andre Masson", "Andy Goldsworthy", "Andy Warhol", "Angus Mckie", "Antoine Blanchard", "Anton Fadeev", "Anton Otto Fischer", "Anton Pieck", "Antoni Gaudi", "Antti Lovag", "Artemisia Gentileschi", "Artgerm", "Albrecht Durer", "Agustin Fernandez", "Amir Zand Laurel Burch", "Andrew Wyeth", "Andre Leblanc", "Andre Masson", "Angus McKie", "Anna Dittmann", "Anne Geddes", "Anne Stokes", "Anni Albers", "Annibale Carracci", "Ansel Adams", "Anthony van Dyck", "Ayami Kojima Banksy", "Beauford Delaney", "Aubrey Beardsley", "Audrey Kawasaki", "Barbara Kruger", "Beeple", "Apollonia Saintclair", "Arik Brauer", "Arnold Bocklin", "Arshile Gorky", "Art Fitzpatrick", "Artgerm ", "Arthur Adams", "Arthur Dove", "Arthur Hughes", "Arthur Rackham", "Atey Ghailan", "Art Spiegelman", "Asaf Hanuka", "August Macke", "Augustus Edwin Mulready", "Austin Briggs", "Bernie Wrightson", "Bjarke Ingels", "Boris Vallejo", "Brian Despain", "Bruce Pennington", "Camille Corot", "Ben Shahn", "Bob Byerley", "Bob Eggleton", "Brian Froud", "Brian Kesinger", "Camille-Pierre Pambu", "Bodo", "Barclay Shaw", "Ben Templesmith", "Bastien Lecouffe-Deharme", "Bauhaus", "Beatrix Potter", "Benoit B. Mandelbrot", "Bernard Buffet", "Bob Ringwood", "Bob Ross", "Bonnard Pierre", "Bridget Bate Tichenor", "Brothers Hildebrandt", "Canaletto", "Candido Portinari", "Caravaggio", "Carl Barks", "Carl Gustav Carus", "Cassius Marcellus Coolidge", "Carl Holsoe", "Carl Larsson", "Cecily Mary Barker", "Charles Addams", "Carne Griffiths", "Caspar David Friedrich", "Charles Angrand", "Charles Blackman", "Charles E. Burchfield", "Charles Schulz", "Chaim Soutine", "Chesley Bonestell", "Chiharu Shiota", "Chris Foss", "Chris LaBrooy", "Chris Mars", "Chris Moore", "Claude Monet", "Clive Madgwick", "Clovis Trouille", "Christopher Balaskas", "Cindy Sherman", "Claude Cahun", "Clyde Caldwell", "Coby Whitmore", "Coles Phillips", "Conrad Roset", "Cory Loftis", "Craig Davison", "Craig Mullins", "Craola", "Daniel Ridgway Knight", "David B. Mattingly", "Dean Ellis", "Dorothea Tanning", "Daniel Ridgway Knights", "David Bates", "David Burdeny", "Diane Arbus", "Diego Velazquez", "Cuno Amiet", "Dave Dorman", "Eddie Mendoza", "Edward Gorey", "Egon Schiele", "Eiichiro Oda", "Elsa Beskow", "Emil Nolde", "Ernst Ludwig Kirchner", "David Burliuk", "Don Bluth", "Dorothy Lathrop", "Dustin Nguyen", "Earl Norem", "Edgar Degas", "Edmund Dulac", "Edmund Leighton", "Edward Hopper", "Edward Lear", "Edward Robert Hughes", "Eileen Agar", "Elaine de Kooning", "Emile Galle", "Esao Andrews", "Dan Flavin", "Dave Gibbons", "David Finch", "Dan Mumford", "Dave McKean", "Daniel Merriam", "David A. Hardy", "Don Maitz", "David Hockney", "Donato Giancola", "David Palumbo", "Dora Maar", "Ed Emshwiller", "Edvard Munch", "Edward Weston", "Eddie Campbell", "Edward Burne-Jones", "Edwin Austin Abbey", "El Greco", "Emma Geary", "Eugene Delacroix", "Eleanor Vere Boyle", "Elliott Erwitt", "Enki Bilal", "Erich Heckel", "Ernst Fuchs", "Ernst Haeckel", "Evelyn De Morgan", "Eyvind Earle", "Farel Dalrympleq", "Felix-Kelly", "Fenghua Zhong", "Ferdinand Hodler", "Filip Hodas", "Francisco Goya", "Frank Auerbach", "Frank Frazetta", "Franz Xaver Winterhalter", "Frederic Church", "Frank Miller ", "Frederick Lord Leighton", "Filippino Lippi ", "Franklin Booth", "Francis Bacon", "Francis Picabia", "Franz Marc", "Franz Sedlacek", "Frida Kahlo ", "Frits Van den Berghe", "Gabriele M\u00fcnter", "Gaston Bussi\u00e8re ", "Geof Darrow", "George Frederic Watts", "George Grosz", "George Inness", "George Lucas", "George Luks ", "Georges Rouault", "Georges Seurat", "Georgia O'Keeffe", "Gerald Brom", "Gerhard Munthe", "Gerhard Richter", "Giacomo Balla", "Giorgio de Chirico", "Giovanni Battista Gaulli", "Giovanni Battista Piranesi", "Giuseppe Arcimboldo", "Grandma Moses", "Greg Hildebrandt", "Glen Fabry ", "Greg Rutkowski", "Go Nagai ", "Gregory Crewdson", "Goro Fujita ", "Graham Ingels", "Grzegorz Domaradzki", "Guido Borelli da Caluso", "Gustav Klimt", "Gustave Courbet", "Gustave Dor\u00e9", "Gustave Moreau", "Gustave Van de Woestijne ", "H. R. (Hans Ruedi) Giger", "H.P. Lovecraft", "Hans Bellmer", "Harold Elliott", "Helmut Newton", "Henri Rousseau", "Hieronymous Bosch", "Honor\u00e9 Daumier", "Hugh Kretschmer", "Hieronymus Bosch ", "Hope Gangloff ", "Hundertwasser", "Harriet Backer", "Harry Clarke", "Hal Foster ", "Hasui Kawase", "Hannah Hoch", "Hans Baldung", "Heinrich Kley ", "Heinrich Lefler", "Hendrick Goltzius", "Hendrik Kerstens", "Henri de Toulouse-Lautrec", "Henri Matisse", "Henri-Edmond Cross", "Henriette Grindat ", "Hilma af Klint ", "Howard Finster", "Henry Fuseli ", "Henry Ossawa Tanner", "Hirohiko Araki", "Ilya Repin", "Irma Stern", "Ivan Shishkin", "J. J. Grandville", "Jack Gaughan", "James Abbott McNeill Whistler", "Ian McQue ", "lan Miller ", "Isaac Levitan ", "Ismail Inceoglu ", "J.C. Leyendecker ", "Jack Kirby ", "Jacob Hashimoto ", "James C. Christensen", "James Jean ", "Jasmine Becket-Griffith", "James Paick", "James Turrell ", "Jamie Hewlett", "Hiromu Arakawa ", "Howard Hodgkin ", "Huang Guangjian ", "Ida Rentoul Outhwaite ", "Igor Morski ", "Ivan Aivazovsky ", "Ivan Albright ", "J.M.W. Turner ", "Jacek Yerka ", "Jack Butler Yeats ", "Jacob van Ruisdael ", "Jakub Rozalski ", "James Ensor ", "James Gilleard ", "Jane Graverol", "Hiroshi Nagai", "Hugh Ferriss", "Ilya Kuvshinov ", "Ivan Bilibin", "Jack Davis", "James Gurney", "Jaros\u0142aw Ja\u015bnikowski", "Jason Edmiston", "Jean-Antoine Watteau", "Jeff Easley ", "Jeremiah Ketner", "Jean-Baptiste Monge ", "Jeff Koons ", "Jeff Lemire ", "Jeremy Geddes", "Jeremy Lipking", "Joaqu\u00edn Sorolla ", "Joe Fenton ", "Joe Jusko", "John Atkinson Grimshaw", "Johannes Itten", "Jason Limon ", "Jean Arp ", "Jean-Honor\u00e9 Fragonard ", "Jeffrey Catherine Jones ", "Jeffrey Smith ", "Jeffrey T. Larson ", "Jeremy Mann ", "Jesper Ejsing ", "Jim Burns ", "Johannes Vermeer ", "Johfra Bosschart", "Jean Delville ", "Jean-Leon Gerome", "Jean Giraud ", "Jean Metzinger", "Jean-Michel Basquiat", "Joan Miro", "John Bauer ", "John Berkey ", "John Blanche", "John Constable", "Johji Manabe ", "John Frederick Kensett", "John Harris", "John Howe", "John Martin ", "John Perceval", "Jordan Grimmer", "John Hoyland ", "John Philip Falter ", "Josan Gonzalez ", "Josef Albers", "John James Audubon ", "John Singer Sargent ", "Joseph Cornell", "John Kenn Mortensen", "John Lavery", "John William Waterhouse", "Jon Klassen", "Joseph Ducreux", "Joseph Stella", "Jo\u00e3o Artur da Silva", "Judy Chicago ", "Jules Bastien-Lepage", "Julie Bell", "Junji Ito", "Justin Gerard", "Kaethe Butcher", "Kaja Foglio ", "Karl Blossfeldt ", "Karl Schmidt-Rottluff", "Karol Bak ", "Kate Greenaway", "Kati Horna", "Katsuhiro Otomo", "Katsushika Hokusai ", "Kay Nielsen", "Kay Sage", "Kazimir Malevich", "Keith Haring", "Keith Parkinson", "Kelly Freas", "Kelly McKernan ", "Ken Sugimori", "Kitty Lange Kielland", "Kengo Kuma", "Kent Monkman", "Kentaro Miura", "Konstantin Korovin", "Koson Ohara", "Krenz Cushart", "Kilian Eng ", "Kuang Hong", "Kim Jung Gi ", "Kuno Veeber", "K\u00e4the Kollwitz ", "Larry Elmore", "Laurie Greasley", "Laurie Lipton", "Lawren Harris", "Lee Madgwick", "Leiji Matsumoto", "Leon Kossoff", "Leonardo da Vinci", "Leonid Afremov", "Les Edwards", "Liam Wong", "Lisa Frank", "Lisa Keene", "Lise Deharme ", "Louis Comfort ", "Tiffany Lucas Cranach the Elder ", "Lucian Freud M.W. ", "Kaluta Mab Graves", "Louis Wain", "Louise Bourgeois", "Louise Dahl-Wolfe", "Lovis Corinth", "Makoto Shinkai", "Luis Royo ", "Lyonel Feininger ", "Malcolm Liepke ", "Man Ray", "Lyubov Popova", "M.C. Escher", "Marc Chagall", "Marc Simonetti", "Marcel Chagall", "Marcell Chagall", "Marco Mazzoni", "Marek Okon", "Margaret Macdonald Mackintosh", "Maria Sibylla Merian", "Marianne North", "Marianne von Werefkin", "Marius Borgeaud ", "Mark Briscoe ", "Mark Brooks", "Mark Rothko ", "Mark Ryden", "Marsden Hartley ", "Martin Deschambault", "Martin Johnson Heade", "Martine Johanna", "Martiros Saryan ", "Mary Blair", "Mary Cassatt", "Masaaki Sasamoto", "Masamune Shirow", "Mat Collishaw", "Mati Klarwein", "Matt Groening", "Matthias Gr\u00fcnewald", "Matti Suuronen", "Maurice Sendak", "Max Beckmann", "Max Ernst", "Max Pechstein", "Max Weber", "Maxfield Parrish", "Michael Parkes", "Michael Whelan", "Michaelangelo", "Michal Lisowski", "Miho Hirano", "Mikalojus Konstantinas Ciurlionis", "Mike Mignola ", "Mike Winkelmann", "Mikhail Nesterov", "Mikhail Vrubel", "Miles Johnston", "Natalia Goncharova", "Nele Zirnite", "Nicholas Roerich", "Nobuyoshi Araki ", "Noriyoshi Ohrai", "Odd Nerdrum", "Pablo Picasso", "Otto Marseus van Schrieck", "Paul C\u00e9zanne ", "Paul Delvaux", "Patrick Heron ", "Patrick Woodroffe ", "Paul Gustave Fischer ", "Paul Klee ", "Paul Lehr ", "Paula Modersohn-Becker ", "Peter Elson ", "Peter Gric ", "Peter Max ", "Peter Mohrbacher", "Milton Avery ", "Nick Knight ", "Odilon Redon ", "Pascal Blanch\u00e9", "Milton Glaser", "Moebius", "M\u00e9ret Oppenheim", "Nicolas Delort ", "Olafur Eliasson ", "Pascal Campion", "Nikolai Ge ", "Noah Bradley", "Oskar Kokoschka", "Otto Dix", "Philip Guston", "Philippe Druillet ", "Pierre Puvis de Chavannes ", "Pieter Aertsen ", "Pieter Bruegel the Elder ", "Pieter Claesz", "Quentin Blake", "Raphael", "Rafal Olbinski ", "Raphael Lacoste", "Rembrandt van Rijn", "Remedios Varo", "Richard Deacon", "Richard Doyle", "Raffeaello Ossola ", "Ray Caesar ", "Rene Magritte ", "Richard Eurich", "Patrice Murciano ", "Patrick Brown ", "Paul Gauguin ", "Paul Gustav Fischer ", "Peter Andrew Jones ", "Peter Bagge ", "Peter Paul Rubens ", "Petros Afshar ", "Phil Foglio ", "Pierre-Auguste Renoir ", "Piet Mondrian ", "Pieter de Hooch ", "Prateep Kochabua ", "Ralph Horsley ", "Ralph McQuarrie ", "Raymond Briggs ", "Raymond Swanland ", "RHADS ", "Richard Burlet ", "Richard S. Johnson", "Qian Xuan ", "Randolph Caldecott ", "Rebecca Guay", "Richard Corben", "Rob Gonsalves", "Richard Dadd ", "Rob Liefeld", "Rockwell Kent", "Robert Antoine Pinchon", "Rodel Gonzalez", "Robert Crumb", "Robert McCall ", "Rodney Matthews", "Robert Motherwell ", "Roger Dean", "Roberto Ferri", "Romero Britto", "Roberto Matta ", "Ron Walotsky", "Ronald Balfour", "Ross Tran", "Roy Lichtenstein", "Ruan Jian", "Rudolf Hausner", "Russ Mills", "Ryan Hewett", "Ryan McGinley", "Ryohei Hase", "Sailor Moon", "Sally Mann", "Sandra Chevrier", "Sandro Botticelli", "Santiago Caruso", "Salvador Dal\u00ed", "Satoshi Kon", "Sam Bosma", "Shinji Aramaki", "Shohei Otomo", "Shotaro Ishinomori", "Sir James Guthrie", "Siya Oum", "Sofonisba Anguissola", "Sidney Nolan", "Sonia Delaunay", "Scott Listfield", "Simon Bisley", "Sam Mayle", "Shepard Fairey", "Simon Stalenhag", "Sophie Anderson", "Stephen Gammell", "Steve Dillon", "Steve Ditko", "Steve Henderson", "Storm Thorgerson", "Sven Nordqvist", "Syd Mead", "Sydney Prior Hall", "Taiy\u014d Matsumoto", "Takasaki Masaharu", "Stanley Donwood", "Stuart Davis", "Takashi Murakami", "Takato Yamamoto", "Takeshi Obata", "Thomas Blackshear", "Tibor Nagy", "Tom Bagshaw", "Ub Iwerks", "Victor Brauner", "Virgil Finlay", "Wayne Barlowe", "William Blake", "William S Burroughs", "Yasushi Nirasawa", "Tom Thomson", "Ueda Fumito", "Victor Moscoso", "Walt Disney", "Wendy Froud", "William Gropper", "Thomas Cole ", "Tim Doyle ", "Tim Hildebrandt ", "Tomer Hanuka ", "Umberto Boccioni", "Victoria Franc\u00e9s ", "Walter Crane ", "Wes Anderson", "Tatsuro Kiuchi ", "Thomas Eakins ", "Tim White ", "Titian ", "Tony DiTerlizzi ", "Valentine Hugo ", "Viktor Vasnetsov ", "Walter Percy Day ", "Wilfredo Lam ", "William Henry Hunt ", "William Hogarth", "Ted Nasmith ", "Terada Katsuya ", "Terry Oakes", "Tex Avery", "Thomas Gainsborough", "Thomas H\u00e4fner ", "Tivadar Csontv\u00e1ry Kosztka ", "Travis Louie ", "Tsutomu Nihei ", "Tyler Edlin ", "Victo Ngai ", "Victor Adame Minguez", "Thomas Kinkade", "Todd McFarlane", "Vincent Di Fate ", "Warwick Goble", "Vincent Van Gogh ", "Wassily Kandinsky", "Willem de Kooning", "Willem van Haecht", "William Logsdail", "William Morris", "William Stout ", "Yayoi Kusama", "William-Adolphe Bouguereau", "Winslow Homer", "Yanjun Cheng", "Yoshitaka Amano", "Yuri Ivanovich Pimenov", "Yuumei", "Yves Klein", "Yves Tanguay ", "Yves Tanguy", "Zack Snyder \u00c9douard Manet", "Zaha Hadid \u00c9mile Bernard", "Zdzislaw Beksinski", "Zhang Kechun", "Zhichao Cai", "\u00d3scar Dom\u00ednguez"]

# Number of styles and qualities to include in the prompt
numstyles = 3
numquality = 4

while True:
    user_input = input("Press enter to generate a new prompt, or enter a number 1-7 to update the corresponding list in the previous prompt(or enter 'q' to exit): ")
    if user_input == "":
        # Select random elements from the lists
        character = rn.choice(characters)
        obj = rn.choice(objects)
        setting = rn.choice(settings)
        adj = rn.choice(adjectives)
        liststyles = rn.sample(styles, numstyles)
        listmetas =  rn.sample(genmetas, numquality)
        artist = rn.choice(artists)

        # Create the prompt
        prompt = adj + ' ' + character + ' ' + 'with a ' + obj + ' in ' + setting + ', ' + ', '.join(liststyles) + ', ' + ', '.join(listmetas) + ', art by ' + artist

        # Store the prompt and its elements in variables
        prev_prompt = prompt
        prev_characters = character
        prev_objects = obj
        prev_settings = setting
        prev_adjectives = adj
        prev_styles = str(', '.join(liststyles))
        prev_metas = str(', '.join(listmetas))
        prev_artists = artist

        # Print the prompt
        print("\nPrompt:\n      " + prompt)
        print("\n")
        pc.copy(prompt)
    elif user_input == "1":
        prev_adjectives = rn.choice(adjectives)
        prev_prompt = prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' in ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + ', art by ' + prev_artists
        print("\nThe adjectives in the previous prompt has been updated to: \n",prev_adjectives)
        print("\nThe updated prompt is: \n\n",prev_prompt)
        print("\n")
        pc.copy(prev_prompt)
    elif user_input == "2":
        prev_characters = rn.choice(characters)
        prev_prompt = prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' in ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + ', art by ' + prev_artists
        print("The characters in the previous prompt has been updated to: ",prev_characters)
        print("\nThe updated prompt is: \n\n",prev_prompt)
        print("\n")
        pc.copy(prev_prompt)
    elif user_input == "3":
        prev_objects = rn.choice(objects)
        prev_prompt = prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' in ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + ', art by ' + prev_artists
        print("The objects in the previous prompt has been updated to: ",prev_objects)
        print("\nThe updated prompt is: \n\n",prev_prompt)
        print("\n")
        pc.copy(prev_prompt)
    elif user_input == "4":
        prev_settings = rn.choice(settings)
        prev_prompt = prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' in ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + ', art by ' + prev_artists
        print("The settings in the previous prompt has been updated to: ",prev_settings)
        print("\nThe updated prompt is: \n\n",prev_prompt)
        print("\n")
        pc.copy(prev_prompt)
    elif user_input == "5":
        prev_styles = ', '.join(rn.sample(styles, numstyles))
        prev_prompt = prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' in ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + ', art by ' + prev_artists
        print("The styles in the previous prompt has been updated to: ",prev_styles)
        print("\nThe updated prompt is: \n\n",prev_prompt)
        print("\n")
        pc.copy(prev_prompt)
    elif user_input == "6":
        prev_metas = ', '.join(rn.sample(genmetas, numquality))
        prev_prompt = prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' in ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + ', art by ' + prev_artists
        print("The genmetas in the previous prompt has been updated to: ",prev_metas)
        print("\nThe updated prompt is: \n\n",prev_prompt)
        print("\n")
        pc.copy(prev_prompt)
    elif user_input == "7":
        prev_artists = rn.choice(artists)
        prev_prompt = prev_adjectives + ' ' + prev_characters + ' ' + 'with a ' + prev_objects + ' in ' + prev_settings + ', ' + prev_styles + ', ' + prev_metas + ', art by ' + prev_artists
        print("The artist in the previous prompt has been updated to: ",prev_artists)
        print("\nThe updated prompt is: \n\n",prev_prompt)
        print("\n")
        pc.copy(prev_prompt)
    elif user_input == "q":
        break
    else:
        print("Invalid input. Please enter a number 1-6 or press enter to generate a new prompt.")