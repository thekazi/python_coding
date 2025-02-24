def todo_list():
    tasks = []

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Choose an Option: ")

        if choice == '1' :
            task = input("Enter Task: ")
            tasks.append(task)
        elif choice == '2' :
            print("\n Tasks: ")
            for i, task in enumerate(tasks, 1):
                print(f"{1}, {task}")
        elif choice == '3' :
            task_num = ini(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                tasks.pop(task_num -1)
            else:
                print("Invalid Task Number!")
        elif choice == '4' :
            break
        else:
            print("Invalid Choice!")

todo_list()