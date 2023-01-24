import os
import json
import ast

# Initialize an empty list to store the dataset
current_dataset = ""

while True:
    # Print menu options
    print("1. Load list")
    print("2. Edit list")
    print("3. Quit")
    print("4. View loaded list")
    
    # Get user input
    option = input("Enter an option: ")

    if option == "1":
        while True:
            print("List files:")
            # Get all json files in current directory
            json_files = [f for f in os.listdir() if f.endswith('.json')]
            for i, file in enumerate(json_files):
                print(f"{i+1}. {file}")
            # Get file number from user
            file_num = input("Enter file number (or 'q' to exit): ")
            if file_num == "q":
                break
            try:
                file_num = int(file_num)
                # Load dataset from json file
                with open(json_files[file_num-1], "r") as f:
                    dataset = json.load(f)
                dataset = list(dataset)
                current_dataset = json_files[file_num-1]
                print(f"{current_dataset} loaded.")
                break
            except (ValueError, IndexError) as e:
                print(f"Invalid input, please try again. Error: {e}")
                
    elif option == "2":
        if not current_dataset:
            print("No dataset loaded. Please load a dataset first.")
            continue
        print(f"Editing {current_dataset}")
        while True:
            print("1. Add item to dataset")
            print("2. Remove item from dataset")
            print("3. Back")
            action = input("Enter an option: ")
            if action == "1":
                while True:
                    item = input("Enter item to add (or 'q' to exit): ")
                    if item == "q":
                        break
                    if item in dataset:
                        print(f"{item} already exists in the dataset")
                        continue
                    dataset.append(item)
                    print(f"{item} added to dataset: {dataset}")
            elif action == "2":
                item = input("Enter item to remove: ")
                try:
                    dataset.remove(item)
                except ValueError:
                    print(f"{item} not found in the dataset.")
            elif action == "3":
                break
            else:
                print("Invalid input, please try again.")
            save = input("Save changes? (y/n) ")
            if save == "y":
                formatted_dataset = "[" + ",".join(dataset) + "]"
                with open(current_dataset, "w") as f:
                    json.dump(dataset, f)
                print(f"{current_dataset} saved.")
                break
    elif option == "3":
        # Quit
        break
    elif option == "4":
        if not current_dataset:
            print("No dataset loaded. Please load a dataset first.")
            continue
        print(f"Dataset: {json.load(dataset)}")
    else:
        print("Invalid input, please try again.")
