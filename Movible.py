from abc import ABC, abstractmethod

class Movible (ABC):
    @abstractmethod
    def mover(self) -> str:
        pass