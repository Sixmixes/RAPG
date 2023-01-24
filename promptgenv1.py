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