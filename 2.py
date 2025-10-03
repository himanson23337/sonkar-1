
import json
import os

TODO_FILE = 'todo_list.json'

def load_tasks():
	if not os.path.exists(TODO_FILE):
		return []
	with open(TODO_FILE, 'r') as f:
		return json.load(f)

def save_tasks(tasks):
	with open(TODO_FILE, 'w') as f:
		json.dump(tasks, f, indent=2)

def show_tasks(tasks):
	if not tasks:
		print('No tasks found.')
		return
	for idx, task in enumerate(tasks, 1):
		status = '✓' if task['done'] else '✗'
		print(f"{idx}. [{status}] {task['title']}")

def add_task(tasks):
	title = input('Enter task: ').strip()
	if title:
		tasks.append({'title': title, 'done': False})
		save_tasks(tasks)
		print('Task added.')

def mark_task(tasks):
	show_tasks(tasks)
	try:
		idx = int(input('Enter task number to mark as done/undone: ')) - 1
		if 0 <= idx < len(tasks):
			tasks[idx]['done'] = not tasks[idx]['done']
			save_tasks(tasks)
			print('Task updated.')
		else:
			print('Invalid task number.')
	except ValueError:
		print('Please enter a valid number.')

def delete_task(tasks):
	show_tasks(tasks)
	try:
		idx = int(input('Enter task number to delete: ')) - 1
		if 0 <= idx < len(tasks):
			tasks.pop(idx)
			save_tasks(tasks)
			print('Task deleted.')
		else:
			print('Invalid task number.')
	except ValueError:
		print('Please enter a valid number.')

def main():
	while True:
		print('\nTo-Do List Application')
		print('1. View tasks')
		print('2. Add task')
		print('3. Mark task as done/undone')
		print('4. Delete task')
		print('5. Exit')
		choice = input('Choose an option: ')
		tasks = load_tasks()
		if choice == '1':
			show_tasks(tasks)
		elif choice == '2':
			add_task(tasks)
		elif choice == '3':
			mark_task(tasks)
		elif choice == '4':
			delete_task(tasks)
		elif choice == '5':
			print('Goodbye!')
			break
		else:
			print('Invalid choice. Please try again.')

if __name__ == '__main__':
	main()