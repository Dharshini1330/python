##single inheritance
class parent:
    def code(self):
        print("good coder")
class child(parent):
    def develop(self):
        print("good developer")
c=child()
c.develop()
c.code()
print(".....................")
##multiple inheritance

class parent1:
    def code(self):
        print("good coder")
class parent2:
    def chef(self):
        print("good chef")

class child(parent1,parent2):
    def develop(self):
        print("good developer")
multi=child()
multi.develop()
multi.code()
multi.chef()
print(".....................")
##multilevel inheritance
class grandparent:
    def code(self):
        print("good coder")
class parent(grandparent):
    def chef(self):
        print("good chef")
class child(parent1):
    def develop(self):
        print("good developer")
m=child()
m.develop()
m.code()
m.chef()


