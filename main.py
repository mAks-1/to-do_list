import json

def return_json():
    try:
        with open("data.json", "r") as json_file:
            content = json_file.read().strip()
            return json.loads(content) if content else []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in data.json. Replacing with an empty list.")
        return []

def add_task():
    task = input('Enter a task to add: ')
    try:
        data = return_json()

        task_id = max((item["id"] for item in data), default=0) + 1

        new_task = {"id": task_id, "name": task, "status": "not done"}
        data.append(new_task)

        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print(f'Task "{task}" added successfully with ID {task_id}!')

    except Exception as e:
        print(f"An error occurred: {e}")

def delete_task():
    while True:
        # task_id = input('Enter an ID of the task you want to delete: ')
        try:
            while True:
                task_id = input('Enter an ID of the task you want to delete: ')
                try:
                    task_id = (int(task_id))
                    break
                except Exception:
                    print('Incorrect input\n')
                    continue
                
            data = return_json()
            print(data)
            task = None
            for i in range(len(data)-1):
                if data[i]['id'] == task_id:
                    task = data[i]['name']
                    del data[i]

            if task is None:
                print(f'Task with ID {task_id} was not found.')
            else:
                with open("data.json", "w") as json_file:
                    json.dump(data, json_file, indent=4)

                print(f'Task "{task}" with ID {task_id} has been successfully deleted!')
            break

        except Exception as e:
            print(f"An error occurred: {e}")

def update_task():
     while True:
        try:
            while True:
                task_id = input('Enter an ID of the task you want to update: ')
                try:
                    task_id = (int(task_id))
                    break
                except Exception:
                    print('Incorrect input\n')
                    continue
                
            task_to_update = None

            data = return_json()
            print(data)

            for task in data:
                if task['id'] == task_id:
                    task_to_update = task
                    break

            if not task_to_update:
                print(f"Task with ID {task_id} not found.")
                break
            
            new_task_name = input('Enter a new name for the task: ')
            if new_task_name is not None:
                task_to_update["name"] = new_task_name

            new_task_satus = input('Enter a new status for the task: ')
            if new_task_satus is not None:
                task_to_update["status"] = new_task_satus

            with open("data.json", "w") as json_file:
                json.dump(data, json_file, indent=4)

            print(f'Task with ID "{task_id}" has been succesfully updated!')
            break

        except Exception as e:
            print(f"An error occurred: {e}")

def show_tasks(choice):
    try:
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            i = 1
            if choice == 4:
                for task in data:
                    print(f'{i}) Task: {task['name']}, id: {task['id']}, status: {task['status']}')
                    i+=1
            if choice == 5:
                for task in data:
                    if task['status'] == 'done':
                        print(f'{i}) Task: {task['name']}, id: {task['id']}, status: {task['status']}')
                        i+=1
            if choice == 6:
                for task in data:
                    if task['status'] == 'not done':
                        print(f'{i}) Task: {task['name']}, id: {task['id']}, status: {task['status']}')
                        i+=1
            if choice == 7:
                for task in data:
                    if task['status'] == 'in progress':
                        print(f'{i}) Task: {task['name']}, id: {task['id']}, status: {task['status']}')
                        i+=1
    except FileNotFoundError:
        print(f'An error occured: {FileNotFoundError}')
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in data.json.")
    
def main():
    while True:
        print('\nThis is a to-do list\n')
        print('1. Add a task\n2. Delete a task\n3. Update a task\n4. List all tasks\n5. List all tasks that are done\n6. List all tasks that are not done\n7. List all tasks that are in progress\n8. EXIT')
        choice = input('Enter your choice: ')

        try:
            choice = int(choice)
            if choice == 1:
                add_task()
            elif choice == 2:
                delete_task()
            elif choice == 3:
                update_task()
            elif choice in (4,5,6,7):
                show_tasks(choice)
            elif choice == 8:
                print("Goodbye!")
                break
            else:
                print('Invalid choice. Please enter a number between 1 and 8.\n')
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 8.\n')

main()