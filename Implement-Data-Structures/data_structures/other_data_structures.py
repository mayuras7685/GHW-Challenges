# other_data_structures.py
class Set:
    def __init__(self):
        self.items = []

    def add(self, item):
        if item not in self.items:
            self.items.append(item)

    def remove(self, item):
        if item in self.items:
            self.items.remove(item)

    def contains(self, item):
        return item in self.items

    def size(self):
        return len(self.items)

class Dictionary:
    def __init__(self):
        self.items = {}

    def add(self, key, value):
        self.items[key] = value

    def remove(self, key):
        if key in self.items:
            del self.items[key]

    def get(self, key):
        return self.items.get(key)

    def contains_key(self, key):
        return key in self.items

    def size(self):
        return len(self.items)
