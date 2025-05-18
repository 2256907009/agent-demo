from typing import List

class Memory:
    def __init__(self):
        self.history: List[str] = []

    def add(self, record: str):
        self.history.append(record)

    def search(self, keyword: str) -> List[str]:
        return [record for record in self.history if keyword in record]

    def __len__(self):
        return len(self.history)