#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import 

import requests
import sys

EMPLOYEE_API_URL = "https://jsonplaceholder.typicode.com/users/{employee_id}"
TODO_API_URL = "https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

employee_id = int(sys.argv[1])

# Fetch employee information
employee_response = requests.get(EMPLOYEE_API_URL.format(employee_id=employee_id))
employee_data = employee_response.json()
employee_name = employee_data['name']

# Fetch employee's todo list
todo_response = requests.get(TODO_API_URL.format(employee_id=employee_id))
todo_data = todo_response.json()

# Calculate progress
total_tasks = len(todo_data)
done_tasks = len([task for task in todo_data if task['completed']])
progress = done_tasks / total_tasks * 100

# Print progress and completed tasks
print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
for task in todo_data:
    if task['completed']:
        print(f"\t{task['title']}")


