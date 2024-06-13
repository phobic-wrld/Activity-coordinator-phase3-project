from database.setup import create_tables
from models.user import User
from models.task import Task

def main():
    create_tables()
    print("Welcome to the to do list app :)")
    user_name = input("Enter your name: ")
    user = User.get_user_by_name(user_name)
    if not user:
        user = User.create(user_name)

    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_description = input("Please enter a task: ")
            user.add_task(task_description)
        elif choice == "2":
            user.delete_task()
        elif choice == "3":
            user.list_tasks()
        elif choice == "4":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye")

if __name__ == "__main__":
    main()
