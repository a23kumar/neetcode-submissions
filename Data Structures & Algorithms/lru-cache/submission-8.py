
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.hm:
            res = self.hm[key]
            self.hm.move_to_end(key)
            return res
        return -1
                

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.hm[key] = value
            self.hm.move_to_end(key)
        else:
            if len(self.hm) == self.capacity:
                self.hm.popitem(last=False)
            self.hm[key] = value

