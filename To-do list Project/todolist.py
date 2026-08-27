import time
import os

task_list = []

def to_do_list_app():
    os.system('clear')
    print("To-Do List App")
    while True:
        os.system('clear')
        print("---------------")
        print("1. show tasks")
        print("2. add task")
        print("3. remove task")
        print("4. exit program")
        print("---------------")
        choice = input("choose an option: ")
        ("--------")
        if choice == "4":
            os.system('clear')
            print("Good bye")
            time.sleep(1.5)
            break
        elif choice == "1":
            if len(task_list) == 0:
                os.system('clear')
                print("You dont have any tasks")
                time.sleep(1.5)
                os.system('clear')
                continue
            else:
                os.system('clear')
                print("There is your list")
                for task in task_list:
                    print(f"-- {task}")
                    time.sleep(1.5)
                    os.system('clear')
                    continue
        elif choice == "2":
            os.system('clear')
            add_task = input("enter task name: ").lower()
            if add_task in task_list:
                os.system('clear')
                print(f"'{add_task}' is already found in the todo list")
                time.sleep(1.5)
                os.system('clear')
                continue

            else:
                task_list.append(add_task)
                os.system('clear')
                print(f"'{add_task}' has been added to the todo list")
                time.sleep(1.5)
                os.system('clear')
                continue
        elif choice == "3":
            os.system('clear')
            
            if len(task_list) == 0:
                os.system('clear')
                print("your list is already empty")
                time.sleep(1.5)
                os.system('clear')
                continue
            else:
                os.system('clear')
                remove_task = input("enter the task name: ").lower()
                if remove_task not in task_list:
                 os.system('clear')
                 print(f"'{remove_task}' is not in the todo list")
                 time.sleep(1.5)
                 os.system('clear')
                 continue
                else:
                 remove_task = input("enter the task name: ").lower()
                 task_list.remove(remove_task)
                 os.system('clear')
                 print(f"'{remove_task}' has been removed from the todo list")
                 time.sleep(1.5)
                 os.system('clear')
                 continue
        else:
            os.system('clear')
            print("invaild option")
            time.sleep(1.5)
            os.system('clear')
            continue            


to_do_list_app()