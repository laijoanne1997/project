#practising the task tracker project on roadmap
#task tracker is a simple command line interface to track what needs to be done
import datetime
import random
import json

#should store tasks as a json file
#should be able to add, delete, update, mark task, list all task, list all that are done, list all that are not done, list all in progress

def saving_file(task_list):
    with open("tasks.json", "w") as file:
        json.dump(task_list, file)
    print("Tasks saved to file")

def loading_file(task_list):
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def adding_task(task_list, task, id="", description="", status="to do", created_at=datetime.datetime.now().strftime("%d %B %Y")):
    number = random.randint(1, 100)
    task_list.append({"task": task, "id": number, "description": description, "status": status, "created_at": created_at})
    print(f"{task} added to list (ID: {number} )")
    return task_list

def update_description(task_list, task, description, updated=datetime.datetime.now().strftime("%d %B %Y")):
    for tasks in task_list:
        if tasks["task"] == task:
            tasks["description"] = description
            tasks["updated"] = updated
            print(f"{task} description updated to '{description}'")
            return task_list

def delete_task(task_list, task):
    for tasks in task_list:
        if tasks["task"] == task:
            task_list.remove(tasks)
            return task_list
    if task not in task_list:
        print(f"{task} not in list")

def printing_tasks(task_list):
    for tasks in task_list:
        update = tasks.get("updated", "Not yet")
        print(f"Task: {tasks['task']} | ID: {tasks["id"]} | Status: {tasks["status"]} | Description: {tasks['description']} | Created: {tasks["created_at"]} | Last updated: {update}")

def update_status(task_list, task, status, updated=datetime.datetime.now().strftime("%d %B %Y")):
    for tasks in task_list:
        if tasks["task"] == task:
            tasks["status"] = status
            tasks["updated"] = updated
            return task_list

#up to creating a menu to add, update description or status, delete task, list all task, list by status

def show_menu():
    print("--Menu--")
    print("1. Add task")
    print("2. Update task")
    print("3. Delete task")
    print("4. Print tasks")
    print("5. Exit")

list = loading_file()

while True:
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 5:
        print ("Exiting...")
        break
    elif choice == 1:
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        adding_task(list, task_name, task_description)
        saving_file(list)
    elif choice == 2:
        print("Do you want to update 1. Description or 2. Status")
        pick = int(input("Enter your choice: "))
        if pick == 1:
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")
            update_status(list, task_name, task_description)
            saving_file(list)
        elif pick == 2:
            task_name = input("Enter task name: ")
            task_status = input("Enter task status: ")
            update_status(list, task_name, task_status)
            saving_file(list)
    elif choice == 3:
        printing_tasks(list)
        print("Which task would you like to delete?")
        deleting_task = str(input("Enter the task: "))
        delete_task(list, deleting_task)
        saving_file(list)
    elif choice == 4:
        printing_tasks(list)

