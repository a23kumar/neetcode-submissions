from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mappings = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.mappings:
            return -1
        self.mappings.move_to_end(key)
        return self.mappings[key]

    def put(self, key: int, value: int) -> None:
        # CASES:
        # Default case: There is capacity
        # Edge cases: Capacity is full
        if key in self.mappings:
            self.mappings.move_to_end(key)
        self.mappings[key] = value
        if len(self.mappings) > self.capacity:
            self.mappings.popitem(last=False)
        

