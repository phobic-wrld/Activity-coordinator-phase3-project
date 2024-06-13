from database.connection import get_db_connection

class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description

    @staticmethod
    def create(description, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (description, user_id) VALUES (?, ?)", (description, user_id))
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        return Task(task_id, description)

    @staticmethod
    def get_tasks_by_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, description FROM tasks WHERE user_id = ?", (user_id,))
        tasks = [Task(id, description) for id, description in cursor.fetchall()]
        conn.close()
        return tasks

    @staticmethod
    def delete_task(task_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
