from database.connection import get_db_connection
from models.task import Task

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def create(name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (?)", (name,))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return User(user_id, name)

    @staticmethod
    def get_user_by_name(name):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM users WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(row[0], row[1])
        else:
            return None

    def add_task(self, task_description):
        task = Task.create(task_description, self.id)
        print(f"Task '{task.description}' added to {self.name}'s list.")

    def list_tasks(self):
        tasks = Task.get_tasks_by_user(self.id)
        if not tasks:
            print(f"{self.name} has no tasks currently.")
        else:
            print(f"{self.name}'s Current Tasks:")
            for index, task in enumerate(tasks):
                print(f"Task #{index}. {task}")

    def delete_task(self):
        tasks = Task.get_tasks_by_user(self.id)
        if not tasks:
            print(f"{self.name} has no tasks to delete.")
            return

        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task.description}")

        try:
            task_to_delete = int(input("Enter the # to delete: "))
            if 0 <= task_to_delete < len(tasks):
                task = tasks[task_to_delete]
                Task.delete_task(task.id)
                print(f"Task '{task.description}' has been removed from {self.name}'s list.")
            else:
                print(f"Task #{task_to_delete} was not found.")
        except ValueError:
            print("Invalid input.")
