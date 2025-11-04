import tkinter as tk
# import customtkinter as ctk


# リスト読み込み
try:
    with open("tasks.txt", "r", encoding="utf-8") as f:
        tasks = f.read().splitlines()
except FileNotFoundError:
    tasks = []


# タスク保存
def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(tasks))


# タスク追加
def in_tasks():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()


# タスク削除
def del_tasks():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        listbox.delete(index)
        save_tasks()


# GUI構成
root = tk.Tk()
root.title("Todoリスト")
root.geometry("300x200")
root.resizable(True, True)

# タスク入力欄
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

# ボタン追加
frame = tk.Frame(root)
frame.pack()
tk.Button(frame, text="追加", command=in_tasks).pack(side="left", padx=5)
tk.Button(frame, text="削除", command=del_tasks).pack(side="right", padx=5)

# リストボックス
listbox = tk.Listbox(root, width=40, height=100)
listbox.pack(pady=10)

for i in tasks:
    listbox.insert(tk.END, i)

root.mainloop()


# while True:
#     print("\n1.タスク追加\n2.タスク表示\n3.タスクを削除\n4.終了")
#     choice = input("選択してください")

#     if choice == "1":
#         in_task = input("追加するタスクを入力してください：")
#         tasks.append(in_task)
#         save_tasks()

#         print("追加しました")

#     elif choice == "2":
#         if not tasks:
#             print("現在のタスクはありません")
#         else:
#             print("現在のタスク一覧")
#             for i, l in enumerate(tasks, 1):
#                 print(f"{i}:{l}")

#     elif choice == "3":
#         if not tasks:
#             print("削除するタスクはありません")
#         else:
#             for i, l in enumerate(tasks, 1):
#                 print(f"{i}:{l}")

#             num = input("削除するタスク番号を記入してください")
#             if 1 <= int(num) <= len(tasks):
#                 del tasks[int(num) - 1]
#                 save_tasks()
#                 print("削除しました")

#             else:
#                 print("該当番号はありません")

#     elif choice == "4":
#         break

#     else:
#         print("無効な数字です")
