#Python automatically allocates memory
#convert python objects into strings, can write and read json data to a file
import csv

def Add():
    task = str(input("Enter a new task: "))
    with open("Tasks.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([task])  # writewrow method used to insert user input into a row

def View():
    with open("Tasks.csv", 'r') as file:
        csv_reader = csv.reader(file)   #outputs file contents
        for row in csv_reader:
            print(row)

def Edit():     #can allow user to alter tasks via column numbers
    with open("Tasks.csv", 'r') as file:
        csv_reader = csv.reader(file)   #reader method meant to read through csv file printed to the console
        rows = list(csv.reader(file))   #creates a list of my csv files

    for i in rows:      #loop through list of data and outputs it for viewers sake
        print(i)

    row_index = int(input("Based of the tasks here pick a task number to edit: ")) - 1  #access number to alter the task column

    new_task = input("Enter the new task text: ")   #create a new text to overwrite the prior one

    # Update task text
    rows[row_index][0] = new_task

    # Write updated list back to the CSV file
    with open("Tasks.csv", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    

def Delete():
    open("Tasks.csv", "w").close()     #meant to delete data within csv file if user decides to

def main():
    print("1. To add to tasks")
    print("2. To view tasks")
    print("3. To edit tasks")
    print("4. To delete tasks\n")
    choice = int(input("Choose: "))
    if choice == 1:

        Add()

    if choice == 2:

        View()

    if choice == 3:

        Edit()

    if choice == 4:
        print("Tasks deleted")

        Delete()

main()