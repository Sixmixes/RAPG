import random as rn
import pyperclip as pc
import json

    #.json loaded from lists>characters directory(customize or change the json file to your liking)
with open('lists/characters/char.json', 'r') as file:
    characters = json.load(file)

    #.json loaded from lists>objects directory(customize or change the json file to your liking)
with open('lists/objects/scifantasy-obj.json', 'r') as file:
    objects = json.load(file)

    #.json loaded from lists>settings directory(customize or change the json file to your liking)
with open('lists/settings/settings.json', 'r') as file:
    settings = json.load(file)

    #.json loaded from lists>adj directory(customize or change the json file to your liking)
with open('lists/adj/adj.json', 'r') as file:
    adjectives = json.load(file)

    #.json loaded from lists>styles directory(customize or change the json file to your liking)
with open('lists/styles/styles.json', 'r') as file:
    styles = json.load(file)

    #.json loaded from lists>genmeta directory(customize or change the json file to your liking)
with open('lists/genmeta/genmeta.json', 'r') as file:
    genmetas = json.load(file)

    #.json loaded from lists>artists directory(customize or change the json file to your liking)
with open('lists/artists/artists.json', 'r') as file:
    artists = json.load(file)

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