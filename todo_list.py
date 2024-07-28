def main():
    task = []
    
    while True:
        print("\n === To Do List ===")
        print("1 Add Task")
        print("2 Delete Task")
        print("3 Show task as completed")
        print("4 Exit")
        
        choice = int(input("Enter your Choice  "))
        
        if choice==1:
            print()
            tasks_=int(input("How many task do you want to add  "))
            
            for i in range(tasks_):
                tasks=input("Enter Your Task")
                task.append({"tasks" : tasks, "done": False})
                print("task successfully added ")
        elif choice ==2:
            print("\n")
            for index, tasks in enumerate(task):
                status = "Done" if tasks["Done"] else["Not Done"]
                print(f"{index + 1}.{task['task']} - {status}")
                
        elif choice == 3:
            task_index = int(input("enter the task mark as done: ")) - 1
            if 0 <= task_index < len(task):
                task[task_index]["done"] = True
                print("mark as done")
            else:
                print("Invalid task number")
                
        elif choice == 4:
            print("Exiting the to do list")
            break
        else:
            print("Invalid choice.Please Try again later")
            
if __name__ == "__main__":
    main()