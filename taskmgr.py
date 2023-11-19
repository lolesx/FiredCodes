import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists('tasks.json'):
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def display_tasks(self):
        if not self.tasks:
            print("Aucune tâche enregistrée.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task['title']} - {task['due_date']} - {'Fait' if task['done'] else 'À faire'}")

    def add_task(self, title, due_date):
        task = {'title': title, 'due_date': due_date, 'done': False}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Tâche ajoutée : {title}")

    def mark_as_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['done'] = True
            self.save_tasks()
            print(f"Tâche marquée comme terminée : {self.tasks[task_index - 1]['title']}")
        else:
            print("Index de tâche invalide.")

def main():
    manager = TaskManager()

    while True:
        print("\nGestionnaire de tâches:")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Marquer une tâche comme terminée")
        print("4. Quitter")

        choice = input("Choisissez une option (1/2/3/4): ")

        if choice == '1':
            manager.display_tasks()
        elif choice == '2':
            title = input("Entrez le titre de la tâche : ")
            due_date = input("Entrez la date d'échéance (YYYY-MM-DD) : ")
            manager.add_task(title, due_date)
        elif choice == '3':
            manager.display_tasks()
            task_index = int(input("Entrez l'index de la tâche à marquer comme terminée : "))
            manager.mark_as_done(task_index)
        elif choice == '4':
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()
