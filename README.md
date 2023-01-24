AI Art Text Prompt Generator

This program is designed to generate creative prompts for AI art generators. The program uses 
a set of predefined lists of characters, objects, settings, adjectives and styles to randomly 
generate a new prompt every time the user presses enter. The user can also choose to update 
any of the elements in the previous prompt by entering a number between 1-6, corresponding to 
the elements in the prompt.

To use this program, the user will first need to run the program and then press enter to 
generate the first prompt. The user can then choose to generate a new prompt or update any of 
the elements in the previous prompt. The program also allows the user to update the prompt 
with new elements from a .json file, this can be done by using the "List Formatter" program. 
The List Formatter program can be used to create different components for the variables in 
this program.

By using the List Formatter program, the user can add new words to the predefined lists and 
save them to a .json file, which can be later loaded into this program to update the existing 
lists. This allows for greater flexibility and creativity when generating prompts.

It is important to note that this program is designed for the purpose of providing inspiration 
for AI art and should not be used for any other purpose.

List Formatter README - 

List Formatter is a simple program that allows the user to store words in a dataset in the format 
of ["item1", "item2", "item3", etc...]. The use case for this program is to enter words and add 
them to lists in this format so that the user can later open the .json file and copy and paste 
all of its contents to another program for text prompt generation for AI art.

The program has a main menu with the following options:

1. Load list - allows the user to load a previously saved dataset from a .json file
2. Edit list - allows the user to add or remove items from the current dataset
3. Quit - exits the program
4. View loaded list - displays the current dataset

When the user chooses to "Load list" option, the program will display a list of all .json files 
in the current directory, and the user can select the file they wish to load.

NOTE: if you want to add your own empty .json files it must contain [] brackets initally.

When the user chooses to "Edit list" option, the user will be able to add new items to the 
dataset or remove items that already exist in the dataset. The user will also be prompted 
to save the changes made to the dataset.

When the user chooses the "View loaded list" option, the program will display the current 
dataset.

The program also has a confirmation prompt before quitting to ensure that the user does not 
accidentally exit without saving their work.

In summary, List Formatter is a simple program that allows the user to easily create and 
edit datasets in a specific format for use in other programs such as text prompt generators 
for AI art.

props to @526christian for inspiring me to make this
https://github.com/526christian 

