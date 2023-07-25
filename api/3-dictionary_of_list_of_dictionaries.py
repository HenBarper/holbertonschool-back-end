#!/usr/bin/python3
""" Dictionary of list of dictionaries """
import json
import requests
import sys

def record_all_tasks():
    """gather and print api data"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users"
    todo_url = f"{url}/todos"
    user_data = requests.get(user_url).json()
    todo_data = requests.get(todo_url).json()

    user_dict = {str(user['id']): {"username": user['username'], "tasks": []} for user in user_data}
    for task in todo_data:
        user_id = str(task['userId'])
        task_data = {"task": task['title'], "completed": task['completed']}
        user_dict[user_id]["tasks"].append(task_data)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_dict, f)

if __name__ == "__main__":
    record_all_tasks()
