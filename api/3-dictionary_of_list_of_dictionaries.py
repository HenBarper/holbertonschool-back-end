#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import requests
import sys


def record_all_tasks():
    """gather and print api data"""

    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    counter = 0
    # id_list = []
    # task_list = []
    # complete_status_list = []
    # username_list = []
    for thing in todo_data:
        if thing.get("userId") > counter:
            counter += 1
        # id_list.append(counter)
        # task_list.append(thing.get("title"))
        # complete_status_list.append(thing.get("completed"))
        # username_list.append(thing.get("username"))
    
    todo_list = []
    for i in range(1, counter):
        todo_list.append(requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={"userId": i}).json())

    for i in range(len(todo_list)):
        json_list = []
        new_dict = {
                "username": username_list[j],
                "task": task_list[j],
                "completed": complete_status_list[j],
            }
        json_list.append(new_dict)
        json_dict = {
        f"{USER_ID}": json_list
        }
            

    # for i in range(len(todo_list)):
    #     print(todo_list[i])

    # for j in range(id_list):
    #     json_dict = {
    #         f"{id_list[j]}": 
    #     }
    # json_list = []
    # for i in range(counter):
    #     new_dict = {
    #         "username": username_list[i],
    #         "task": task_list[i],
    #         "completed": complete_status_list[i],
    #     }
    #     json_list.append(new_dict)

    # json_object = json.dumps(json_dict)

    # with open('todo_all_employees.json', 'w') as f:
    #     f.write(json_object)


if __name__ == "__main__":
    record_all_tasks()
