# objectives 
# Add Tasks: Users should be able to add new tasks to the list.
# View Tasks: Users should be able to see all the tasks listed.
# Edit Tasks: Users should be able to modify the details of existing tasks.
# Delete Tasks: Users should be able to remove tasks from the list.

#reqiorements:
#   for this: must be a simple text based interface in the console
#   tasks can be stored in a local file (like a JSON or CSV file) or in memory (using a simple lists

#create tasks via memory

#requires allocating memeory on a heap:'

def Add():
    global lst
    Adding = str(input())

    lst.append(Adding)

def View():
    global lst
    print(lst)
    
def Delete():
    global lst
    lst.clear()

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

    #               
if __name__ == "__main__":
    main()