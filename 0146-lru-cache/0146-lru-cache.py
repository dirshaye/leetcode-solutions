from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity
        self.least = deque()

    def get(self, key: int) -> int:
        if key in self.lru:
            # Remove old usage if it exists
            if key in self.least:
                self.least.remove(key)
            # Add to the end (most recently used)
            self.least.append(key)
            return self.lru[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            # Remove old usage before re-adding
            self.least.remove(key)
        elif len(self.lru) >= self.capacity:
            # Remove the least recently used key
            lru_key = self.least.popleft()
            del self.lru[lru_key]

        # Add or update the key
        self.lru[key] = value
        self.least.append(key)
