#practising the task tracker project on roadmap
#task tracker is a simple command line interface to track what needs to be done
import datetime


#should store tasks as a json file
#should be able to add, delete, update, mark task, list all task, list all that are done, list all that are not done, list all in progress

list = []

def adding_task(task_list, task, id, description, status="to do", created_at=datetime.datetime.now()):
    task_list.append({"task": task, "id": id, "description": description, "status": status, "created_at": created_at})
    return task_list
