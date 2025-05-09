#Python automatically allocates memory
#convert python objects into strings, can write and read json data to a file
import json

def Add():
    global lst
    Adding = str(input())
    with open("Tasks.json", "w") as task:   #creates json file to add contents of list within file
        task.write(Adding)

def View():
    global lst
    with open("Tasks.json", "r") as file:   #meant to read content of file
        tasks = json.load(file)
        print(tasks)
    
def Delete():
    global lst
    open("Tasks.json", "w").close()     #meant to delete data within json file if user decides to

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

    if choice == 4:
        Delete()

if __name__ == "__main__":
    main()