from abc import ABC, abstractmethod
class Clothing(ABC):
    @abstractmethod
    def cloth_consumption(self):
        pass

class Coat(Clothing):
    def __init__(self, V):
        self.V = V

    @property
    def cloth_consumption(self):
        result = self.V / 6.5 + 0.5
        return f'расход ткани составит {round(result,2)} метров'

class Suit(Clothing):
    def __init__(self, H):
        self.H = H

    @property
    def cloth_consumption(self):
        result = 2 * self.H + 0.3
        return f'расход ткани составит {result} метров'

coat = Coat(46)
suit = Suit(1.74)
print(coat.cloth_consumption)
print(suit.cloth_consumption)
