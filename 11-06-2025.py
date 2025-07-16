class IceCream:
    def __init__(self, name, _amount, __flavour):
        self.name = name
        self._amount = _amount
        self.__flavour = __flavour

    def getdetails(self):
        return f"name of the icecream: {self.name}, amount: {self._amount}, flavour: {self.__flavour}"
    
    def getname(self):
        return self.name
    
    def getflavour(self):
        return self.__flavour

    def change(self, flavour):
        self.__flavour = flavour

ice = IceCream("arun", 30, "chocolate")
print(ice.getname())
print(ice.getflavour())       
ice.change("strawberry")
print(ice.getdetails())     
