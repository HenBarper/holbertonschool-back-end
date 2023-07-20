#!/usr/bin/python3
"""extend your script to export data in CSV"""
import csv
import requests
import sys


def export_to_csv():
    """gather and print api data"""
    if(len(sys.argv) != 2):
        print("Error not 3 commands")

    USER_ID = sys.argv[1]

    user_data = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(USER_ID)).json()
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={"userId": USER_ID}).json()
    EMPLOYEE_NAME = user_data.get("username")

    with open('{}.csv'.format(USER_ID), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for item in todo_data:
            writer.writerow((USER_ID, EMPLOYEE_NAME,
                            item.get("completed"), item.get("title")))


if __name__ == "__main__":
    export_to_csv()
