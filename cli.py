from core import *
import os
import readline
import json

FILE_NAME = "cmdlists_data"
DATA_FILE = FILE_NAME + ".json"
BACKUP_FILE = FILE_NAME + ".bak"

cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

def save_data(manager):
    try: os.rename(DATA_FILE, BACKUP_FILE)
    except Exception: pass
    with open(DATA_FILE, "w") as f:
        json.dump(manager.toDict(), f, indent=4)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return ListManager.fromDict(data)

def manage_list(list):
    while True:
        cls()
        list.list()
        print("\nCommands:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Check/Uncheck item")
        print("4. Go back")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            item_name = input("Enter item name: ")
            list.add(Item(item_name))
        elif choice == "2":
            itemID = int(input("Enter item ID to remove: "))
            list.remove(itemID)
        elif choice == "3":
            itemID = int(input("Enter item ID to check/uncheck: "))
            item: Item = list.items[itemID]
            item.checked = False if item.checked else True
        elif choice == "4":
            break

def main():
    listmngr = load_data()
    if not isinstance(listmngr, ListManager):
        listmngr = ListManager()
        listmngr.create("Example List")
        defaultList: List = listmngr.get(0)
        defaultList.add(Item("A basic example"))

    try:
        while True:
            cls()
            print("To-Do List Manager")
            print("==================")
            listmngr.list()
            print("==================")
            print("\nCommands:")
            print("1. Create new list")
            print("2. Delete a list")
            print("3. Open a list")
            print("4. Quit")

            choice = input("Choose an option: ").strip()

            if choice == "1":
                name = input("Enter list name: ")
                listmngr.create(name)
            elif choice == "2":
                listID = int(input("Enter list ID to delete: "))
                listmngr.delete(listID)
            elif choice == "3":
                listID = int(input("Enter list ID to open: "))
                selected_list: List = listmngr.get(listID)
                manage_list(selected_list)
            elif choice == "4":
                break
    except KeyboardInterrupt:
        pass

    save_data(listmngr)
    print("\nData saved!")

if __name__ == "__main__":
    main()