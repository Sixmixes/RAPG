import random as rn

characters = ["a knight", "a dragon", "a princess", "a wizard"]
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