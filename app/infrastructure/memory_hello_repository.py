from app.domain.hello_repository import HelloRepository


class MemoryHelloRepository(HelloRepository):
    def __init__(self):
        self._memory = {"hello": "fabien"}

    def get(self) -> dict:
        return self._memory

    def save(self, hello: dict) -> dict:
        self._memory["hello"] = hello["hello"]
        return self._memory
