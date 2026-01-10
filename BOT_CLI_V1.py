EMPTY_INPUT_MESSAGE = "OoOoOoOops You forgot to press a couple of keys on the keyboard."
INVALID_COMMAND_MESSAGE = "Invalid command."


def parse_input(user_input: str):
    user_input = user_input.strip()

    if not user_input:
        return "", []

    parts = user_input.split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def add_contact(args, contacts: dict) -> str:
    if len(args) != 2:
        return INVALID_COMMAND_MESSAGE

    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts: dict) -> str:
    if len(args) != 2:
        return INVALID_COMMAND_MESSAGE

    name, new_phone = args
    if name not in contacts:
        return "Contact not found."

    contacts[name] = new_phone
    return "Contact updated."


def show_phone(args, contacts: dict) -> str:
    if len(args) != 1:
        return INVALID_COMMAND_MESSAGE

    name = args[0]
    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts saved."

    lines = []
    for name in sorted(contacts):
        lines.append(f"{name}: {contacts[name]}")
    return "\n".join(lines)


def show_help() -> str:
    return (
        "Available commands:\n"
        "hello\n"
        "  Prints: How can I help you?\n\n"
        "add <username> <phone>\n"
        "  Adds a new contact with name and phone number.\n\n"
        "change <username> <phone>\n"
        "  Updates the phone number for an existing contact.\n\n"
        "phone <username>\n"
        "  Shows the phone number for the given contact.\n\n"
        "all\n"
        "  Shows all saved contacts.\n\n"
        "close / exit\n"
        "  Exits the assistant bot."
    )


def main() -> None:
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        command, args = parse_input(user_input)

        if command == "":
            print(EMPTY_INPUT_MESSAGE)
            continue

        if command in ("close", "exit"):
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "help":
            print(show_help())

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print(INVALID_COMMAND_MESSAGE)


if __name__ == "__main__":
    main()