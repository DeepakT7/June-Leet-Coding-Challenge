class RandomizedSet:

    def __init__(self):

        self.items = set()

    def insert(self, val: int) -> bool:
        
        if val in self.items:
            return False
        self.items.add(val)
        return True

    def remove(self, val: int) -> bool:
        
        if val not in self.items:
            return False
        self.items.remove(val)
        return True

    def getRandom(self) -> int:
        from random import randint
        return list(self.items)[randint(0, len(self.items) - 1)]