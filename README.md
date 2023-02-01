# AI Art Text Prompt Generator

This program is designed to generate creative prompts for AI art generators. The program uses 
a set of predefined lists of characters, objects, settings, adjectives and styles to randomly 
generate a new prompt every time the user presses enter. The user can also choose to update 
any of the elements in the previous prompt by entering a number between 1-7, corresponding to 
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

# List Formatter README - 

List Formatter is a simple program that allows the user to store words in a dataset in the format 
of ["item1", "item2", "item3", etc...]. The use case for this program is to enter words and add 
them to lists in this format so that the user can later open the .json file and copy and paste 
all of its contents to another program for text prompt generation for AI art.

## The program has a main menu with the following options:

1. Load list - allows the user to load a previously saved dataset from a .json file
2. Edit list - allows the user to add or remove items from the current dataset
3. Quit - exits the program
4. View loaded list - displays the current dataset

When the user chooses to "Load list" option, the program will display a list of all .json files 
in the current directory, and the user can select the file they wish to load.

## NOTE: if you want to add your own empty .json files it must contain [] brackets initally.

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

# Steps to Create a Batch File to Run a Python Script

## Step 1: Create the Python Script
To start, create your Python Script.

For example, let’s create a simple Python script that contains a countdown (alternatively, you may use any Python script that you wish to run):

```
countdown = 10

while countdown > 0:
    print ('CountDown = ', countdown)
    countdown = countdown - 1
```

##Step 2: Save your Script
Save your Python script (your Python script should have the extension of ‘.py‘).

For our example, let’s save the Python script as: Promptgen

Where the file extension is .py

## Step 3: Create the Batch File to Run the Python Script
To create the batch file, open Notepad and then use the following template:

```
@echo off
"Path where your Python exe is stored\python.exe" "Path where your Python script is stored\script name.py"
pause
```

You’ll need to adjust the syntax in two places:

“Path where your Python exe is stored\python.exe”
Here is an example where a Python exe is located: “C:\Users\Ron\AppData\Local\Programs\Python\Python39\python.exe”
“Path where your Python script is stored\script name.py”
And here is an example where a Python script is located:
“C:\Users\Ron\Desktop\Test\promptgen.py”

Note that you’ll need to change the paths to reflect the locations where the files are stored on *your* computer.

This is how the batch script would look like in Notepad for our example:

```
@echo off
"C:\Users\Ron\AppData\Local\Programs\Python\Python39\python.exe" "C:\Users\Ron\Desktop\Test\promptgen.py"
pause
```
Save the Notepad with a ‘.bat‘ extension. For example, let’s save the Notepad as Run_Script.bat

A new batch file, called “Run_Script.bat,” will be created at your specified location.