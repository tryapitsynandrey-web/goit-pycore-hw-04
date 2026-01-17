"""Домашнє завдання 4: Консольний асистент-бот.

Бот підтримує базові команди для роботи з контактами:
- додавання
- оновлення
- пошук
- перегляд усіх контактів
- довідку (help)
"""

from __future__ import annotations

import random
from typing import Dict, List, Tuple


# =========================
# ТЕКСТОВІ ПОВІДОМЛЕННЯ (UX)
# =========================

WELCOME_MESSAGES = (
    (
        "Welcome to the assistant bot!\n"
        "This bot helps you manage your contacts.\n"
        "Type 'help' to see the list of available commands."
    ),
    (
        "Welcome!\n"
        "You are now using the assistant bot for contact management.\n"
        "Enter 'help' to get an overview of all supported commands."
    ),
    (
        "Hello and welcome to the assistant bot.\n"
        "You can add, update, and view contacts here.\n"
        "Use the 'help' command to get started."
    ),
    (
        "Welcome to the assistant bot.\n"
        "This tool allows you to work with contacts via simple commands.\n"
        "Type 'help' to learn how to use the bot."
    ),
    (
        "Welcome!\n"
        "The assistant bot is ready to help you manage your contact list.\n"
        "For instructions, type 'help'."
    ),
    (
        "Welcome to the assistant bot.\n"
        "You can manage contacts quickly and easily from here.\n"
        "Type 'help' to see all available options."
    ),
)

GOODBYE_MESSAGES = (
    "Good bye! Thank you for using the assistant bot.",
    "Good bye! See you next time.",
    "Good bye! Have a great day.",
    "Good bye! Your contacts are safe.",
    "Good bye! Glad I could help.",
    "Good bye! Come back anytime you need assistance.",
    "Good bye! Session ended successfully.",
    "Good bye! All changes have been saved.",
    "Good bye! Wishing you a productive day.",
    "Good bye! Thanks for choosing the assistant bot.",
    "Good bye! Looking forward to helping you again.",
    "Good bye! Take care and see you soon.",
)

HELP_MESSAGE = (
    "Commands (syntax -> description)\n"
    "--------------------------------\n"
    "hello                  -> Prints: How can I help you?\n"
    "add <name> <phone>     -> Add a new contact\n"
    "change <name> <phone>  -> Update phone for an existing contact\n"
    "phone <name>           -> Show phone for the specified contact\n"
    "all                    -> Show all saved contacts\n"
    "help                   -> Show this help message\n"
    "close | exit           -> Exit the assistant bot\n"
)

EMPTY_INPUT_MESSAGES = (
    "No command entered.\nPlease type a command or use 'help' to see available options.",
    "Empty input received.\nEnter a command or type 'help' for guidance.",
    "You did not enter any command.\nUse 'help' to view available commands.",
    "Nothing was entered.\nPlease provide a command to continue.",
)

INVALID_COMMAND_MESSAGES = (
    "Invalid command.\nType 'help' to see the list of supported commands.",
    "Command not recognized.\nUse 'help' to view all available commands.",
    "Unknown command entered.\nPlease check the spelling or type 'help'.",
    "This command is not supported.\nType 'help' for the full command list.",
)

CONTACT_NOT_FOUND_MESSAGES = (
    "Contact not found.\nPlease check the name or add a new contact.",
    "No contact with this name was found.\nYou may want to add it first.",
    "The requested contact does not exist.\nUse 'add' to create a new contact.",
    "Contact is missing.\nVerify the name or create a new entry.",
)

CONTACT_ADDED_MESSAGES = (
    "Contact added successfully.",
    "The contact has been added.",
    "New contact saved successfully.",
    "Contact was added to your list.",
)

CONTACT_UPDATED_MESSAGES = (
    "Contact updated successfully.",
    "The contact information has been updated.",
    "Contact details were updated.",
    "Changes to the contact have been saved.",
)

NO_CONTACTS_MESSAGES = (
    "No contacts saved yet.\nUse the 'add' command to create a new contact.",
    "Your contact list is empty.\nAdd a contact to get started.",
    "There are no saved contacts.\nUse 'add' to create one.",
    "No contacts found.\nStart by adding a new contact.",
)


# =========================
# ДОПОМІЖНІ ФУНКЦІЇ
# =========================

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """Розбиває введення користувача на команду та аргументи."""

    cleaned = user_input.strip()
    if not cleaned:
        return "", []

    parts = cleaned.split()
    return parts[0].lower(), parts[1:]


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Додає новий контакт."""

    if len(args) != 2:
        return random.choice(INVALID_COMMAND_MESSAGES)

    name, phone = args
    contacts[name] = phone
    return random.choice(CONTACT_ADDED_MESSAGES)


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """Оновлює номер телефону існуючого контакту."""

    if len(args) != 2:
        return random.choice(INVALID_COMMAND_MESSAGES)

    name, phone = args
    if name not in contacts:
        return random.choice(CONTACT_NOT_FOUND_MESSAGES)

    contacts[name] = phone
    return random.choice(CONTACT_UPDATED_MESSAGES)


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """Повертає номер телефону для заданого контакту."""

    if len(args) != 1:
        return random.choice(INVALID_COMMAND_MESSAGES)

    name = args[0]
    if name not in contacts:
        return random.choice(CONTACT_NOT_FOUND_MESSAGES)

    return contacts[name]


def show_all(contacts: Dict[str, str]) -> str:
    """Повертає всі збережені контакти."""

    if not contacts:
        return random.choice(NO_CONTACTS_MESSAGES)

    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


# =========================
# ГОЛОВНИЙ ЦИКЛ
# =========================

def main() -> None:
    """Точка входу для запуску асистент-бота."""

    contacts: Dict[str, str] = {}

    command_handlers = {
        "hello": lambda _args: "How can I help you?",
        "add": lambda args: add_contact(args, contacts),
        "change": lambda args: change_contact(args, contacts),
        "phone": lambda args: show_phone(args, contacts),
        "all": lambda _args: show_all(contacts),
        "help": lambda _args: HELP_MESSAGE,
    }

    print(random.choice(WELCOME_MESSAGES))

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if not command:
            print(random.choice(EMPTY_INPUT_MESSAGES))
            continue

        if command in ("close", "exit"):
            print(random.choice(GOODBYE_MESSAGES))
            break

        handler = command_handlers.get(command)
        if handler is None:
            print(random.choice(INVALID_COMMAND_MESSAGES))
            continue

        print(handler(args))


if __name__ == "__main__":
    main()