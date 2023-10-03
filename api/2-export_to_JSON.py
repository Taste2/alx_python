import requests
import sys
import json

# Function to fetch employee TODO list progress and export to JSON
def get_employee_todo_and_export_to_json(employee_id):
    # Define API endpoints
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Make requests to the API
    todo_response = requests.get(todo_url)
    user_response = requests.get(user_url)

    # Check if requests were successful (status code 200)
    if todo_response.status_code == 200 and user_response.status_code == 200:
        todo_data = todo_response.json()
        user_data = user_response.json()

        # Extract relevant information
        employee_id = user_data["id"]
        employee_username = user_data["username"]

        # Create a list to store task information
        tasks_list = []

        # Iterate through tasks and add to the list
        for task in todo_data:
            task_info = {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_username
            }
            tasks_list.append(task_info)

        # Create a dictionary with the user ID as the key and tasks list as the value
        user_tasks = {str(employee_id): tasks_list}

        # Define JSON file path
        json_file_path = f"{employee_id}.json"

        # Write JSON data to the file
        with open(json_file_path, 'w') as json_file:
            json.dump(user_tasks, json_file, indent=4)

        print(f"Data has been exported to {json_file_path}")

    else:
        print(f"Failed to retrieve data. Status codes: {todo_response.status_code}, {user_response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
    else:
        employee_id = sys.argv[1]
        get_employee_todo_and_export_to_json(employee_id)
