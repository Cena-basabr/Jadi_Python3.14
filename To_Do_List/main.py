import csv


class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"نام: {self.name} | توضیحات: {self.description} | اولویت: {self.priority}"


class ToDoList:
    def __init__(self, filename="tasks.csv"):
        self.tasks = []
        self.filename = filename
        self.load_from_csv()

    def save_to_csv(self):
        with open(self.filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'description', 'priority'])
            for task in self.tasks:
                writer.writerow([task.name, task.description, task.priority])
        print(f"لیست کارها به طور خودکار ذخیره شد.")

    def load_from_csv(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                header = next(reader)
                self.tasks.clear()
                for row in reader:
                    task = Task(name=row[0], description=row[1], priority=row[2])
                    self.tasks.append(task)
            print(f"کارها با موفقیت از فایل '{self.filename}' بارگذاری شدند.")
        except FileNotFoundError:
            print(f"فایل '{self.filename}' یافت نشد. یک لیست جدید ایجاد می‌شود.")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"کار '{task.name}' با موفقیت اضافه شد.")
        self.save_to_csv()

    def view_tasks(self):
        print("\n--- لیست کارها ---")
        if not self.tasks:
            print("لیست کارها خالی است.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        print("------------------\n")

    def delete_task(self):
        self.view_tasks()
        if not self.tasks:
            return

        try:
            task_number = int(input("شماره کاری که می‌خواهید حذف کنید را وارد کنید: "))

            if 1 <= task_number <= len(self.tasks):
                index_to_delete = task_number - 1
                removed_task = self.tasks.pop(index_to_delete)
                print(f"کار '{removed_task.name}' با موفقیت حذف شد.")
                self.save_to_csv()
            else:
                print("خطا: شماره وارد شده معتبر نیست.")
        except ValueError:
            print("خطا: لطفاً فقط عدد وارد کنید.")


def main():
    my_list = ToDoList()

    while True:
        print("\n--- منوی مدیریت کارها ---")
        print("1. اضافه کردن کار جدید")
        print("2. مشاهده لیست کارها")
        print("3. حذف کار")
        print("4. خروج")

        choice = input("لطفاً گزینه مورد نظر خود را انتخاب کنید: ")

        if choice == '1':
            name = input("نام کار را وارد کنید: ")
            description = input("توضیحات کار را وارد کنید: ")
            priority = input("اولویت کار را وارد کنید (بالا، متوسط، پایین): ")
            new_task = Task(name, description, priority)
            my_list.add_task(new_task)

        elif choice == '2':
            my_list.view_tasks()

        elif choice == '3':
            my_list.delete_task()

        elif choice == '4':
            print("از برنامه خارج شدید. خدانگهدار!")
            break

        else:
            print("خطا: انتخاب شما نامعتبر است. لطفاً دوباره تلاش کنید.")


if __name__ == "__main__":
    main()