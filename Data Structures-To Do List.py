def main():
    tasks = []

    while True:
        print("\n-------To Do List--------------")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as done")
        print("4. Exit")

        choice = (input("Enter Your Choice"))

        if choice == '1':
            print()
            n_tasks = int(input("How many tasks you want to add "))

            for i in range(n_tasks):
                task = str(input("Enter your task: "))
                tasks.append({"task": task, "done": False})
                print("Task Added!")
        elif choice == '2':
            print("\n------Tasks-----------")
            for index, task in enumerate(tasks):
                status = "done" if task["done"] else "Not done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter The Task no mark  as done:"))
            if 0 <= task_index < len(tasks):
                tasks = tasks[tasks_index]["done"] = "True"
                print("Task Mark as Done")
            else:
                print("INVALID TASK NUMBER!")
        elif choice == 4 :
            print("Exiting the TO DO LIST")
            break
        else:
            print("IVALID CHOICE. PLEASE TRY AGAIN")

if __name__  == "__main__":
    main()