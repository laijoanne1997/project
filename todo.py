#practising the task tracker project on roadmap
#task tracker is a simple command line interface to track what needs to be done
import datetime
import random

#should store tasks as a json file
#should be able to add, delete, update, mark task, list all task, list all that are done, list all that are not done, list all in progress

list = []

def adding_task(task_list, task, id="", description="", status="to do", created_at=datetime.datetime.now().strftime("%d %B %Y")):
    task_list.append({"task": task, "id": random.randint (0,100), "description": description, "status": status, "created_at": created_at})
    print(f"{task} added to list (ID: )")
    return task_list

def updating_task(task_list, task, description, updated=datetime.datetime.now().strftime("%d %B %Y")):
    for tasks in task_list:
        if tasks["task"] == task:
            tasks["description"] = description
            tasks["updated"] = updated
            print(f"{task} description updated to {description}")
            return task_list

def delete_task(task_list, task):
    for tasks in task_list:
        if tasks["task"] == task:
            task_list.remove(tasks)
            return task_list
    if task not in task_list:
        print(f"{task} not in list")



adding_task(list, "swimming")
adding_task(list, "sleeping")
print (list)

updating_task(list, "swimming", "going to the pool")

print(list)

delete_task(list, "sleeping")
print(list)