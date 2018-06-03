"""
define a family of algorithms ,
encapsulate each one and make them interchangeable
Strategy lets the algorithm vary independently from
the CLIENTS that use it 

"""
class Context:
    """
    Define a interface of interest to clients
    maintian a reference to a strategy
    """

    def __init__(self, strategy):
        self._strategy= strategy
    def context_interface(self):
        self._strategy.algorithm_interface()
class Strategy(metaclass= abc.ABCMeta):
    """
    Declare an interface commo to all supported algorithms
    Context uses this interface to call the algorithm defined by a Concrete Strategy
    """
    @abc.abstractmethod
    def algorithm_interface(self):
        pass
class ConcreteStrategyA(Strategy):
    """
    Implement the algorithm using the Strategy interface 
    """
    def algorithm_interface(self):
        pass
class ConcreteStrategyB(Strategy):
    """
    Implement the algorithm using the Strategy interface 
    """
    def algorithm_interface(self):
        pass


def main():
    concrete_strategy_a=ConcreteStrategyA()
    context = Context(concrete_strategy_a)
    context.context_interface()

if __name__ =="__main__":
    main()