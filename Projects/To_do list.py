list_today = []
task_completed = set()

def display_lists(list_today):
    print("To-do lists:")
    
    for tasks in list_today:
        print(f"[{tasks}]")

def add_list(list_today):
    task = input("Enter the task you want to add to your list: ")
    list_today.append(task)
    print("Added!")
    return list_today

def completed_list(list_today, task_completed):
    completed_task = input("Enter the task you finished: ")
    if completed_task in list_today:
        task_completed.add(completed_task)
        list_today.remove(completed_task)
        print("Task marked as completed and removed from to-do list.")
    else:
        print("Task not found in the to-do list.")

while True:
    print("Menu:")
    print("1. Show your tasks")
    print("2. Add a task")
    print("3. Remove a completed task")
    print("4. Exit")

    user = int(input("Choose what to display (1/2/3/4): "))
    
    if user == 1:
        if not list_today:
            print("Sorry, there is no task to show")
        display_lists(list_today)
    elif user == 2:
        add_list(list_today)
    elif user == 3:
        completed_list(list_today, task_completed)
    elif user == 4:
        print("Quitting...")
        break
    else:
        print("Error!")
