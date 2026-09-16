import uuid

class Solution:
    def __init__(self):
        self.mappings = dict()

    def encode(self, strs: List[str]) -> str:
        key = str(uuid.uuid1())
        self.mappings[key] = strs
        return key

    def decode(self, s: str) -> List[str]:
        return self.mappings[s]