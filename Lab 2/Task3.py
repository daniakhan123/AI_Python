import random

class BackupTask:
    def __init__(self, id):
        self.id = id
        self.status = random.choice(["Completed", "Failed"])

    def __str__(self):
        return f"Backup Task {self.id}: {self.status}"

class BackupManager:
    def __init__(self):
        self.tasks = [BackupTask(i) for i in range(1, 10)]  # 3x3 grid

    def display_tasks(self, message):
        print(message)
        grid = []
        for i in range(0, 9, 3):
            row = [self.tasks[i].status[0] for i in range(i, i + 3)]
            grid.append(" | ".join(row))
        print("\n".join(grid))
        print("----------------------------")

    def retry_failed_backups(self):
        for task in self.tasks:
            if task.status == "Failed":
                print(f"Retrying Backup Task {task.id}")
                task.status = "Completed"

if __name__ == "__main__":
    manager = BackupManager()
    manager.display_tasks("Initial Backup Task Statuses:")
    
    manager.retry_failed_backups()
    
    manager.display_tasks("Final Backup Task Statuses:")
