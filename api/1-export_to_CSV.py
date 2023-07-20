#!/usr/bin/python3
"""extend your script to export data in CSV"""
import csv
import requests
import sys


def export_to_csv():
    """gather and print api data"""
    if(len(sys.argv) != 2):
        print("Error not 3 commands")

    employee_id = sys.argv[1]

    user_data = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                             .format(employee_id)).json()
    todo_data = requests.get('https://jsonplaceholder.typicode.com/todos',
                             params={"userId": employee_id}).json()
    EMPLOYEE_NAME = user_data.get("username")

    f = open('{}.csv'.format(employee_id), 'w')
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for item in todo_data:
        writer.writerow((employee_id, EMPLOYEE_NAME,
                         item.get("completed"), item.get("title")))

    f.close()


if __name__ == "__main__":
    export_to_csv()
