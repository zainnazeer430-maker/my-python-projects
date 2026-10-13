import os

FILE = "tasks.txt"

def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return [line.strip() for line in f if line.strip()]

def save(tasks):
    with open(FILE, "w") as f:
        for t in tasks:
            f.write(t + "\n")

tasks = load()

while True:
    print("\n1) Show tasks  2) Add task  3) Delete task  4) Quit")
    choice = input("Choose: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        for i, t in enumerate(tasks, 1):
            print(i, "-", t)
    elif choice == "2":
        task = input("New task: ").strip()
        if task:
            tasks.append(task)
            save(tasks)
            print("Added.")
    elif choice == "3":
        num = input("Task number to delete: ")
        if num.isdigit() and 1 <= int(num) <= len(tasks):
            removed = tasks.pop(int(num) - 1)
            save(tasks)
            print("Deleted:", removed)
        else:
            print("That number doesn't exist.")
    elif choice == "4":
        print("Bye!")
        break
    else:
        print("Please choose 1, 2, 3 or 4.")
