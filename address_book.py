from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Phone number should contain 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            phone_obj = Phone(phone)
            self.phones.append(phone_obj)
        except ValueError as e:
            return str(e)

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return f"Phone {phone} removed."
        return f"Phone {phone} not found."

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return f"Phone {old_phone} changed to {new_phone}."
        return f"Phone {old_phone} not found."

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value
        return f"Phone {phone} not found."

    def __str__(self):
        return (
            f"Contact name: {self.name.value}, "
            f"phones: {'; '.join(p.value for p in self.phones)}"
        )


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        if name in self.data:
            return self.data[name]
        return f"Record {name} not found."

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Record {name} deleted."
        return f"Record {name} not found."


def main():
    book = AddressBook()

    id_record = Record("ID")
    id_record.add_phone("1234567890")
    id_record.add_phone("5555555555")

    book.add_record(id_record)

    kat_record = Record("Kat")
    kat_record.add_phone("9876543210")
    book.add_record(kat_record)

    print("All records in the address book:")
    for name, record in book.data.items():
        print(record)

    id = book.find("ID")
    print("Editing phone for ID:")
    print(id.edit_phone("1234567890", "1112223333"))
    print(id)

    found_phone = id.find_phone("5555555555")
    print(f"Found phone in ID's record: {found_phone}")

    print("Deleting Kat record:")
    print(book.delete("Kat"))


if __name__ == "__main__":
    main()
