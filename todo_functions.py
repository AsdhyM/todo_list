import csv
# import json

def add_todo(file_name):
    print("Add todo")
    # Ask the title of the todo
    todo_name = input("Enter a todo: ")
    # Open file - list.csv
    with open(file_name, "a") as f:     # "a" means append
        writer = csv.writer(f)
        # Insert values - title = user entered
                      # - completed = False
        writer.writerow([todo_name, "False"])
    
    
                    

def remove_todo(file_name):
    print("Remove todo")

def mark_todo(file_name):
    print("Mark todo")

def view_todo(file_name):
    print("View todo")