import csv

class Contact:
    def __init__(self, name, email, phonenumber):
        self.name = name
        self.email = email
        self.phonenumber = phonenumber

    def __str__(self):
        return f"نام: {self.name} | ایمیل: {self.email} | شماره تماس: {self.phonenumber}"

class ContactBook:
    def __init__(self, filename= "contact.csv"):
        self.filename = filename
        self.contacts = []
        self.load_from_csv()


    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"مخاطب '{contact.name}' با موفقیت اضافه شد.")
        self.save_to_csv()

    def remove_contact(self, contact):
        self.contacts.remove(contact)
        if not self.contacts:
            return

        try:
            contact_number = int(input("شماره مخاطبی که می‌خواهید حذف کنید را وارد کنید: "))
            if 1 <= contact_number <= len(self.contacts):
                removed_contact = self.contacts.pop(contact_number - 1)
                print(f"مخاطب '{removed_contact.name}' با موفقیت حذف شد.")
                self.save_to_csv()
            else:
                print("خطا: شماره وارد شده معتبر نیست.")
        except ValueError:
            print("خطا: لطفاً فقط عدد وارد کنید.")

def main():
    my_contacts = ContactBook()

    while True:
        print("\n--- منوی دفترچه تلفن ---")
        print("1. اضافه کردن مخاطب جدید")
        print("2. مشاهده لیست مخاطبین")
        print("3. حذف مخاطب")
        print("4. خروج")

        choice = input("لطفاً گزینه مورد نظر خود را انتخاب کنید: ")

        if choice == '1':
            name = input("نام مخاطب را وارد کنید: ")
            email = input("ایمیل مخاطب را وارد کنید: ")
            phonenumber = input("شماره تماس مخاطب را وارد کنید: ")
            new_contact = Contact(name, email, phonenumber)
            my_contacts.add_contact(new_contact)

        elif choice == '2':
            my_contacts.view_contacts()

        elif choice == '3':
            my_contacts.delete_contact()

        elif choice == '4':
            print("از برنامه خارج شدید. خدانگهدار!")
            break

        else:
            print("خطا: انتخاب شما نامعتبر است. لطفاً دوباره تلاش کنید.")


if __name__ == "__main__":
    main()