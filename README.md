# Random Art Prompt Generator(RAPG)

Welcome to the Random Art Prompt Generator, where your creative spirit gets a kick in the pants! With just the press of a button (or the enter key), you'll be transported to a world of adjectives, characters, objects, settings, styles, meta elements, and artists. Where your imagination takes you from there is up to you!

To get started, simply run the program and press enter. You'll be greeted with a brand new art prompt, complete with all the elements you need to get your creative juices flowing. If you want to update any of the elements in the prompt, simply enter the corresponding number (1-7) and you'll be given a new element in that category. Want to generate a new prompt entirely? Just press enter!

**The prompts are copied to your clipboard after they are generated and after you change one of the components using "1-7". All you have to do is go to your art generator and paste it!**

This program is fully customizable - you can add or change elements in the .json files located in the "lists" directory to your liking. So go ahead, get inspired, and create something amazing!

Just remember, this is just the starting point for your imagination. The final product is entirely up to you and your creativity, so have fun and let your imagination run wild!

**Disclaimer: Using this program may cause excessive creativity and artistic inspiration. Use at your own risk!**

# Welcome to List Manager!

List Manager is a tool to manage and modify your lists with ease. Whether you're looking to update your RAPG(Random Art Prompt Generator) lists or any other list, List Manager is here to help.

### Features

   - Load a list from a .json file
   - Edit a loaded list by adding or removing items
   - Quit the program
   - View the loaded list

### How to Use

   - Start the program by running the python file.
   - Select an option from the main menu.
      - Load list: Select this option to load a list from a .json file in your current directory or a subdirectory.
      - Edit list: Select this option to add or remove items from the loaded list.
      - Quit: Select this option to exit the program.
      - View loaded list: Select this option to view the contents of the loaded list.
   - Follow the on-screen prompts to complete the selected action.

### Tips

   - Make sure to save changes to the list before quitting to ensure your changes are preserved.
   - If you encounter any issues, check the .json file format to ensure it is valid.

With List Manager, managing your lists has never been easier! Let's get started!

**_NOTE: if you want to add your own empty .json files it must contain [] brackets initally._**

When the user chooses the "Edit list" option, the user will be able to add new items to the 
loaded list or remove items that already exist in the list. The user will also be prompted 
to save the changes made to the dataset when exiting edit mode.(you must exit edit mode after you have edited to save changes.)

When the user chooses the "View loaded list" option, the program will display the current 
list.

The program also has a confirmation prompt before quitting to ensure that the user does not 
accidentally exit without saving their work.

In summary, List Formatter is a simple program that allows the user to easily create and 
edit lists in a specific format for use in RAPG.


# Steps to Create a Batch File to Run a Python Script

### To create your own batch file for the script:

   1. Create a new .txt file and paste the following code into it:

     @echo off
     "Path where your Python exe is stored\python.exe" "Path where your Python script is stored\script name.py"
     pause

   2. Replace "Path where your Python exe is stored" with the actual path to your Python executable, and replace "Path where your Python script is stored\script name.py" with the actual path to your Python script.
   3. Save the .txt file and change its extension to .bat, for example, "run_script.bat".
   4. Place the batch file in the same directory as the prompt generator script because the .jsons load from directories within the root of the promptgen script.

And don't worry, it's easy, even easier than trying to catch a greased pig!

### To make a shortcut to the batch file:

   1. Right-click on the .bat file and select "Copy".
   2. Navigate to the location where you want the shortcut to be and right-click, then select "Paste Shortcut".
   3. The shortcut to your batch file can now be accessed from anywhere on your system for easy access.

# Important Info:

This process for creating a batch file and running the Python script has been tested on Windows 10. If you are using a different operating system such as MacOS or Linux, you can create a similar script using a shell script. To do this, you will need to use a different file extension, such as .sh, and use the appropriate shell interpreter to run the script. You can learn more about creating shell scripts by searching online or consulting the documentation for your operating system.

### Hat Tips: 

props to @526christian for inspiring me to make this
https://github.com/526christian 
