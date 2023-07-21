#!/usr/bin/python3
""" Export to JSON """
import json
import requests
import sys


def export_user_to_json():
    """export user id data to json format"""
    if(len(sys.argv) != 2):
        print("Error not 3 commands")

    USER_ID = sys.argv[1]

    user_data = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(USER_ID)).json()
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={"userId": USER_ID}).json()
    EMPLOYEE_UN = user_data.get("username")
    EMPLOYEE_NAME = user_data.get("name")
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

    completed_tasks = []

    for item in todo_data:
        TOTAL_NUMBER_OF_TASKS += 1
        if item.get("completed"):
            NUMBER_OF_DONE_TASKS += 1
            completed_tasks.append(item.get("title"))

    counter = 0
    task_list = []
    complete_status_list = []
    for thing in todo_data:
        counter += 1
        task_list.append(thing.get("title"))
        complete_status_list.append(thing.get("completed"))

    json_list = []
    for i in range(counter):
        new_dict = {
            "task": task_list[i],
            "completed": complete_status_list[i],
            "username": EMPLOYEE_UN
        }
        json_list.append(new_dict)

    json_dict = {
        f"{USER_ID}": json_list
    }

    json_object = json.dumps(json_dict)

    with open('{}.json'.format(USER_ID), 'w') as f:
        f.write(json_object)

    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    export_user_to_json()
