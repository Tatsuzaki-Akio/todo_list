import tkinter as tk

root = tk.Tk()
root.title("Todoリスト")
root.geometry("300x200")
root.resizable(True, True)


label = tk.Label(root, text="ToDoリストへようこそ")
label.pack()

root.mainloop()


def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(tasks))


try:
    with open("tasks.txt", "r", encoding="utf-8") as f:
        tasks = f.read().splitlines()
except FileNotFoundError:
    tasks = []


while True:
    print("\n1.タスク追加\n2.タスク表示\n3.タスクを削除\n4.終了")
    choice = input("選択してください")

    if choice == "1":
        in_task = input("追加するタスクを入力してください：")
        tasks.append(in_task)
        save_tasks()

        print("追加しました")

    elif choice == "2":
        if not tasks:
            print("現在のタスクはありません")
        else:
            print("現在のタスク一覧")
            for i, l in enumerate(tasks, 1):
                print(f"{i}:{l}")

    elif choice == "3":
        if not tasks:
            print("削除するタスクはありません")
        else:
            for i, l in enumerate(tasks, 1):
                print(f"{i}:{l}")

            num = input("削除するタスク番号を記入してください")
            if 1 <= int(num) <= len(tasks):
                del tasks[int(num) - 1]
                save_tasks()
                print("削除しました")

            else:
                print("該当番号はありません")

    elif choice == "4":
        break

    else:
        print("無効な数字です")
