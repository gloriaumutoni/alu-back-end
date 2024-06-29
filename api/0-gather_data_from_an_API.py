#!/usr/bin/python3
"""
Python script that returns TODO list progress for a given employee ID
"""
import requests
from sys import argv

<<<<<<< HEAD
=======


>>>>>>> 06b2b817633e70bf753da09c8db1ed4d28f41a5d
def get_employee_info(employee_id):
    """
    Get employee information by employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/'
    response = requests.get(url)
    return response.json()

<<<<<<< HEAD
=======

>>>>>>> 06b2b817633e70bf753da09c8db1ed4d28f41a5d
def get_employee_todos(employee_id):
    """
    Get the TODO list of the employee by employee ID
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    return response.json()

<<<<<<< HEAD
=======

>>>>>>> 06b2b817633e70bf753da09c8db1ed4d28f41a5d
def main(employee_id):
    """
    Main function to fetch and display the TODO list progress of the employee
    """
    employee = get_employee_info(employee_id)
    employee_name = employee.get("name")

    emp_todos = get_employee_todos(employee_id)
    tasks = {todo.get("title"): todo.get("completed") for todo in emp_todos}

    total_tasks = len(tasks)
    completed_tasks = [completed for completed in tasks.values() if completed]
    completed_tasks_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks"
          f"({completed_tasks_count}/{total_tasks}):")
    for title, completed in tasks.items():
        if completed:
            print(f"\t {title}")

<<<<<<< HEAD
=======

>>>>>>> 06b2b817633e70bf753da09c8db1ed4d28f41a5d
if __name__ == "__main__":
    if len(argv) > 1:
        main(argv[1])
    else:
<<<<<<< HEAD
        print("Usage: ./0-gather_data_from_an_API.py <employee_id")
=======
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
>>>>>>> 06b2b817633e70bf753da09c8db1ed4d28f41a5d
