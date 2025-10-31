tasks = []

while True:
    print("\n1.タスク追加\n2.タスク表示\n3.終了")
    choice = input("選択してください")

    if choice == "1":
        in_task = input("追加するタスクを入力してください：")
        tasks.append(in_task)
        with open("tasks.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(tasks))

        print("追加しました")

    elif choice == "2":
        with open("tasks.txt", "r", encoding="utf-8") as f:
            tasks = f.read().splitlines()
        print(tasks)

    elif choice == "3":
        break

    else:
        print("無効な数字です")
