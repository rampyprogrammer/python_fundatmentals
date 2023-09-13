from abc import ABC,abstractmethod
# creating abstract class with abstractmethod
class Calci(ABC):
    @abstractmethod
    def sum(self,*arg):
        pass
    
    @abstractmethod
    def product(self,*arg):
        pass
    
    