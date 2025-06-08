from datetime import datetime

class Item:
    def __init__(self, name, checked = False):
        self.name = name
        self.checked = checked

    def toDict(self):
        return {"name": self.name, "checked": self.checked}

    @staticmethod
    def fromDict(data):
        return Item(data["name"], data["checked"])

class List:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add(self, item):
        if not isinstance(item, Item):
            raise TypeError("That isn't a valid item")
        self.items.append(item)

    def remove(self, itemID):
        self.items.pop(itemID)
    
    def list(self):
        print(self.name)
        print("----------")
        for index, item in enumerate(self.items):
            icon = "[ ✓ ]" if item.checked else "[   ]"
            print(str(index) + ".", icon, item.name)
        print("----------")

    def toDict(self):
        return {
            "name": self.name,
            "items": [item.toDict() for item in self.items]
        }

    @staticmethod
    def fromDict(data):
        lst = List(data["name"])
        lst.items = [Item.fromDict(item_data) for item_data in data["items"]]
        return lst

class ListManager:
    def __init__(self):
        self.lists = []

    def create(self, name):
        self.lists.append(List(name))
        return len(self.lists)-1

    def delete(self, listID):
        self.lists.pop(listID)

    def get(self, listID):
        return self.lists[listID]

    def list(self):
        print("Lists")
        print("----------")
        for index, list in enumerate(self.lists):
            print(str(index) + ". " + list.name)
        print("----------")

    def toDict(self):
        return {
            "saveDate": str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
            "lists": [lst.toDict() for lst in self.lists]
        }

    @staticmethod
    def fromDict(data):
        manager = ListManager()
        manager.lists = [List.fromDict(lst_data) for lst_data in data["lists"]]
        return manager