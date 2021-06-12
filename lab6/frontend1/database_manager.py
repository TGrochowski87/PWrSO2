from pymongo import MongoClient


def add_task(text):
    client = MongoClient("database", 27017)

    task = {
        "text": text,
        "checked": False
        }
    tasks = client.sub_db.tasks
    tasks.insert_one(task)

def get_tasks_unchecked():
    client = MongoClient("database", 27017)

    tasks = client.sub_db.tasks
    
    return tasks.find({'checked': False})

def get_tasks_checked():
    client = MongoClient("database", 27017)

    tasks = client.sub_db.tasks
    
    return tasks.find({'checked': True})

def change_task_status(text):
    client = MongoClient("database", 27017)

    tasks = client.sub_db.tasks

    newChecked = False
    task_list = tasks.find()
    for task in task_list:
        if str(task['text']) == text:
            if task['checked'] == False:
                newChecked = True

    tasks.update({'text' : text}, {'$set': {'checked': newChecked}})