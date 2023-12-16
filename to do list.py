class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            print('\n--- To-Do List ---')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')
            print('-------------------\n')

    def complete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{completed_task}" completed.')
        else:
            print('Invalid task index.')

    def clear_tasks(self):
        self.tasks = []
        print('All tasks cleared.')

def main():
    todo_list = TodoList()

    while True:
        print('\nOptions:')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Complete Task')
        print('4. Clear All Tasks')
        print('5. Exit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input('Enter the task index to complete: '))
            todo_list.complete_task(task_index)
        elif choice == '4':
            todo_list.clear_tasks()
        elif choice == '5':
            print('Exiting the to-do list application. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if __name__ == "__main__":
    main()
