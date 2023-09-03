from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Phone(Field):
    pass


class Name(Field):
    pass


class Record:
    def __init__(self, name: str, phones: list, emails: list):
        self.name = Name(name)
        self.phones = [Phone(phone) for phone in phones]
        self.emails = emails

    def add_phone(self, phone):
        phone_number = Phone(phone)
        if phone_number not in self.phones:
            self.phones.append(phone_number)

    def find_phone(self, value):
        for phone in self.phones:
            if phone.value == value:
                return phone
        return None

    def delete_phone(self, phone):
        self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        index = self.phones.index(old_phone)
        self.phones[index] = Phone(new_phone)


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find_record(self, value):
        return self.data.get(value)

    def find_records_by_phone(self, phone):
        found_records = []
        for record in self.data.values():
            for record_phone in record.phones:
                if record_phone.value == phone:
                    found_records.append(record)
                    break
        return found_records


def main():
    address_book = AddressBook()

    while True:
        user_input = input(">>> ").strip()
        if user_input.lower() in ["good bye", "close", "exit"]:
            print("Good bye!")
            break

        command, *args = user_input.split()

        if command == "add":
            if len(args) < 2:
                print("Please provide name and phone number.")
                continue
            name, phone = args[0], args[1]
            if name in address_book:
                print(f"Contact {name} already exists.")
            else:
                record = Record(name, [phone], [])
                address_book.add_record(record)
                print(f"Contact {name} added with phone {phone}.")
        elif command == "change":
            if len(args) < 2:
                print("Please provide name and phone number.")
                continue
            name, phone = args[0], args[1]
            if name not in address_book:
                print(f"Contact {name} not found.")
            else:
                record = address_book[name]
                record.edit_phone(record.phones[0], phone)
                print(f"Contact {name} updated with new phone {phone}.")
        elif command == "phone":
            if not args:
                print("Please provide a name.")
                continue
            name = args[0]
            if name not in address_book:
                print(f"Contact {name} not found.")
            else:
                record = address_book[name]
                print(f"The phone number for {name} is {record.phones[0].value}.")
        elif command == "show":
            if len(args) > 0 and args[0] == "all":
                if not address_book:
                    print("No contacts found.")
                else:
                    print("Contacts:")
                    for name, record in address_book.items():
                        print(f"{name}: {record.phones[0].value}")
            else:
                print("Unknown command")
        else:
            print("Unknown command")


if __name__ == "__main__":
    main()
