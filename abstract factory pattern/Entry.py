"""
Provide an Interface for creating families of related 
or dependent objects without specifying their concrete classes
"""

# import abc
class AbstractFactory(metaclass=abc.ABCMeta):
    """
    Declare an interface of operations that create abstract product objects 
    """
    @abc.abstractmethod
    def create_product_a(self):
        pass
    @abc.abstractmethod
    def create_product_b(self):
        pass
class ConcreteFactory1(AbstractFactory):
    """
    Implement theoperations to make the 
    concrete concrete product objects
    """
    def create_product_a(self):
        return ConcreteProductA1()
    def create_product_b(self):
        return ConcreteProductB1()
class ConcreteFactory2(AbstractFactory):
    """
    Implement theoperations to make the 
    concrete concrete product objects
    """
    def create_product_a(self):
        return ConcreteProductA2()
    def create_product_b(self):
        return ConcreteProductB2()

class AbstractProductA(metaclass=abc.ABCMeta):
    """
    declare the interface for the type
     of product objects
    """
    @abc.abstractmethod
    def interface_a(self):
        pass
class ConcreteProductA1(AbstractProductA):
    """
    define a product object to be created by the 
    corresponding concrete factory
    Implement the abstract factory interface
    """
    def interface_a(self):
        pass
class ConcreteProductA2(AbstractProductA):
    """
    define a product object to be created by the 
    corresponding concrete factory
    Implement the abstract factory interface
    """
    def interface_a(self):
        pass

### there is another concrete product 

class AbstractProductB(metaclass=abc.ABCMeta):
    """
    declare the interface for the type
     of product objects
    """
    @abc.abstractmethod
    def interface_b(self):
        pass
class ConcreteProductB1(AbstractProductA):
    """
    define a product object to be created by the 
    corresponding concrete factory
    Implement the abstract factory interface
    """
    def interface_b(self):
        pass
class ConcreteProductB2(AbstractProductA):
    """
    define a product object to be created by the 
    corresponding concrete factory
    Implement the abstract factory interface
    """
    def interface_b(self):
        pass

def main():
    for factory in (ConcreteFactory1(), ConcreteFactory2()):
        product_a=factory.create_product_a()
        product_b=factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()

if __name__ == "__main__":
    main()
    