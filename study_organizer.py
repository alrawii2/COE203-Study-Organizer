# COE203 – Project 1: Study Organizer
# Weeks 1–3 (B1–B2). Uses: variables, conditionals, lists, loops, file I/O, functions.
# Simple student-style implementation.

DATA_FILE = "tasks.txt"   # subject|title|due|status

def load_tasks():
    tasks = []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 4:
                    # bad line in file, skip it
                    continue
                tasks.append({
                    "subject": parts[0],
                    "title": parts[1],
                    "due": parts[2],
                    "status": parts[3]
                })
    except FileNotFoundError:
        # file will be created on save
        pass
    return tasks

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for t in tasks:
            row = f'{t["subject"]}|{t["title"]}|{t["due"]}|{t["status"]}\n'
            f.write(row)

def print_menu():
    print("\n=== Study Organizer ===")
    print("1) add task")
    print("2) list tasks")
    print("3) mark as done")
    print("4) delete task")
    print("5) save & exit")

def add_task(tasks):
    subject = input("subject: ").strip()
    title = input("title: ").strip()
    due = input("due (yyyy-mm-dd or none): ").strip() or "none"
    tasks.append({"subject": subject, "title": title, "due": due, "status": "pending"})
    print("added.")

def list_tasks(tasks):
    if not tasks:
        print("no tasks yet.")
        return
    print("\n#  subject         title                   due         status")
    print("--  --------------  ---------------------  -----------  ------")
    for i, t in enumerate(tasks, start=1):
        s = t["subject"][:14].ljust(14)
        ti = t["title"][:21].ljust(21)
        d = t["due"][:11].ljust(11)
        st = t["status"]
        print(f"{i:>2}  {s}  {ti}  {d}  {st}")

def pick_index(tasks, msg):
    if not tasks:
        print("nothing to choose.")
        return None
    try:
        n = int(input(msg))
        if 1 <= n <= len(tasks):
            return n - 1
        print("out of range.")
    except ValueError:
        print("please type a number.")
    return None

def mark_done(tasks):
    list_tasks(tasks)
    idx = pick_index(tasks, "which # is done? ")
    if idx is None:
        return
    tasks[idx]["status"] = "done"
    print("updated.")

def delete_task(tasks):
    list_tasks(tasks)
    idx = pick_index(tasks, "delete which #? ")
    if idx is None:
        return
    title = tasks[idx]["title"]
    tasks.pop(idx)
    print(f"deleted: {title}")

def main():
    tasks = load_tasks()
    while True:
        print_menu()
        choice = input("choose (1-5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("saved. bye.")
            break
        else:
            print("try 1-5.")

if __name__ == "__main__":
    main()
