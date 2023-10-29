def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "ValueError: Give me name and phone please."
        except KeyError:
            return "Key Error: Contact not found."
        except IndexError:
            return "IndexError: An error occurred. Please check your input."
    return inner


@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact changed."


@input_error
def get_contact(args, contacts):
    if len(args) != 1:
        raise ValueError
    name = args[0].lower()
    if name not in contacts:
        raise KeyError
    return contacts[next(contact for contact in
                         contacts if contact.lower() == name)]


@input_error
def get_all(contacts):
    if not contacts:
        raise IndexError
    contact_list = "\n".join(
        [f"{name} : {phone}" for name, phone in contacts.items()])
    return contact_list


def main():
    contacts = {}
    help_message = [
        "Welcome to the assistant bot!",
        "Commands:",
        " - 'hello' or 'start' - to start the conversation",
        " - 'add -> (username phone)' - to add a contact",
        " - 'change -> (username phone)' - to change a contact's phone number",
        " - 'phone -> (username)' - to get a contact's phone number",
        " - 'all' - to get all contacts",
        " - 'close' or 'exit' - to exit the bot"
    ]
    print("\n".join(help_message))

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "start"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print("Invalid command format or unknown command.")



if __name__ == "__main__":
    main()
