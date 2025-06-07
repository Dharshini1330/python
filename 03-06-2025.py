class chocalates:
    def __init__(self,name,flavour):
        self.name=name
        self.flavour=flavour
    def return_chocolates(self):
        print(f"the name of the chocolate is {self.name} and the flavour is {self.flavour}")



choco1=chocalates("galaxy","darkchocolate")
choco2=chocalates("galaxy","whitechocolate")
print(choco1.flavour,choco2.flavour,choco1.name,choco2.name)
choco1.return_chocolates()
choco2.return_chocolates()
