from abc import abstractmethod


class HelloRepository:

    @abstractmethod
    def get(self):
        raise NotImplementedError

    @abstractmethod
    def save(self, hello: dict):
        raise NotImplementedError
