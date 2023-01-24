# promptgeneratorV1
A simple prompt generator script that prints random text prompts for ai art generators.

Prompt Generator
Prompt Generator is a simple script that generates creative prompts for writing, drawing, or other creative endeavors. The script uses random selection to choose elements from predefined lists of characters, objects, settings, adjectives, and styles/qualities to generate a unique prompt each time it is run.

Getting Started
To use the script, simply run it in a Python environment. The script will prompt you to either generate a new prompt or update a previous prompt by entering a number 1-6 corresponding to the component of the prompt you would like to update.

Features
Generates unique prompts each time it is run using random selection from predefined lists
Allows for updating of specific elements of the previous prompt by entering a number 1-6
Can be easily modified to add or remove elements from the predefined lists
Can be used for a variety of creative endeavors such as writing, drawing, or brainstorming
Limitations
The script is currently only set up to generate one prompt at a time. If you want to generate multiple prompts, you will need to run the script multiple times.
The script is currently only set up to update one component of the previous prompt at a time, if you want to update multiple components you will need to re-run the script multiple times.
The script is command-line based and does not currently have a GUI
Conclusion
Prompt Generator is a simple and versatile tool for generating creative prompts. It's a great tool to help with writer's block or to jump start your creative endeavors. With its ability to update the previous prompt, you can continue to refine your prompt to your liking. If you have any questions or suggestions for improvements, please feel free to reach out.

List Formatter - 

The list formatter is a program that allows you to create, edit, save, and view lists for use in text prompt generators and other applications. The program is written in Python and is designed to format the dataset in a way that makes it easy to copy and paste into other programs.

Features
Add items to the dataset: You can add new items to the dataset one at a time. If you want to add multiple items, you can do that as well by typing 'q' to exit the add item option.

Remove items from the dataset: You can remove an existing item from the dataset by typing in the item name.

Save dataset to file: You can save the dataset to a file in the format of ["name1", "name2", "name3", etc...] so that you can easily open the file and copy and paste the formatted list into other programs.

Edit dataset: You can edit existing items within the dataset.

View number of items in dataset: You can view the number of items in the dataset.

Quit: You can quit the program at any time by selecting the 'Quit' option from the menu.

Usage
To run the program, you will need to have Python installed on your computer. Once you have Python installed, you can run the program by opening a terminal or command prompt, navigating to the directory where the script is located, and typing python dataset_manager.py.

The program will display a menu of options that you can choose from. You can add items to the dataset, remove items from the dataset, save the dataset to a file, edit the dataset, view the number of items in the dataset, and quit the program.

You can also edit the script to add multiple datasets, by creating a new list and a while loop for each one. You can also consider creating a function to handle this process, so you can call it multiple times and pass it the name of the dataset and the list.

Please note that the program does not allow for duplicate items to be added to the dataset. If you attempt to add an item that already exists in the dataset, the program will inform you that the item already exists and prompt you to enter a different item.

Additionally, the program uses the json library to save the dataset to file, and the file is saved in json format.

Limitations
The program can only handle one dataset at a time. If you want to use multiple datasets, you will need to create multiple instances of the program or edit the script to handle multiple datasets.
The program is command-line based and does not currently have a GUI.
The program only accepts input in the form of text strings and does not currently support other data types such as numbers or dates.
Conclusion
Dataset Manager is a versatile and easy-to-use tool for creating, editing, and managing datasets. It is designed to make it easy to format and save datasets for use in other programs, and can be used for a variety of applications. If you have any questions or suggestions for improvements, please feel free to reach out.